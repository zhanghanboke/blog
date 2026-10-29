import type { APIRoute } from 'astro';
import { getPosts, postHref, collectCategories, collectTags, categoryHref, tagHref } from '../utils/posts';
import { site } from '../site.config';

export const GET: APIRoute = async () => {
  const posts = await getPosts();
  const cats = collectCategories(posts);
  const tags = collectTags(posts);
  const urls = [
    '/',
    '/posts/',
    '/archive/',
    '/categories/',
    '/tags/',
    '/about/',
    '/search/',
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
