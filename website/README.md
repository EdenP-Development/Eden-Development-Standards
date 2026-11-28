# Eden Practical website — deployment home

The existing hub is the canonical repository. No separate website repository is required.

- website/redesign/ contains the current development records and recovery tools.
- website/public/ will contain the actual deployable static site, and nothing else.
- Private V14 archive: search Drive for eden-practical-artwork-pilot-v14.zip. Its fingerprint is in redesign/review-recovery-v14.json.

Restore the existing candidate locally from the hub root:

    python website/redesign/review-patches/restore_site.py /path/to/eden-practical-artwork-pilot-v14.zip /path/to/new-review-directory

The command restores the 38 actual site files (13 HTML, CSS, 24 artwork) but not the receipt. The result is still the V14 review version; it is NOT a public release. It contains draft notices and noindex. Do not commit uncleared assets or deploy the restored review version automatically.

When the public content is ready, put the approved HTML/CSS/images in website/public/. For initial Cloudflare Pages Direct Upload, upload only that folder. For later Git integration, use the existing hub repository, no framework, repository root, no build command for committed static files, output directory website/public, production branch main and website/public/** build watch path where supported. Disable automatic deployment until the approved files exist. Verify the actual dashboard configuration; this is a proposed setup, not an existing integration.

No need for private staging for ordinary public-ready content. A public preview is public. Test the deployed links, HTTPS and mobile experience. No custom domain purchase is necessary for the initial setup.
