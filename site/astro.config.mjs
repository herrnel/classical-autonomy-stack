// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
//
// NOTE: Update `site` to match your GitHub Pages URL:
//   https://<your-username>.github.io
// `base` is the repository name and must match for project pages.
export default defineConfig({
  site: 'https://herrnel.github.io',
  base: '/classical-autonomy-stack',
  markdown: {
    // Syntax highlighting theme for fenced code blocks (```python, ```js, …).
    // Language is auto-detected from the fence info string.
    shikiConfig: {
      theme: 'github-light',
      wrap: false,
    },
  },
});
