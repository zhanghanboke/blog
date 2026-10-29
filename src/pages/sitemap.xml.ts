import type { APIRoute } from 'astro';
import { getPosts, postHref, collectCategories, collectTags, categoryHref, tagHref } from '../utils/posts';
import { site } from '../site.config';
import { u } from '../utils/base';

export const GET: APIRoute = async () => {
  const posts = await getPosts();
  const cats = collectCategories(posts);
  const tags = collectTags(posts);
  // 静态路径必须过一遍 u()，否则根相对的 '/posts/' 会把 site.url 里的子路径覆盖掉
  const urls = [
    u('/'),
    u('/posts/'),
    u('/archive/'),
    u('/categories/'),
    u('/tags/'),
    u('/about/'),
    u('/moments/'),
    u('/changelog/'),
    u('/search/'),
    ...cats.map((c) => categoryHref(c.name)),
    ...tags.map((t) => tagHref(t.name)),
    ...posts.map(postHref),
  ];
  const body = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map((u) => `  <url><loc>${new URL(u, site.url).href}</loc></url>`).join('\n')}
</urlset>`;
  return new Response(body, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
};
