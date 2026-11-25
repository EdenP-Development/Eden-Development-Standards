package eden.toolkit.preferences

import android.content.SharedPreferences

/**
 * Capture only explicitly allowed non-sensitive preference keys.
 * The caller must exclude credentials, identity, permissions and trust state.
 * Capture again after writes to obtain a fresh view.
 */
fun SharedPreferences.safeSnapshot(keys: Set<String>): SafePreferences {
    require(keys.isNotEmpty()) { "Explicit preference allowlist required" }
    val snapshot = all.filterKeys { it in keys }
    return SafePreferences(snapshot)
}
