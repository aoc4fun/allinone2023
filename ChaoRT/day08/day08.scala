import scala.collection.immutable.Map
import scala.io.Source

val test="""RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""


case class Choice(left:String, right:String):
    def next(c:Char)=
        c match
            case 'L' => left
            case 'R' => right
            case _ => ???

def parseChoice(s:String) =
    s match 
        case "" => "" -> Choice("","")
        case s"$res = ($l, $r)" => res -> Choice(l,r)
        case _ => throw RuntimeException(s"unparsable:[$s]")      
case class State(total:Int, local:Int, length:Int):
    def next() =
        State(total+1, (local +1 )% length, length)
end State

case class InfiniteCharInterator(s:String):
    val chars = s
    var state = State(0, -1, chars.size)
    def next():Char =
        state = state.next()
        chars(state.local)
    def total():Int =
        state.total
end InfiniteCharInterator


def day08P1():Long =
    day08P1(Source.fromFile("day08-input.ctxt").getLines())

def day08P1(s:Iterator[String]):Long=
    val iter = InfiniteCharInterator(s.next())
    s.next()
    val choices = s.map(parseChoice).toMap
    choices.size
    var current = "AAA"
    while current !="ZZZ"
    do
        println(current)
        choices.get(current) match
            case Some(choice) => current = choice.next(iter.next())
            case None => ???
    iter.total()
        
def next(choices:Map[String,Choice])(current:String, pathToTake:Char):String =
    choices.get(current) match
            case Some(choice) => choice.next(pathToTake)
            case None => ???

def start(all:Set[String]):Set[String] =
    all.filter(s => s.endsWith("A")).toSet

def allGood(all:Set[String]):Boolean =
    !all.exists(s => !s.endsWith("Z"))

def day08P2():Long =
    day08P2(Source.fromFile("day08-input.ctxt").getLines())

def cycle(start:String, seq:String, choices:Map[String,Choice]):Long =
    val iter = InfiniteCharInterator(seq)
    var current = start
    while !current.endsWith("Z")
    do
        println(current)
        choices.get(current) match
            case Some(choice) => current = choice.next(iter.next())
            case None => ???
    iter.total()

def gcd(a: BigInt, b: BigInt):BigInt=if (b==0) a.abs else gcd(b, a%b)
def lcm(list: Set[BigInt]):BigInt=list.foldLeft(BigInt(1))((a, b) => (a/gcd(a,b))*b)

def day08P2(s:Iterator[String]):Long=
    val seq = s.next()
    val iter = InfiniteCharInterator(seq)
    s.next()
    val choices = s.map(parseChoice).toMap
    var current = start(choices.keySet)

    val cycles = current.map(s => cycle(s, seq, choices)).map(l => BigInt(l))

    lcm(cycles).toLong