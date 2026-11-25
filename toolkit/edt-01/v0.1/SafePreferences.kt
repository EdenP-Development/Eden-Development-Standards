package eden.toolkit.preferences

enum class ReadStatus { VALID, MISSING, INVALID }
data class ReadResult<T>(val value: T, val status: ReadStatus)

/** Read-only snapshot adapter for non-sensitive preferences. Never writes or logs values. */
class SafePreferences(private val values: Map<String, *>) {
    private fun <T> read(key: String, fallback: T, decode: (Any?) -> T?): ReadResult<T> {
        if (!values.containsKey(key)) return ReadResult(fallback, ReadStatus.MISSING)
        val decoded = decode(values[key]) ?: return ReadResult(fallback, ReadStatus.INVALID)
        return ReadResult(decoded, ReadStatus.VALID)
    }
    fun integer(key: String, fallback: Int, range: IntRange = Int.MIN_VALUE..Int.MAX_VALUE): ReadResult<Int> {
        require(fallback in range)
        return read(key, fallback) { (it as? Int)?.takeIf { n -> n in range } }
    }
    fun boolean(key: String, fallback: Boolean): ReadResult<Boolean> = read(key, fallback) { it as? Boolean }
    fun text(key: String, fallback: String): ReadResult<String> = read(key, fallback) { it as? String }
    fun option(key: String, fallback: String, allowed: Set<String>): ReadResult<String> {
        require(fallback in allowed)
        return read(key, fallback) { (it as? String)?.takeIf { s -> s in allowed } }
    }
    fun strings(key: String, fallback: Set<String>): ReadResult<Set<String>> = read(key, fallback.toSet()) { raw ->
        val set = raw as? Set<*> ?: return@read null
        if (set.any { it !is String }) null else set.filterIsInstance<String>().toSet()
    }
}
