import scala.io.Source


val test=""".....
.S-7.
.|.|.
.L-J.
.....
"""


val up = (0,-1)
val down = (0,1)
val left = (-1,0)
val right = (1,0)

object Directions extends Enumeration {
  type Direction = Value
  val up, down, left, right = Value
}

def possiblePipe(d:Directions.Direction) =
    d match
        case up => Map( '|' -> up, 'F' -> right, '7' -> left) 
        case left => Map('L' -> up, 'F' -> down, '-' -> left)
        case right => Map('J' -> up, '7' -> down, '-' -> right)
        case down  => Map('|' -> down, 'J' -> left, 'L' -> right)


case class Point(source:IndexedSeq[String], x:Int, y:Int):
    val c = source(y)(x)

    def move(dx:Int, dy:Int):Option[Point] =
        if source.head.indices.contains(x+dx) && source.indices.contains(y+dy)
        then Some(Point(source, x+dx,y+dy))
        else None
    def value() = c
end Point


def findS(source:IndexedSeq[String])=
    val res = for {
        y <- source.indices
        x <- source.head.indices
        if source(y)(x) == 'S'
     } yield (x,y) -> source(y)(x)
    res.head



val test2="""..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""

def day10P1(s:Iterator[String]):Long=
    0L

def day10P1():Long =
    day10P1(Source.fromFile("day10-input.ctxt").getLines())

def day10P2(s:Iterator[String]):Long=
    0L

def day10P2():Long =
    day10P2(Source.fromFile("day10-input.ctxt").getLines())

