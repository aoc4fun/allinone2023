import scala.annotation.tailrec
import scala.io.Source
import java.awt.geom.Point2D
import math.Numeric.Implicits.infixNumericOps

val test="""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


val test2="""467
...
..3
...
617
...
..5
...
...
.66"""


case class PointKey(x:Int, y:Int)

case class PointGroup(y:Int, pos:Range, value:Int):
    def extend(newDigit:Int):PointGroup =
        PointGroup(y, Range(pos.start, pos.end+1), value*10 + newDigit)
    def keys():Seq[(PointKey,PointGroup)] =
        for i <- pos.indices
        yield PointKey(pos.start + i,y) -> this
    def next(source: IndexedSeq[String]):Option[Point] =
        if(source.head.indices.contains(pos.end)) then Some(Point(source, pos.end, y))
        else None
end PointGroup

val up = (0,-1)
val down = (0,1)
val left = (-1,0)
val right = (1,0)
val upright = (1,-1)
val upleft = (-1,-1)
val downleft = (-1,1)
val downright = (1,1)
val alldirection = List(up, down, left, right, upright, upleft, downright, downleft)


case class Point(source:IndexedSeq[String], x:Int, y:Int):
    
    val matcher = """^[^\.0-9]$""".r.unanchored
    
    val c = source(y)(x)

    def isDigit():Boolean = 
        Range(0,10).contains(c.asDigit)
    def isSymbol():Boolean =
        c != 46 && !isDigit()

    
    def next():Option[Point] =
        if(source.head.indices.contains(x+1)) then Some(Point(source, x+1, y))
        else None

    def char():Char =
        source(y)(x)

    def move(dx:Int, dy:Int):Option[Point] =
        if source.head.indices.contains(x+dx) && source.indices.contains(y+dy)
        then Some(Point(source, x+dx,y+dy))
        else None

    def touchSymbol():Boolean = 
        alldirection.map(this.move)
        .exists(x => x.isDefined && x.get.isSymbol())

    def value():(Int,Option[Point]) =
        def loop(v:Int, point:Point, touch:Boolean):(Int,Option[Point]) =
            val current = v*10 + point.c.asDigit
            val touching = if(touch) then touch else point.touchSymbol()
            val res = if(touching) then current else 0
            point.next() match
                case None => (res, None)
                case Some(next) => if(!next.isDigit()) then (res, Some(next)) else loop(current, next, touching) 
        if(!isDigit()) then (0, this.next()) else loop(0, this, false)

    def asGroup =
        PointGroup(y, Range(x, x + 1), c.asDigit)

    def asPointKey =
        PointKey(x,y)

    def group():Option[PointGroup] =
        def loop(point:Point, acc:Option[PointGroup]):Option[PointGroup] =
            if(!point.isDigit()) 
            then acc
            else
                val extended = acc match 
                    case None => point.asGroup
                    case Some(group) => group.extend(point.c.asDigit)
                point.next() match
                    case None => Some(extended)
                    case Some(next) => loop(next, Some(extended))
        loop(this, None)
            

    override def toString(): String = s"($x,$y, '$c')"
end Point


def line(source:IndexedSeq[String], y:Int):Int =
    def loop(p:Point, i:Int):Int =
        if(p.isDigit()) then
            val (current, posibleNext) = p.value()
            posibleNext match
                case None => current + i
                case Some(next) => loop(next, current + i)
        else p.next() match
            case None => i
            case Some(next) => loop(next, i)
    loop(Point(source, 0, y), 0)

def lineGroup(source:IndexedSeq[String], y:Int):List[PointGroup] =
    def loop(p:Point, acc:List[PointGroup]):List[PointGroup] =
        p.group() match
            case Some(newGroup) => newGroup.next(p.source) match
                case None => newGroup::acc
                case Some(next) => loop(next, newGroup::acc)
            case None => p.next() match
                case None => acc
                case Some(next) => loop(next, acc)
    loop(Point(source, 0, y), List())

def collectSymbol(source:IndexedSeq[String], y:Int, f: Point => Int):Int =
    def loop(p:Point, acc:Int):Int =
        val newVal = if (p.c == '*') 
            then acc + f(p)
            else acc
        p.next() match
            case None => newVal
            case Some(next) => loop(next, newVal)
    loop(Point(source, 0, y), 0)

def sumGroupsIfTwo(allGroups:Map[PointKey, PointGroup])(p:Point):Int =
    val groups = alldirection.map(p.move).flatten.map(_.asPointKey)
    .map(p => allGroups.get(p)).flatten.distinct
    if groups.size == 2 then groups.map(_.value).fold(1)((a,b) => a * b)
    else 0

val ts = IndexedSeq.from(test.linesIterator)

def scanSourceAndSum(source: IndexedSeq[String], f:(IndexedSeq[String],Int) => Int):Int =
    val lines = for y <- source.indices
                yield 
                    f(source, y)
    lines.sum


def day03P1(s:Iterator[String]):Int =
    val source = IndexedSeq.from(s)
    scanSourceAndSum(source, line)

def day03P1():Int =
    day03P1(Source.fromFile("day03-input1.ctxt").getLines())


def day03P2(s:Iterator[String]):Int =
    val source = IndexedSeq.from(s)
    val allGroupsPerLine = 
        for y <- source.indices
        yield 
            lineGroup(source, y).map(_.keys()).flatten
    val gearDetector=sumGroupsIfTwo(allGroupsPerLine.flatten.toMap)
    val myCollector = collectSymbol(_,_,gearDetector)
    scanSourceAndSum(source, myCollector)

def day03P2():Int =
    day03P2(Source.fromFile("day03-input1.ctxt").getLines()) 
    
        
