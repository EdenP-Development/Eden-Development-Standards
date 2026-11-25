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
    test("snapshot survives map mutation") { data["count"] = 99; check(p.integer("count", 0).value == 3) }
    test("snapshot survives collection mutation") { check(p.strings("items", emptySet()).value == setOf("a", "b")) }
    test("long valid") { check(p.long("long", 0L) == ReadResult(3L, ReadStatus.VALID)) }
    test("long strict type") { check(p.long("count", 0L).status == ReadStatus.INVALID) }
    test("long range") { check(p.long("long", 0L, 0L..2L).status == ReadStatus.INVALID) }
    test("float valid") { check(SafePreferences(mapOf("f" to 1.5f)).float("f", 0f).value == 1.5f) }
    test("float NaN rejected") { check(SafePreferences(mapOf("f" to Float.NaN)).float("f", 0f).status == ReadStatus.INVALID) }
    test("float infinity rejected") { check(SafePreferences(mapOf("f" to Float.POSITIVE_INFINITY)).float("f", 0f).status == ReadStatus.INVALID) }
    test("float range") { check(SafePreferences(mapOf("f" to 2f)).float("f", 0f, 0f, 1f).status == ReadStatus.INVALID) }
    test("nullable missing") { check(p.nullableText("missing", null) == ReadResult(null, ReadStatus.MISSING)) }
    test("nullable wrong type") { check(p.nullableText("count", null) == ReadResult(null, ReadStatus.INVALID)) }
    test("nullable valid") { check(p.nullableText("name", null) == ReadResult("", ReadStatus.VALID)) }
    println("$count tests passed")
}
