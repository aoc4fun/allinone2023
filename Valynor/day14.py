import PIL

import helper.helper as aoc
import math
import logging
from PIL import Image

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sample = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

def prepare_data(data):
    return data.splitlines()

def trans(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def turn(M):
    return [[M[len(M)-j-1][i] for j in range(len(M))] for i in range(len(M[0]))]

def gravity_line(dataline):
    result=[]
    dotcount, ocount=0,0
    for i in range(0,len(dataline)):
        if dataline[i]==".":
            dotcount+=1
        if dataline[i]=="O":
            ocount+=1
        if dataline[i]=="#":
            result.append("."*dotcount+"O"*ocount+"#")
            dotcount, ocount = 0, 0
    result.append("." * dotcount + "O" * ocount)
    return "".join(result)

def printgrav(data):
    for i in data:
        print("".join(i))
    print("----")


def gravity(data):
#    printgrav(data)
    data_r=turn(data)
    data_dest=[]
    for line in data_r:
        data_dest.append(gravity_line(line))
    result=turn(turn(turn(data_dest)))
#    print("=>")
#    printgrav(result)
    return result

def count(data):
    return sum([data[i].count("O")*(len(data)-i) for i in range(0,len(data))])

def part_1(input_data):
    data=prepare_data(input_data)
    return count(gravity(data))

def hash(data):
    return "".join(["".join(x) for x in data])

def part_2(input_data):
    data=prepare_data(input_data)
    counter={hash(data):count(data)}
    found=False
    images=[]
    for i in range(200):
        for _ in range(0,4):
          data = gravity(data)
          data = turn(data)
        images.append(take_image(data))
        result=count(data)
        if hash(data) in counter.keys():
#            print(f"fount it at {i}")
            if not found:
                found=i
                counter={}
            else:
                break
        counter[hash(data)]=count(data)
#    print((1000000000-found)%((i-found)))
#    print(f"first : {found} second {i}")
#    print(list(counter.values())[(1000000000-found)%((i-found))-1])
    images[0].save("out.gif", save_all=True, append_images=images, duration=50, loop=0)
    return list(counter.values())[(1000000000-found)%((i-found))-1]

def take_image(data,size=5):
    x=len(data[0])
    y=len(data)
    newImg1 = Image.new('RGB', (x*size, y*size))
    pixels1 = newImg1.load()
    for line in range(len(data)):
        for geo in range(len(data[0])):
            for i in range(size):
                for j in range(size):
                    pixels1[geo*size+i,line*size+j] = (200*(data[line][geo]=="O"), 0, 200*(data[line][geo]=="#"))
    return newImg1
#im1.save("out.gif", save_all=True, append_images=[im2, im3], duration=100, loop=0)
#newImg1 = PIL.Image.new('RGB', (512,512))
#pixels1 = newImg1.load()
#pixels1[i, 511-j]=(0,0,0)

if __name__ == '__main__':
    assert (part_1(sample) == 136)
    assert (part_2(sample) == 64)

    aoc.retrieve_input(14, 2023)
    load_data = aoc.load_input(14, 2023)
    print(f"Day 14 part 1: {part_1(load_data)}")
    print(f"Day 14 part 2: {part_2(load_data)}")
