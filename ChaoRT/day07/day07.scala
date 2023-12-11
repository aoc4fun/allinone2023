import scala.io.Source
import javax.swing.text.StyledEditorKit.BoldAction

val test="""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

val test2="""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
// 6440

/**
  * Every hand is exactly one type. From strongest to weakest, they are:

    Five of a kind, where all five cards have the same label: AAAAA
    Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    High card, where all cards' labels are distinct: 23456
  */

def countWithGroupBy(string: String) =
    string.groupBy(identity).mapValues(_.map(_ => 1).reduce(_+_))


object Orders extends Enumeration {
  type Order = Value
  val HighCard, Pair, TwoPair, Triple, FullHouse, Four, Five = Value
}

val cardOrderFacial = "AKQJT98765432".reverse
val cardOrderFacialP2 = "AKQT98765432J".reverse

def getOrder(s:String):Orders.Order =
  val maps = countWithGroupBy(s).filter((k,v) => v>1).toMap
  val occurence = maps.values.toSet
  if (occurence.contains(5)) then Orders.Five
  else if (occurence.contains(4)) then Orders.Four
  else if (occurence.contains(3) && occurence.contains(2)) then Orders.FullHouse
  else if (occurence.contains(3)) then Orders.Triple
  else if (occurence.contains(2) && maps.size == 2 ) then Orders.TwoPair
  else if (occurence.contains(2)) then Orders.Pair
  else Orders.HighCard

def addToMax(map:Map[Char,Int], toAdd:Int):Map[Char,Int] =
  if( toAdd ==0 ) then return map

  val max = map.values.max
  val sToChange = map.keys.find(k => {
    val v = map.get(k)
    v.isDefined && v.get == max 
  })
  println(sToChange)
  sToChange match
    case None => ???
    case Some(toChange) => map - toChange + (toChange -> (max + toAdd)) 
      
  
def getOrderP2(s:String):Orders.Order =
  val noJ=s.filter(c => c!='J').toString
  
  if(noJ.isEmpty()) then return Orders.Five

  val maps = countWithGroupBy(noJ).toMap
  
  val max = maps.values.max

  val mapsNew = addToMax(maps, s.length()-noJ.length())
  println(s"$s;$noJ;$maps; -> ${mapsNew}")

  val occurence = mapsNew.values.toSet
  if (occurence.contains(5)) then Orders.Five
  else if (occurence.contains(4)) then Orders.Four
  else if (occurence.contains(3) && occurence.contains(2)) then Orders.FullHouse
  else if (occurence.contains(3)) then Orders.Triple
  else if (occurence.contains(2) && mapsNew.size == 2 ) then Orders.TwoPair
  else if (occurence.contains(2)) then Orders.Pair
  else Orders.HighCard

def facialLowerThan(rank:String)(toCompare:List[(Char, Char)]):Boolean =
  toCompare match
    case Nil => false
    case head::tail => 
      val i0 = rank.indexOf(head(0))
      val i1 = rank.indexOf(head(1))
      if ( i0 < i1) then true
      else if (i0 > i1) then false
      else facialLowerThan(rank)(tail)

  
def handLowerThan(s1:String, s2:String):Boolean =
  val o1 = getOrder(s1)
  val o2 = getOrder(s2)
  if o1 < o2 then true
  else if o1 > o2 then false
  else
    facialLowerThan(cardOrderFacial)(s1.zip(s2).toList)

def handLowerThanP2(s1:String, s2:String):Boolean =
  val o1 = getOrderP2(s1)
  val o2 = getOrderP2(s2)
  if o1 < o2 then true
  else if o1 > o2 then false
  else
    facialLowerThan(cardOrderFacialP2)(s1.zip(s2).toList)

def calc(sortedCards: List[String], cards: Map[String,Int]) =
  for i <- sortedCards.indices
  yield (i.toLong+1) * cards(sortedCards(i)).toLong


def day07P1(source:Iterator[String]):Long=
  val cards = source.map(s => s.split(" ")).map(t => t(0) -> t(1).toInt).toMap
  val sortedCard = cards.keys.toList.sortWith(handLowerThan)
  print(calc(sortedCard, cards))
  calc(sortedCard, cards).sum

  

def day07P1():Long =
    day07P1(Source.fromFile("day07-input.ctxt").getLines())

def day07P2(source:Iterator[String]):Long=
  val cards = source.map(s => s.split(" ")).map(t => t(0) -> t(1).toInt).toMap
  val sortedCard = cards.keys.toList.sortWith(handLowerThanP2)
  println(sortedCard.mkString("\n"))
  print(sortedCard.zip(calc(sortedCard, cards)).mkString("\n"))
  print(sortedCard.size)
  
  calc(sortedCard, cards).sum

// ne marche pas
def day07P2():Long =
    day07P2(Source.fromFile("day07-input.ctxt").getLines())
