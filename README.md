# ラクしる — Japanese editorial affiliate-ready Astro site

**毎日の暮らしを、もっとラクに。** Japanese static editorial website about time-saving household services.

## Stack
Astro 7 + TypeScript; Markdown Content Collections; vanilla CSS; sitemap; RSS; textlint with Japanese rules; static output for Cloudflare Pages.

## Prerequisites / start
Node.js 22.12+ and npm (the project specifies Node 22 in `.node-version`).

```bash
npm install
npm run dev
npm run check
npm run lint:ja
python3 scripts/check_content.py
npm run build
npm run preview
```

`npm install` generates `package-lock.json`; commit this lockfile to GitHub before deploying. If the selected versions have become incompatible, resolve against current compatible Astro packages and regenerate the lockfile. The initial source kit was produced in an offline environment without npm registry access, so dependencies and a successful Astro build were **not** locally verified there.

Textlint preset warnings are signals for editorial review, not substitutes for checking meaning.

## Editing articles
Articles live at `src/content/blog/<slug>.md`. Use frontmatter:

```yaml
---
title: '忙しい人のためのサービスの選び方'
description: '読者に役立つ内容を自然な日本語で説明します。記事のテーマと判断ポイントを短くまとめる紹介文です。'
publishedAt: 2026-10-30
category: meal
readingMinutes: 5
featured: false
sponsored: false
sources: []
---
```

The filename becomes `/articles/<slug>/`. Categories: `meal`, `housework`, `cleaning`, `subscriptions`. Update `src/lib/site.ts` for labels and category definitions. Do not add `updatedAt` unless you really edited the article. Do not claim personal use without evidence.

The `/articles/` index, category pages and RSS build automatically. Add descriptive links to related articles within the Markdown body.

## Brand & images
Approved white-background turquoise `ラ` favicon used in `public/`. Edit `public/favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png`, and `og-default.png` together when refreshing identity. The large original image is provided as `public/images/approved-rakushiru-logo.png`.

The design uses safe Japanese system fonts. It intentionally avoids external Google Fonts requests until fonts can be performance-tested.

## SEO & GEO
Canonical URLs, Open Graph, Article and BreadcrumbList JSON-LD, `robots.txt`, Astro sitemap, and RSS are included. `astro.config.mjs` sets the `site` from the `SITE_URL` environment variable, defaulting to `https://rakushiru.pages.dev`. **Make sure the actual Pages project name/subdomain matches this default or set `SITE_URL` correctly before the first production build.** The site's canonical and sitemap paths must always point to the real production domain.

No fake reviews, ratings, promotional terms, or invented article authors. Review current service terms before making specific claims. There is no special guaranteed GEO markup. Search Console verification must be done separately.

`robots.txt` references the Astro-generated `sitemap-index.xml`. Cloudflare preview URLs should not be submitted for indexing; production canonical targets remain the production site. Consider additional preview-specific noindex headers if your deployment architecture requires them.

## Affiliate / A8.net
`src/lib/affiliate.ts` contains the central campaign map, initially empty. `src/components/AffiliateLink.astro` hides links for missing campaigns and assigns `rel="sponsored noopener noreferrer"` to actual links. `AffiliateDisclosure.astro` displays a prominent notice on articles with `sponsored: true`.

Insert only actual authorized A8.net campaign links and follow advertisers' creative requirements. Disclose advertising clearly. Recheck your policy copy when activating real campaigns.

## Legal/trust readiness
About, editorial, advertising and privacy policies exist. `運営者情報` and `お問い合わせ` are intentionally marked `noindex` while genuine operator details and a functioning contact channel have not been supplied. **Before active monetization**, provide and verify those details and review all published policies against real analytics/advertising practices. Do not publish fictional legal identities or emails.

## GitHub → Cloudflare Pages
1. Create an empty repository `raku-shiru/raku-shiru` on GitHub, if not already created.
2. Push this entire project's files to `main`, including the generated `package-lock.json` after successful `npm install`.
3. In Cloudflare Dashboard → Workers & Pages → Create application → Pages → Connect to Git. Authorize the **Cloudflare Workers & Pages GitHub App** to access this repository.
4. Select `raku-shiru/raku-shiru`, production branch `main`, build command `npm run build`, output `dist`.
5. Set environment variable `SITE_URL=https://<actual-pages-project>.pages.dev` if the assigned subdomain is different from `rakushiru.pages.dev`.
6. Save and deploy, inspect build logs and test live `/`, `/articles/`, four article pages, `robots.txt`, `sitemap-index.xml`, `rss.xml`, and social metadata.
7. Subsequent pushes to `main` will trigger Git integration builds after the integration is connected.

Do **not** create a Direct Upload project if automatic GitHub deploys are required. If a custom domain is added later, update `SITE_URL` and rebuild, then verify canonical URLs and sitemap.

## Quality checklist
- Astro check and build succeed with dependencies installed.
- `npm run lint:ja` reviewed and actionable warnings addressed.
- `python3 scripts/check_content.py` passes.
- View at 375 / 768 / 1440 widths; verify navigation, tables and focus states.
- Run Lighthouse and manual keyboard/a11y testing against the live website. No Lighthouse scores are claimed in this source archive.
- Validate structured data on generated HTML and via Google's Rich Results Test where applicable.

## References
Cloudflare Pages Git integration: https://developers.cloudflare.com/pages/configuration/git-integration/
Astro Content Collections: https://docs.astro.build/en/guides/content-collections/
Google SEO Starter Guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide

## Google Search Console

See [docs/google-search-console.md](docs/google-search-console.md) for URL-prefix verification using the `PUBLIC_GOOGLE_SITE_VERIFICATION` Cloudflare Pages build variable and sitemap submission. No verification token is included in the public source.

## Contact form

The public `/contact/` page uses [FormSubmit](https://formsubmit.co/) to forward messages to `raku-shiru@protonmail.com`. **One-time activation is necessary:** submit a test message from the live form and open the confirmation email in the Proton inbox. Until activation, successful forwarding has not been verified. CAPTCHA/honeypot protection is enabled by the provider. The form service handles contact data; see `src/pages/privacy.astro`. If changing recipient address, update the form action and privacy disclosure, then re-activate.
