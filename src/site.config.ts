import { u } from './utils/base';

export interface NavItem {
  label: string;
  href: string;
  children?: { label: string; href: string; desc?: string }[];
}

export const site = {
  title: '张涵的博客',
  name: '张涵',
  description: '个人技术与生活分享博客',
  // 注意：这里是「含子路径」的完整站点地址，sitemap/RSS 会用它拼绝对链接。
  // 如果改了 astro.config.mjs 里的 base，这里也要同步改。
  url: 'https://zhanghanboke.github.io/blog/',
  lang: 'zh-CN',
  startDate: '2026-10-01',
  avatar: u('/images/avatar.jpg'),
  favicon: u('/images/favicon.png'),
  banner: u('/images/banner.svg'),
  bio: '把知识沉淀下来，把生活记录下来。',
  email: '2832242119@qq.com',
  socials: [
    { label: 'GitHub', href: 'https://github.com/', icon: 'github' },
    { label: 'Bilibili', href: 'https://space.bilibili.com/', icon: 'bilibili' },
    { label: '邮箱', href: 'mailto:2832242119@qq.com', icon: 'mail' },
  ],
  weather: {
    enabled: true,
    city: '武汉市',
    lat: 30.5928,
    lon: 114.3055,
  },
  music: {
    enabled: true,
    playlist: [
      {
        title: '示例环境音',
        artist: 'Demo · 可替换',
        src: u('/music/demo-ambient.wav'),
        cover: u('/images/banner/01.webp'),
      },
    ],
  },
  comments: {
    provider: 'waline' as const,
    serverURL: 'https://blog-waline-henna.vercel.app',
    lang: 'zh-CN',
    login: 'disable' as const,
    requiredMeta: ['nick', 'mail'] as string[],
  },
  features: {
    comments: true,
    search: true,
    toc: true,
    darkMode: true,
  },
};

export const navigation: NavItem[] = [
  { label: '主页', href: '/' },
  { label: '文章', href: '/posts/' },
  { label: '说说', href: '/moments/' },
  {
    label: '归档',
    href: '/archive/',
    children: [
      { label: '时间轴', href: '/archive/', desc: '按年月浏览全部文章' },
      { label: '分类', href: '/categories/', desc: '按主题归类' },
      { label: '标签', href: '/tags/', desc: '按关键词检索' },
    ],
  },
  { label: '更新日志', href: '/changelog/' },
  {
    label: '关于',
    href: '/about/',
    children: [{ label: '关于我', href: '/about/', desc: '个人简介与联系方式' }],
  },
];

export const stats = {
  posts: 0,
  categories: 0,
  tags: 0,
};
