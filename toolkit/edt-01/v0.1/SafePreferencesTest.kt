package eden.toolkit.preferences

fun main() {
    var count = 0
    fun test(name: String, block: () -> Unit) { block(); count++; println("PASS $name") }
    val data = mutableMapOf<String, Any?>("count" to 3, "sound" to false, "name" to "", "theme" to "forest", "items" to mutableSetOf("a", "b"), "mixed" to setOf("a", 1), "null" to null, "long" to 3L)
    val p = SafePreferences(data)
    test("valid integer") { check(p.integer("count", 0) == ReadResult(3, ReadStatus.VALID)) }
    test("missing integer") { check(p.integer("absent", 0) == ReadResult(0, ReadStatus.MISSING)) }
    test("wrong type") { check(p.integer("sound", 0).status == ReadStatus.INVALID) }
    test("range") { check(p.integer("count", 0, 0..2) == ReadResult(0, ReadStatus.INVALID)) }
    test("invalid fallback") { check(runCatching { p.integer("count", 9, 0..2) }.exceptionOrNull() is IllegalArgumentException) }
    test("false preserved") { check(p.boolean("sound", true) == ReadResult(false, ReadStatus.VALID)) }
    test("empty text preserved") { check(p.text("name", "default") == ReadResult("", ReadStatus.VALID)) }
    test("option valid") { check(p.option("theme", "plain", setOf("plain", "forest")).value == "forest") }
    test("option invalid") { check(p.option("theme", "plain", setOf("plain")).status == ReadStatus.INVALID) }
    test("mixed set rejected") { check(p.strings("mixed", setOf("default")) == ReadResult(setOf("default"), ReadStatus.INVALID)) }
    test("set copy") { val result = p.strings("items", emptySet()); (data["items"] as MutableSet<*>).clear(); check(result.value == setOf("a", "b")) }
    test("null invalid") { check(p.text("null", "default").status == ReadStatus.INVALID) }
    test("no numeric coercion") { check(p.integer("long", 0).status == ReadStatus.INVALID) }
    test("no mutation") { val before = data.toMap(); p.integer("name", 0); p.strings("missing", emptySet()); check(data == before) }
    println("$count tests passed")
}
