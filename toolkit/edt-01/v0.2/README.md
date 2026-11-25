# EDT-01 v0.2 — Android adapter candidate

Adds long, finite float, nullable text fallback, copied map/set snapshot, and explicit-key SharedPreferences adapter. Caller must provide stable input during capture and exclude sensitive keys; Android all temporarily reads the entire store before filtering. Returned snapshot is stale after writes: recapture explicitly. No automatic repair, migration, writes, or security decisions. A present null is invalid, not valid nullable storage. Float bounds and defaults must be finite. Preserve old keys/defaults and semantics before adoption.

26 JVM test cases authored (14 inherited, 12 additional); not yet executed for v0.2. Compile with kotlinc SafePreferences.kt SafePreferencesTest.kt -include-runtime -d /tmp/edt01-tests.jar and run java -jar /tmp/edt01-tests.jar. AndroidPreferences.kt requires Android SDK; actual Android adapter compilation/instrumentation and consumer testing remain unverified. v0.1 preserved. No application changes.

## Verified local regression — 2026-11-25
Actual kotlinc compilation and JVM execution passed all 26 tests. Local Git blob hashes matched committed SafePreferences.kt d3dd262f98e0976bd4b56abd382b676360acf8d2 and SafePreferencesTest.kt e6b1854c98987aa1c0980f79d829d2048648e4ec. Android SDK/adapter instrumentation and consumer integration not verified.
