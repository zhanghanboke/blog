import type { APIRoute } from 'astro';
import { getPosts, postHref, formatDate } from '../utils/posts';

export const GET: APIRoute = async () => {
  const posts = await getPosts();
  const index = posts.map((p) => ({
    title: p.data.title,
    href: postHref(p),
    date: formatDate(p.data.date),
    category: p.data.category,
    tags: p.data.tags,
    excerpt: p.data.description,
  }));
  return new Response(JSON.stringify(index), {
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
};
