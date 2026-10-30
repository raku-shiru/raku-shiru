export const SITE_NAME = 'ラクしる';
export const SITE_TAGLINE = '毎日の暮らしを、もっとラクに。';
export const SITE_DESCRIPTION = '宅配食、家事代行、ハウスクリーニング、サブスク。毎日の暮らしに役立つサービスの選び方を、わかりやすく紹介する情報メディア「ラクしる」。';
export const categoryIds = ['meal','housework','cleaning','subscriptions'] as const;
export type CategoryId = typeof categoryIds[number];
export const categories: Record<CategoryId,{title:string;short:string;intro:string;number:string}> = {
  meal: {title:'宅配食・食事サービス',short:'食事をラクに',intro:'毎日の献立や買い物の負担を軽くする、宅配食・ミールキットなどの選び方を紹介します。',number:'01'},
  housework: {title:'家事代行・時短家事',short:'家事をラクに',intro:'家事代行をはじめ、時間を上手に使うためのサービスや考え方をまとめています。',number:'02'},
  cleaning: {title:'掃除・ハウスクリーニング',short:'掃除をラクに',intro:'日常の掃除と専門的なクリーニングの違いや、依頼前に確認したいポイントを解説します。',number:'03'},
  subscriptions: {title:'暮らしのサブスク',short:'固定費を整える',intro:'便利さと費用のバランスを考えながら、暮らしの定額サービスを見直すヒントを紹介します。',number:'04'},
};
export function articleUrl(id:string) { return `/articles/${id}/`; }
export function categoryUrl(id:CategoryId) { return `/categories/${id}/`; }
export function formatDate(d:Date) { return new Intl.DateTimeFormat('ja-JP',{year:'numeric',month:'long',day:'numeric',timeZone:'Asia/Tokyo'}).format(d); }
export const absoluteUrl = (pathname:string, site:URL) => new URL(pathname,site).toString();
