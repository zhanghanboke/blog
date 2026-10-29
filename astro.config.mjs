// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://zhanghanboke.github.io',
  trailingSlash: 'ignore',
  build: {
    format: 'directory',
  },
  markdown: {
    shikiConfig: {
      themes: { light: 'github-light', dark: 'github-dark' },
      wrap: true,
    },
  },
});
