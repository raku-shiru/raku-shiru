/** Only real, approved A8.net tracking URLs belong here. Never fabricate campaigns. */
export type AffiliateCampaign = { label:string; url:string; advertiser:string; checkedAt:string };
export const affiliateCampaigns: Record<string,AffiliateCampaign> = {};
