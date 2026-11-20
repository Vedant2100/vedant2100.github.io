# Design notes

Readers are hiring managers and researchers. The homepage should tell them, in the first screen, who this is, what he works on, and how to reach him, then let them scan the evidence.

## Direction

The page follows the long-standing format of academic homepages: photo, name, a few sentences of plain bio, then dated lists of work with links to the artifacts. It is meant to read as a document, not a product page.

- One text column of about 42rem. A narrow left column holds dates on dated lists.
- Hierarchy comes from type size, weight and spacing. Sections are separated by a hairline rule.
- No cards, eyebrow labels in capitals, gradients, decorative arrows, icon rows, or entrance animations.
- Links are blue and underlined, so they read as links without relying on colour alone.
- Typeface: IBM Plex Sans for everything, with tabular figures for dates.
- Colours are defined once in `_sass/theme/_default_light.scss` and `_default_dark.scss`. Dark mode is neutral grey, not tinted navy.

## Content rules

- Write the bio in first person, in plain sentences, with specific details instead of taglines.
- Every project entry says what was asked or built, and links to the evidence (note, demo, code).
- Only state numbers that the linked material supports. Date past roles as past.
- Keep the research mini-sites (`/fleet-mem/`, `/replaygate/`, `/skillfalsifier/`) untouched; they have their own styles.

## Before merging a UI change

- Build with Jekyll and check the homepage, a post and the timeline.
- Look at 375px, 768px and a wide desktop width, in light and dark.
- Check keyboard focus, the mobile menu, and that no page scrolls sideways.

## Sources consulted

- Refero, "Anti-AI-slop guide": https://github.com/referodesign/refero_skill
- Impeccable, anti-patterns: https://www.mintlify.com/pbakaus/impeccable/concepts/anti-patterns
- Shikun Wei, Clarity template for AI research pages: https://shikun.io/projects/clarity
