# Google Search Console — ラクしる

## Production site

- URL-prefix property: `https://rakushiru.pages.dev/`
- Sitemap: `https://rakushiru.pages.dev/sitemap-index.xml`
- Robots: `https://rakushiru.pages.dev/robots.txt`

Use a **URL-prefix** property for the Cloudflare Pages subdomain. A **Domain** property requires control of a domain's DNS and is not appropriate for the shared `pages.dev` hostname.

## Google Search Console ownership verification

1. Sign in to https://search.google.com/search-console/ using the intended owner Google account.
2. Add a URL-prefix property with the exact URL `https://rakushiru.pages.dev/`.
3. Select **HTML tag** verification, and copy **only the content value** in Google's `<meta name="google-site-verification" content="TOKEN_FROM_GOOGLE" />` tag.
4. In Cloudflare Pages → **rakushiru → Settings → Variables and Secrets / Environment variables**, add a **plain build-time variable** named `PUBLIC_GOOGLE_SITE_VERIFICATION`. Its value should be exactly `TOKEN_FROM_GOOGLE` (replace this placeholder with the token received from Search Console). Set this for **Production**. No private Google credentials are required.
5. Trigger a new Cloudflare Pages production build from the current GitHub branch (or use **Retry deployment** if appropriate). Since Astro produces static HTML, changing a build variable alone does not change already published HTML.
6. Open the homepage source and confirm a non-empty `<meta name="google-site-verification" content="…">` is in the HTML head.
7. Click **Verify** in Search Console. The Google account owner must complete this step.

The verification code is public site metadata, not a password. Do not paste Google account passwords or API keys into the site.

## Submit the sitemap

Once verified, go to **Indexing → Sitemaps** and submit `sitemap-index.xml`. `@astrojs/sitemap` generates this index and its child sitemap automatically on every build. `/robots.txt` advertises the sitemap URL.

## What is already handled

- Unique per-page title / description and absolute canonical URLs.
- Japanese language metadata, Open Graph, and appropriate structured data.
- Crawlable static HTML and a generated XML sitemap.
- `robots.txt` allowing bots to crawl public pages.
- The contact page is indexable and included in the sitemap; the incomplete operator information page remains noindex.

## Custom-domain migration

When you own a custom domain, set `SITE_URL` in Cloudflare Pages to the final canonical origin (for example `https://example.jp`) and redeploy. Add and verify that property in Search Console and resubmit the sitemap. Update any absolute URLs used by the contact form to reflect the new domain.

**Important:** Preparing verification support does not establish ownership with Google. Indexing and search rankings are subject to Google's crawling and indexing processes.
