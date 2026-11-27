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

## Proposed release architecture
Keep standards repository and private Drive archives separate from deployable output. Use a dedicated website repository with approved assets and source only; explicit production release gate, no automatic deployment from standards main. Static output allowlist; exclude receipts, private archives, source models, QA files and credentials. Test access controls using synthetic content before any private preview upload. Noindex is not access control. Verify HTTPS, navigation, 404, mobile, accessibility, headers, external links, privacy/support and artwork clearance. Preserve versioned independent rollback archive; provider retention is not disaster recovery. Domain optional initially; registration/renewal separate. Recheck provider terms and costs before setup. No account, domain purchase, repository creation or deployment authorized by this decision. Next: publication allowlist and owner acceptance checklist.
