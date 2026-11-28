# WEB-09.01 — Hosting evaluation
2026-11-27. Recommendation, not deployment authorization.

Prefer Cloudflare Pages for the static portfolio, subject to owner approval and current service agreement review. Netlify is fallback. GitHub Pages is unsuitable as the long-term commercial business host given its restrictions. Vercel Hobby is noncommercial. No VPS, database, accounts or payment processing needed. Continue using third-party storefronts for purchases.

## Evidence
- https://developers.cloudflare.com/pages/platform/limits/ — 500 builds/month, 20,000 files, 25 MiB per asset, 100 custom domains per free project; provider deployment retention limited.
- https://developers.cloudflare.com/pages/functions/routing/ — free unlimited static requests; functions separate.
- https://developers.cloudflare.com/pages/configuration/git-integration/ — Git integration and automatic previews.
- https://developers.cloudflare.com/pages/configuration/preview-deployments/ — preview access protection available; verify before uploading private material, do not assume a preview URL is private.
- https://developers.cloudflare.com/pages/configuration/custom-domains/ — apex domain requires Cloudflare nameservers.
- https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits — commercial restrictions.
- https://vercel.com/legal/terms — Hobby noncommercial.
- https://www.netlify.com/blog/introducing-netlify-free-plan/ and https://docs.netlify.com/manage/accounts-and-billing/billing-for-credit-based-plans/credit-based-pricing-plans/ — commercial projects allowed, metered free plan.

## Adopted release architecture — owner direction (2026-11-27)
Keep the website in the existing Eden-Development-Standards hub. Do not create another repository. The site is an informational portfolio, not a sensitive application. No mandatory private staging environment, database, login, CMS, analytics or payment service. Cloudflare Pages remains the preferred host, subject to actual account access and applicable terms.

Use website/public/ as the sole deployment output directory once approved content and assets are present. The existing redesign and publication directories remain development resources. Never publish the repository root. A separate public output directory is ordinary deployment hygiene, not a claim the portfolio contains secrets. Keep recovery archives in existing Drive storage. Use simple manual initial deployment and normal Git history for rollback; optional Git integration later with website-only build triggers. No hosting configuration or deployment yet.

Before launch: settle accurate public copy and artwork rights, verify links, check the actual hosted site, confirm support contact and any required product notices. These are practical release tasks, not reasons to invent additional infrastructure. No publication approval inferred for assets previously marked pending.
