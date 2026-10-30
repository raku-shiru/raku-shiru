import rss from '@astrojs/rss';
import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { SITE_NAME,SITE_DESCRIPTION,articleUrl } from '../lib/site';
export const GET: APIRoute = async (context) => {
  const posts=(await getCollection('blog')).sort((a,b)=>b.data.publishedAt.getTime()-a.data.publishedAt.getTime());
  return rss({title:SITE_NAME,description:SITE_DESCRIPTION,site:context.site??'https://rakushiru.pages.dev',items:posts.map(post=>({title:post.data.title,description:post.data.description,pubDate:post.data.publishedAt,link:articleUrl(post.id)}))});
};
