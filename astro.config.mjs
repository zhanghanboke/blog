// @ts-check
import { defineConfig } from 'astro/config';

const BASE = '/blog';

/**
 * Markdown 正文里的站内绝对路径（如 ![](/media/xx.png)、[链接](/posts/xx/)）
 * 不会被 Astro 自动加 base，这里用 rehype 插件统一补前缀。
 */
function rehypeBasePrefix() {
  const fix = (v) =>
    typeof v === 'string' && v.startsWith('/') && !v.startsWith('//') ? BASE + v : v;
  const ATTRS = ['src', 'href', 'poster', 'data-src'];
  return () => (tree) => {
    const walk = (node) => {
      if (node.type === 'element' && node.properties) {
        for (const key of ATTRS) {
          const v = node.properties[key];
          if (Array.isArray(v)) node.properties[key] = v.map(fix);
          else if (typeof v === 'string') node.properties[key] = fix(v);
        }
      }
      if (node.children) node.children.forEach(walk);
    };
    walk(tree);
  };
}

export default defineConfig({
  site: 'https://zhanghanboke.github.io',
  base: '/blog',
  trailingSlash: 'ignore',
  build: {
    format: 'directory',
  },
  markdown: {
    rehypePlugins: [rehypeBasePrefix],
    shikiConfig: {
      themes: { light: 'github-light', dark: 'github-dark' },
      wrap: true,
    },
  },
});
