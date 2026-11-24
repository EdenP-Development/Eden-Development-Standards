# EdenP Development organization transition

Owner created https://github.com/EdenP-Development and authorized ChatGPT for all organization repositories. SudokuTogether transferred successfully; read/write access and post-transfer signing and unsigned build workflows passed. Other repositories must be checked individually; do not assume transfer. Shared standards has now transferred to EdenP-Development/Eden-Development-Standards; organization ownership and connector read/write permissions verified. Use https://github.com/EdenP-Development/Eden-Development-Standards as the canonical location.

Use dedicated organization Actions secrets restricted to the applicable repository. Existing per-repository secrets and public QA signing identities must be audited and preserved where appropriate; do not overwrite existing credentials or automatically generate a replacement. Verify certificate and private-key operation in trusted workflows. Never commit credentials to public Git. Owner-controlled private backup and independent recovery copy remain recommended and existing signing custody requirements apply; organization secrets cannot be read back. No dedicated vault product is necessary.

Itch.io is public development/beta testing; preserve compatible beta updates and saves where practical. Google Play is a distant separate release decision, not an immediate beta gate. No promised cross-channel progress continuity; separate final identity may be chosen. Early supporter rewards remain a future concept. Keep infrastructure proportionate. Owner handles account actions; assistant handles engineering and verification.

Reference working Sudoku signing preflight: https://github.com/EdenP-Development/SudokuTogether/actions/runs/45479430913. This verifies credentials, not a published signed APK. See APP_REGISTRY.json for non-secret channel status.

## Shared publishing and privacy documentation
Maintain shared privacy policy templates, app-specific disclosures based on verified data practices, third-party attribution, publishing guidance, design standards and QA guidance here as needed. Public policy hosting via GitHub Pages is a future option, not yet configured. Do not publish generic policies as accurate app disclosures without auditing actual behavior. Never store private signing credentials here.
