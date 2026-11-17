# Portfolio design brief

This website is for AI research hiring managers and research collaborators. The first screen should answer three questions: what I work on, what evidence exists, and how to contact me. Keep the site on Jekyll; don't replace it with a landing-page framework.

## Information hierarchy

1. A specific research focus and identity.
2. Three selected projects with a clear question, method, or artifact and direct links to evidence.
3. Relevant experience.
4. Smaller projects and coursework in a compact index.
5. Writing and contact information.

Prefer working results, limitations, and reproducible artifacts to claims about impact that the linked evidence does not support. Do not label a work-in-progress as a publication or completed paper. Do not represent past internships as current employment. Keep existing project links accessible even when reorganizing the homepage.

## Visual direction

Quiet technical portfolio, not a startup sales page or newspaper template. Let the research questions and project titles create hierarchy.

- Avoid repeated equal-weight cards, all-caps eyebrow labels, decorative arrows, and invented metrics.
- Use consistent type sizing and a readable line length; preserve the site's light and dark themes.
- Use one clear emphasis point (featured research); keep other items compact.
- Prefer actual project links over icons, badges, or generic calls to action.
- Do not add automatic reveal animations or decorative gradients.
- Keep keyboard focus visible, use semantic headings and links, and let long titles wrap on mobile.

## Open-source guidance

- [Anthropic frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design): subject-specific direction, typography, and critique of generic design patterns.
- [Frontend Craft](https://github.com/nattergabriel/frontend-craft): audit AI-generated design tells and fix existing sites in place.
- [Vercel Web Design Guidelines](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines): accessibility, link semantics, focus, image layout, and responsive QA.
- [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill): optional searchable layout and typography references.

Treat these as review guidance, not a requirement to add runtime dependencies. Review the skills before installation; upstream guidance can change.

## Before merging

- Build Jekyll and check for template errors.
- Review the homepage at 360 px, 768 px, and a wide desktop viewport.
- Check light and dark appearance, mobile navigation, keyboard focus, and long link wrapping.
- Visit every internal homepage link and check that the PDF opens.
- Check claims and dates against the linked projects and latest resume.
- Confirm no unrelated pages (including the research blogs) have changed.
