// @ts-check
import { defineConfig } from 'astro/config';

const BASE = '/blog';
const ATTRS = ['src', 'href', 'poster', 'data-src'];

/** 是否已经带过前缀（幂等，防止 remark / rehype 两层重复加） */
const needs = (p) => typeof p === 'string' && p.startsWith('/') && !p.startsWith('//') && !p.startsWith(BASE + '/');
const add = (p) => (needs(p) ? BASE + p : p);

/**
 * remark 层：处理 Markdown 语法里的图片/链接，以及直接写在 .md 里的原生 HTML 块
 * （本博客大量正文是 HTML，这类内容在 mdast 里是 `html` 节点，rehype 层看不到）
 */
function remarkBasePrefix() {
  const fixRaw = (s) =>
    s.replace(new RegExp(`(${ATTRS.join('|')})=("|')(\\/(?!\\/)[^"']*)\\2`, 'g'), (_m, attr, q, path) => `${attr}=${q}${add(path)}${q}`);
  return (tree) => {
    const walk = (n) => {
      if ((n.type === 'image' || n.type === 'link') && typeof n.url === 'string') n.url = add(n.url);
      if (n.type === 'html' && typeof n.value === 'string') n.value = fixRaw(n.value);
      if (n.children) n.children.forEach(walk);
    };
    walk(tree);
  };
}

/** rehype 层：兜底处理 hast 元素和 raw 节点 */
function rehypeBasePrefix() {
  const fixRaw = (s) =>
    s.replace(new RegExp(`(${ATTRS.join('|')})=("|')(\\/(?!\\/)[^"']*)\\2`, 'g'), (_m, attr, q, path) => `${attr}=${q}${add(path)}${q}`);
  // 必须直接返回 transformer，不能再包一层：
  // unified 会把 transformer 的「返回值」当成新的语法树，
  // 多包一层就等于把整棵正文树换成一个函数，Markdown 会全部渲染成空。
  return (tree) => {
    const walk = (n) => {
      if (n.type === 'element' && n.properties) {
        for (const key of ATTRS) {
          const v = n.properties[key];
          if (Array.isArray(v)) n.properties[key] = v.map(add);
          else if (typeof v === 'string') n.properties[key] = add(v);
        }
      }
      if (n.type === 'raw' && typeof n.value === 'string') n.value = fixRaw(n.value);
      if (n.children) n.children.forEach(walk);
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
    remarkPlugins: [remarkBasePrefix],
    rehypePlugins: [rehypeBasePrefix],
    shikiConfig: {
      themes: { light: 'github-light', dark: 'github-dark' },
      wrap: true,
    },
  },
});
