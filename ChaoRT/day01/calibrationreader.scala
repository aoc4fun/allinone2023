import scala.annotation.tailrec
import scala.io.Source
import scala.runtime.Statics

def toInt(s: String): Option[Int] =
    try{
        Some(s.toInt)
    } catch {
        case e: Exception => None
    }

@tailrec
def left(s:List[Char]): Int =
    s match
        case Nil => 0
        case head :: next => 
            toInt(head.toString()) match
                case Some(value) => value
                case None => left(next)
                
@tailrec
def replace(s:String, toApply: List[(String, Int)]):String =
    toApply match 
        case Nil => s
        case (str,value)::tail => replace(s.replace(str, value.toString), tail)

val numbersName = List("one","two", "three", "four", "five", "six", "seven", "eight", "nine")
val numbersValue = List(1,2,3,4,5,6,7,8,9)
val numbers = numbersName.zip(numbersValue)
 
def left(s:String):Int = left(s.toCharArray().toList)
def right(s:String):Int = left(s.toCharArray().toList.reverse)
def calibration(s:String):Int = left(s)*10 + right(s)
def fixed_calibration(s:String):Int = calibration(replaceFirstLeft(replaceLastRight(s)))
def puzzle1():Long =
    val lines = Source.fromFile("day01-input1.ctxt").getLines()
    lines.toList.map(line => calibration(line)).sum
def puzzle2():Long =
    val lines = Source.fromFile("day01-input1.ctxt").getLines()
    lines.toList.map(line => fixed_calibration(line)).sum

def indexOf(s:String, tupple:(String,Int)):Option[(String, Int, Int)] =
    val index = s.indexOf(tupple._1)
    index match
        case _ if index < 0 => None
        case _ => Some(tupple._1, tupple._2, index)

def lastIndexOf(s:String, tupple:(String,Int)):Option[(String, Int, Int)] =
    val index = s.lastIndexOf(tupple._1)
    index match
        case _ if index < 0 => None
        case _ => Some(tupple._1, tupple._2, index)
def replaceFirstLeft(s:String):String =
    val found = numbers.map(x => indexOf(s, x)).filter(_.isDefined)
    found match
        case Nil => s
        case _ => val head = found.flatten.sortBy(_._3).head
                  "[0-9]".r findFirstMatchIn s match
                    case None => s.replace(head._1, head._2.toString)
                    case Some(value) => if (value.start < head._3) then s else s.replace(head._1, head._2.toString)

def lastNumberInStr(s:String):Option[Int] =
    val allMatch = "[0-9]".r.findAllMatchIn(s).toList
    if(allMatch.isEmpty) None
    else Some(allMatch.last.start)

def replaceLastRight(s:String):String =
    val found = numbers.map(x => lastIndexOf(s, x)).filter(_.isDefined)
    found match
        case Nil => s
        case _ => val head = found.flatten.sortBy(_._3).reverse.head
                  val lastNumber = lastNumberInStr(s) 
                  lastNumber match
                    case None => s.replace(head._1, head._2.toString)
                    case Some(value) => if (value > head._3) s else s.replace(head._1, head._2.toString)


def test():List[String] =
    """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".split("\\n").map(x => replaceFirstLeft(x)).toList

def test2():List[String] =
    """two1nine
eightwothree3
abcone2threexyz
xtwone3four
4nineeightseven
zoneight234oneight
7pqrstsixteen""".split("\\n").map(x => replaceLastRight(x)).toList