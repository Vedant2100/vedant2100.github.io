"""Minimal provider-neutral JSON chat adapter. Never stores or logs credentials."""
import json
import os
import urllib.request


def ask_json(system: str, user: str, *, model: str, base_url: str = 'https://api.openai.com/v1',
             key_env: str = 'OPENAI_API_KEY', temperature: float = 0.0) -> dict:
    key = os.environ.get(key_env, '')
    if not key:
        raise RuntimeError(f'{key_env} is unset; use --backend mock or configure a real provider')
    url = base_url.rstrip('/') + '/chat/completions'
    request_body = {
        'model': model, 'temperature': temperature,
        'messages': [{'role': 'system', 'content': system}, {'role': 'user', 'content': user}],
    }
    request = urllib.request.Request(url, data=json.dumps(request_body).encode(),
             headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'}, method='POST')
    with urllib.request.urlopen(request, timeout=90) as response:
        payload = json.load(response)
    raw = payload['choices'][0]['message']['content'].strip()
    if raw.startswith('```'):
        raw = raw.split('\n', 1)[-1].rsplit('```', 1)[0].strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError('Model produced invalid JSON (not treated as success): ' + raw[:350]) from exc
