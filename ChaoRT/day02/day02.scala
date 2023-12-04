import scala.compiletime.ops.boolean
import scala.io.Source


val test = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

val line = test.split(':').collect { case s"Game $id" => id case s" $rest" => rest }


def parseSetsAndGetMaxPerColor(s:String):Map[String,Int] =
    s.split(";").map(parseGame(_)).reduce((m1,m2) => mergeMax(m1,m2)) 

def parseGame(s:String):Map[String,Int] =
    s.trim().split(", ").collect { case s"$count $color" => (color, count.toInt) }.toMap

val t1 =parseGame("3 blue, 4 red, 22 green")
val t2 =parseGame("3 yellow, 22 red, 12 green")


def getMax(i1: Option[Int],i2: Option[Int]):Int =
    i1 match
        case Some(i) => i2 match
            case None => i
            case Some(ii) => if(i > ii) i else ii
        case None => i2 match
            case None => -1
            case Some(value) => value
    
def mergeMax(m1: Map[String, Int], m2: Map[String, Int]) =
    (m1.keySet ++ m2.keySet).map(key => (key, getMax(m1.get(key), m2.get(key)))).toMap

def gameIsPossible(stock: Map[String, Int], game:Map[String, Int]) =
    game.keySet.forall(key => stock.isDefinedAt(key) && game.get(key).get <= stock.get(key).get)

val stockP1 = parseGame("12 red, 13 green, 14 blue")

val sampleP1 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".split("\n")


def parseLine(s:String):Array[String] =
    s.split(':').collect { case s"Game $id" => id case s" $rest" => rest }

def load() = 
    Source.fromFile("day02-input1.ctxt").getLines()
 
def day02P1(s:Iterator[String]):Long =
    s.map(parseLine(_)).map(line => if gameIsPossible(stockP1, parseSetsAndGetMaxPerColor(line(1))) then line(0).toInt else 0).sum

def powerOfCube(minStock: Map[String,Int]):Long =
    minStock.values.reduce((i,j) => i * j)

def day02P2(s:Iterator[String]):Long =
    s.map(parseLine(_)).map(line => powerOfCube(parseSetsAndGetMaxPerColor(line(1)))).sum
