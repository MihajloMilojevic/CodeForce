fun case(): String {
    val s = readLine()!!
    for (i in s.length - 1 downTo 0) {
        if (s[i] != '0') {
            return s.substring(0, i)
        }
    }
    return ""
}

fun main() {
    val t = readLine()!!.toInt()
    val rez = mutableListOf<String>()
    repeat(t) {
        rez.add(case())
    }
    for (r in rez) {
        println(r)
    }
}

