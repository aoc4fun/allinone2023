from itertools import combinations

example = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

my_input=""".....................#..................#..................................................................#...........#....................
................................................................#..................#........................................................
..........................#.....#.............................................................#........#..................................#.
...#.......#...........................................#........................................................#...........................
............................................................................................................................................
........................................................................#.....#.................................................#......#....
...............................................#.................#...................#......#..............#................................
.................#.................#.....................................................................................#.................#
......................#....................................................#................................................................
...........#.......................................................................................#........................................
...........................#......................#............................#.......#.....................................#..............
........................................................#......#.......#................................#.........................#......#..
...............................................................................................#............................................
.#.....................#..................#.....................................................................#...........................
..............................#......#.................................................................................#....................
................#....................................#.......................#..............................................................
........#...................................................................................#..............................................#
.........................#....................................#.......................................#............#........................
...................................................................#..............#.........................................................
..................................#...........#...............................................................#.............................
.#.................................................................................................#.....................#..................
.........#...................................................................................#..............................................
..............#........................#...............#.............#...............................................................#......
..........................#............................................................................#.............#......................
.................................................................................#.....#....................................................
.......#...................................................#...............#....................................................#...........
....................................#.......#.....................................................#.........................................
#...............................................................#.....................................................................#.....
...............#..................................#.........................................................#..........#....................
................................#.................................................................................................#.........
.........................#.......................................................#.........................................................#
............................................................#...........#...............#...................................................
....#......#.....................................................#..........................................................................
........................................................................................................#.......................#.....#.....
.............................................................................................#..............................................
....................................#........#.......................................#.....................................#................
...........................................................................................................#.......#........................
#........................#.............................#..........................................................................#.........
...........#......................................#.........................#..........................#.................................#..
................#.....................#...........................................#.........................................................
...#.............................#...........................................................................#.........#....................
............................................#.......................#...........................#...........................................
.....................................................................................................#......................#...............
#.........................................................................................#.................................................
.............................#.......................................................................................#....................#.
...........#.............................#......#........#.....#.......#......#.............................#...............................
...................#........................................................................................................................
...................................................................................................................................#........
.#............#.............................#......#...............................#....................................#...................
..........................#.........#...................................................................#...................................
.....................................................................#.............................#...........................#............
................................................................................................................#...........................
...........................................................#..................................#.............................................
........#....................#....................................#...................#.................................................#...
...#...............#.............................#.....................................................................#....................
.........................#..........#.....#................................#........................#.......................................
................................................................................#..............................#................#...........
............................................................................................................................................
....................................................................................#........#..............................................
............................................................#..........#..........................#.........................................
.............................#........#................#................................................#...............#...................
......................#............................................#........................................................................
.#..........#.........................................................................#.....................................................
..................#..........................................................................................#...................#..........
.......#.........................#................#..........................#.......................#................#................#....
.........................................................#..................................................................................
.....................................................................#......................................................................
............................................#...................#....................#.............................#........................
......................................#.....................................................................................................
...#.......................................................................................................................#................
.......................#..........................#......................................................#.....#............................
.................................#..........................................................................................................
.............#....................................................#........#...........................................................#....
............................................................................................................................................
............................................................................................................................................
.................................................#.....#....................................#......................#..............#.........
.................#............................................................#.............................#.............................#.
............#............................#.........................................#.............#..........................................
.......#...............#........................................................................................#...........................
..................................#............#..............#.....#..................................#....................................
...........................................................................#................................................................
..#.......#.....#............#...........................#............................#..............................#......................
........................................#.......................................#.................#.......................................#.
............................................................................................................................................
..........................#.......................#..............#..........................................................................
..................................#.........................................................................................................
.#..................................................................................................................#.......................
................#.....................#.....................#...............#...................#............#..............................
.........#..................................................................................................................................
................................#..............#........................#.................#........................................#........
............................................................................................................................................
#...................#...................#.......................................................................#........................#..
............................#....................................#............#.......#....................#................................
............................................................#......................................#........................................
...................................................................................................................#.........#..............
..................................................#.................#....................#..............................#...................
........................#..............................#..........................#.........................................................
............#..........................#...................................#.....................#.......#..........................#.......
..................#.............#...........................................................................................................
.....#......................................................................................................................................
.......................................................................#..............................................#.....................
.........#................#................................#........................#.......................#...............................
....................#................#.......#.....................................................................................#........
..................................................#.........................#........................#.............#..........#.............
.#...................................................................#......................................................................
.................................................................................#......#.....................#........#....................
.....#...................................#..................................................................................................
.....................................................#.................................................#....................................
..............#...................#.............................#.................................................................#......#..
........#...........#.......................................................................#.............................#.................
.................................................................................................#..........................................
..........................................................................................................#.....#...........................
..........................#........................#........................................................................................
.#................#.......................#.......................................#..................................#......................
.........#.....................#.....#.................................................................................................#....
............................................................................................#...............................................
.....................................................................#.......................................#..............................
..............................................#............................#............................#.....................#.............
.........................................#................#......................................#.....................#....................
................................#...........................................................................................................
#.....#.........#...............................................#.............#.............................................................
...........................#.......................................................#......................#.................#.......#......#
...........................................................................................#........#.......................................
....................#...................#................#..............#...................................................................
..............................................................#.............................................................................
..........#.......................#..................................................#...............................#......................
...............#..............................................................................#........#.............................#......
.........................#...................#.......#.............#...........................................#...........#................
.....................................#....................................................#.................................................
....................#.............................................................#.....................................................#...
.......#....................................................................#...............................................................
...............................................................#....................................#...........................#...........
...............#...........................#..........................................................................#.....................
.................................#......................................................#...........................................#.......
#........#.........................................#......#.................................................................................
..............................................................................#..........................#..................................
.....#..................#...................................................................................................................
.......................................................#.......#.....#...........................................#.............#............
....................#...............#............#..........................................................................................
.................................................................................#......#..............................................#...."""

