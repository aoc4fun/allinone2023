import scala.annotation.tailrec
import scala.io.Source
import java.awt.geom.Point2D
import scala.math._
import scala.collection.mutable.Map

val test="""Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def parseInt(s:String):Set[Int] =
    s.split(" ").filter(!_.isEmpty()).map(_.toInt).toSet

def calcScore(win:Set[Int], current:Set[Int]) =
    val wins = current.count(win.contains(_))
        wins match
            case 0 => 0
            case 1 => 1
            case n => pow(2,n-1).toInt

def countWin(win:Set[Int], current:Set[Int]):Int =
    current.count(win.contains(_))
    
case class Card(id:Int, score:Int, count:Int):
    def add(i:Int) = 
        Card(id, score, count+i)

    def updateMap(cards:Map[Int,Card]) =
        cards.put(id, this)
    def applyEffects(cards:Map[Int,Card]):Card =
        val cardsIds = Range(0, score) // end is not in range
        for (i <- 1 to score) 
            cards.get(this.id + i) match
                case None => throw RuntimeException(f"Card not found:${this.id+1}") 
                case Some(c) => c.add(count).updateMap(cards);
        this
end Card

def parseCard(s:String, f:(Set[Int], Set[Int]) => Int):Card =
    val line = s.split(':').collect { case s"Card $id" => id case s" $rest" => rest }
    val id = line(0).trim().toInt
    val rest = line(1)
    val numbers = rest.split('|').map(_.trim()).map(parseInt)
    Card(id, f(numbers(0), numbers(1)), 1)

def day04P1(s:Iterator[String]):Long =
    s.map(parseCard(_, calcScore).score).sum

def day04P1():Long =
    day04P1(Source.fromFile("day04-input1.ctxt").getLines())

def day04P2(s:Iterator[String]) =
    val mutaCars = scala.collection.mutable.Map[Int, Card]()
    val cards = s.map(parseCard(_, countWin)).map(c=>c.id -> c).toMap[Int,Card]
    mutaCars.addAll(cards)
    val cardsAfterEffect = 
        for i<-mutaCars.keys
        yield mutaCars(i).applyEffects(mutaCars)
    cardsAfterEffect.toArray.map(c => c.count).sum

def day04P2():Int =
    day04P2(Source.fromFile("day04-input1.ctxt").getLines())
