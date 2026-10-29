/**
 * 站点基础路径（Astro `base` 配置）。
 * 根部署时为空字符串，子路径部署（如 GitHub Pages 项目仓库 /blog）时为 '/blog'。
 *
 * Astro 只会给 `_astro` 下的构建产物自动加 base，
 * public/ 里的资源和手写的内部链接都必须手动加前缀，否则部署到子路径会 404。
 */
export const BASE: string = (import.meta.env.BASE_URL || '/').replace(/\/+$/, '');

/** 给站内绝对路径加上 base 前缀，外链和锚点原样返回。 */
export function u(path: string): string {
  if (typeof path !== 'string') return path;
  // 外链、协议相对链接、mailto/tel、锚点：不加前缀
  if (!path.startsWith('/') || path.startsWith('//')) return path;
  return BASE + path;
}
