# EDT-01 v0.1 — Safe preference reads

2026-11-25. Original dependency-free Kotlin/JVM implementation inspired by Grid Hunt's typed read helpers. For non-sensitive settings only. Accept a caller-owned stable map snapshot (e.g. a copy of SharedPreferences.all); do not mutate the map or its collections concurrently with reads. Valid, missing and invalid statuses are explicit. Reads do not write, clear, migrate, log or repair stored data. Strict types; integer ranges and allowed string options; entire malformed sets rejected; returned sets copied. Invalid fallback configuration throws. No nullable text, float/long, schema migration, transactional backup or security policy support yet. Never apply permissive defaults to authentication, permissions, encryption or trust decisions. Do not write returned defaults back automatically. Consumer-specific migration semantics require review, especially where existing Grid Hunt helpers filter mixed sets rather than rejecting them.

## Local verification
Compile and run:
```sh
kotlinc SafePreferences.kt SafePreferencesTest.kt -include-runtime -d /tmp/edt01-tests.jar
java -jar /tmp/edt01-tests.jar
```
14/14 tests passed in actual Kotlin/JVM execution; repository blob IDs matched tested files: source 08684ab07a08a33ba39a803fbc7d8c3d91377d8d, tests a1ce0735cbe41d58568bd0503af2959ecb0bd3aa. No Android instrumentation or consumer integration yet. Next add a SharedPreferences adapter and verify on a disposable QA consumer while preserving exact existing keys, defaults and data. No app changes or license changes.
