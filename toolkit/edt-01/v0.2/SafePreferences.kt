package eden.toolkit.preferences

enum class ReadStatus { VALID, MISSING, INVALID }
data class ReadResult<T>(val value: T, val status: ReadStatus)

/** Read-only snapshot adapter for non-sensitive preferences. Never writes or logs values. */
class SafePreferences(values: Map<String, *>) {
    private val values: Map<String, Any?> = values.mapValues { (_, value) ->
        if (value is Set<*>) value.toSet() else value
    }
    private fun <T> read(key: String, fallback: T, decode: (Any?) -> T?): ReadResult<T> {
        if (!values.containsKey(key)) return ReadResult(fallback, ReadStatus.MISSING)
        val decoded = decode(values[key]) ?: return ReadResult(fallback, ReadStatus.INVALID)
        return ReadResult(decoded, ReadStatus.VALID)
    }
    fun integer(key: String, fallback: Int, range: IntRange = Int.MIN_VALUE..Int.MAX_VALUE): ReadResult<Int> {
        require(fallback in range)
        return read(key, fallback) { (it as? Int)?.takeIf { n -> n in range } }
    }
    fun long(key: String, fallback: Long, range: LongRange = Long.MIN_VALUE..Long.MAX_VALUE): ReadResult<Long> {
        require(fallback in range)
        return read(key, fallback) { (it as? Long)?.takeIf { n -> n in range } }
    }
    fun float(key: String, fallback: Float, minimum: Float = -Float.MAX_VALUE, maximum: Float = Float.MAX_VALUE): ReadResult<Float> {
        require(minimum.isFinite() && maximum.isFinite() && minimum <= maximum)
        require(fallback.isFinite() && fallback in minimum..maximum)
        return read(key, fallback) { (it as? Float)?.takeIf { n -> n.isFinite() && n in minimum..maximum } }
    }
    fun nullableText(key: String, fallback: String?): ReadResult<String?> {
        if (!values.containsKey(key)) return ReadResult(fallback, ReadStatus.MISSING)
        val value = values[key]
        return if (value is String) ReadResult(value, ReadStatus.VALID)
        else ReadResult(fallback, ReadStatus.INVALID)
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