def expand_rows(input):
  res = ""
  lines = input.splitlines()
  for line in lines:
    res += line + "\n"
    if all(c in [".", "o"] for c in line):
      res += "o" * len(line) + "\n"

  return res

def expand_cols(input):
  lines = input.splitlines()
  to_expand = []
  for x in range(len(lines[0])):
    if all(c  in [".", "o"] for c in [line[x] for line in lines]):
      to_expand.append(x)

  res = ""
  for line in lines:
    for x in range(len(lines[0])):
      res += line[x]
      if x in to_expand:
        res += "o" 
    res += "\n"
  return res

def expand(input):
  return expand_rows(expand_cols(input))

def dist(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_pairs(input):
  input = expand(input)
  lines = [list(x) for x in input.splitlines()]
  stars = []
  for y in range(len(lines)):
    for x in range(len(lines[0])):
      if lines[y][x] == "#":
        stars.append((x,y))

  return list(combinations(stars, 2))

def part1(input):
  pairs = find_pairs(input)
  return str(sum(dist(a, b) for a, b in pairs))

def part2(input, expansion):
  pairs = find_pairs(input)
  input = expand(input)
  res = 0
  lines = input.splitlines()
  for a,b in pairs:
    d = dist(a, b)
    for x in range(min(a[0], b[0]), max(a[0], b[0])):
      if lines[0][x] == "o":
        d += expansion - 2
    for y in range(min(a[1], b[1]), max(a[1], b[1])):
      if lines[y][0] == "o":
        d += expansion - 2
    res += d
  return str(res)

print("Total distance part1 example : " + part1(example))
print("Total distance part1 my input : " + part1(my_input))


print("Total distance part2 example with expansion 10 : " + part2(example, 10))
print("Total distance part2 example with expansion 100 : " + part2(example, 100))
print("Total distance part2 my input with expansion 1000000 : " + part2(my_input, 1000000))

