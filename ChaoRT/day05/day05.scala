
import scala.collection.mutable.Map
import scala.io.Source

val test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

case class LongRange(start:Long, endExcluded:Long):
    def contains(l:Long) =
        start <= l && l<endExcluded
case class Filter(source:Long, dest:Long, length:Long):
    val sourceRange = LongRange(source, source+length)
    def transform(l:Long):Long =
        if(sourceRange.contains(l)) then dest+l-source
        else l
    def contains(l:Long):Boolean =
        sourceRange.contains(l)
end Filter
def parseFilter(s:String):Filter =
    val parts = s.split(" ").map(_.toLong)
    Filter(parts(1),parts(0),parts(2))

case class Mapper(source:String, dest:String, filters:List[Filter]):
    def setFilters(arr:List[Filter]) =
        Mapper(source, dest, arr)
        
    def transform(l:Long):Long =
        filters.find(f => f.contains(l)) match
            case Some(filter) => filter.transform(l)
            case None => l
end Mapper

def parseMapper(s:Iterator[String]) =
    var name = s.next()
    if(name.isBlank()) name = s.next()

    var res = name match 
        case s"$source-to-$dest map:" => Mapper(source, dest, List())
        case _ => throw RuntimeException(s"uknown name: $name")
    def parseNext(s:Iterator[String], acc:List[Filter]):List[Filter] =
        val next = if(s.hasNext) then s.next() else ""
        next match
            case "" => acc
            case _ => parseNext(s, parseFilter(next)::acc)
    val allFilter = parseNext(s, Nil).reverse
    res.setFilters(allFilter)

case class GardenMap():
end GardenMap

def transform(seed: Long, mappers: Map[String, Mapper])=
    def loop(step:String, l:Long, mappers: Map[String, Mapper]):Long =
        mappers.get(step) match
            case None => l
            case Some(mapper) => loop(mapper.dest, mapper.transform(l), mappers)
    loop("seed", seed, mappers)

def parseSeed(s:String):Seq[Long] =
    val parts = s.split(":")
    parts(1).split(" ").map(_.trim).filter(!_.isEmpty).map(_.toLong).toSeq

def getMinOfRange(s:Long, e:Long, mappers: Map[String, Mapper]):Long =
    var i = s
    var min=Long.MaxValue
    while i <= e
    do
        val tmp = transform(i, mappers)
        min = if(tmp<min) then tmp else min
        i = i + 1
    min

def day05P1(s:Iterator[String]):Long=
    val seed = parseSeed(s.next())
    val mappers = Map[String, Mapper]()

    while s.hasNext
        do 
            val newMapper = parseMapper(s)
            mappers.put(newMapper.source, newMapper)
    seed.map(transform(_, mappers)).min

def day05P1():Long =
    day05P1(Source.fromFile("day05-input.ctxt").getLines())


def day05P2(s:Iterator[String]):Long=
    val seed = parseSeed(s.next())
    val mappers = Map[String, Mapper]()

    while s.hasNext
        do 
            val newMapper = parseMapper(s)
            mappers.put(newMapper.source, newMapper)
    getMinOfRange(seed(0), seed(0)+seed(1), mappers)

def day05P2():Long =
    day05P2(Source.fromFile("day05-input.ctxt").getLines())


/**
 * --- Part Two ---

Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

seeds: 79 14 55 13

This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?

**/