import scala.io.Source
import scala.collection.mutable.Stack


val test="""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

def readLIne(s:String) =
    s.split(" ").map(_.toInt).toList

def reduce(l:List[Int]):List[Int] =
    val tmp = l.reverse.tail.reverse
    l.tail.zip(tmp).map((a,b) => a - b ).toList

def allNull(l:List[Int]) =
    l.find(a => a!=0) match
        case None => true
        case _ => false

def load(l:List[Int]):Stack[List[Int]]=
    def loop(l:List[Int], acc:Stack[List[Int]]):Stack[List[Int]] =
        val r = reduce(l)
        if(allNull(r)) then acc.push(r)
        else loop(r, acc.push(r))
    loop(l, Stack[List[Int]](l))

def genNext(l:List[Int], s:Stack[List[Int]]) =
    val h = l.reverse.head
    val r = s.pop().reverse
    val n = r.head + h
    val newL = n :: r
    s.push(newL.reverse)
    s

def genNextP2(l:List[Int], s:Stack[List[Int]]) =
    val h = l.head
    val r = s.pop()
    val n = r.head - h
    val newL = n :: r
    s.push(newL)
    s

def genAll(l:List[Int], f:(List[Int], Stack[List[Int]]) => Stack[List[Int]]) =
    val s = load(l)
    def loop(acc:Stack[List[Int]]):List[Int] =
        acc match
            case acc if acc.size == 1 => acc.pop()
            case s => loop(f(acc.pop, acc))
    loop(s)

def day09P1(s:Iterator[String]):Long=
    s.map(readLIne).map(genAll(_,genNext)).map(l => l.reverse.head).sum

def day09P1():Long =
    day09P1(Source.fromFile("day09-input.ctxt").getLines())

def day09P2(s:Iterator[String]):Long=
     s.map(readLIne).map(genAll(_,genNextP2)).map(l => l.head).sum

def day09P2():Long =
    day09P2(Source.fromFile("day09-input.ctxt").getLines())

