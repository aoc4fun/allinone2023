let example = `R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)`

let my_input = `L 4 (#6c74e0)
D 4 (#1afab1)
L 4 (#0b54a0)
D 18 (#3533c1)
L 3 (#411270)
U 14 (#121ed3)
L 4 (#17e0f0)
U 10 (#113841)
L 8 (#4fa040)
U 13 (#113843)
L 3 (#1b7fb0)
U 7 (#121ed1)
L 10 (#005ed0)
D 4 (#502e73)
L 5 (#47ebf0)
D 10 (#2d9421)
R 7 (#2d4360)
D 8 (#2d9423)
L 7 (#2164d0)
D 8 (#530f03)
L 9 (#14d330)
D 14 (#1c6c43)
L 8 (#5133e0)
U 13 (#2ec813)
L 7 (#2c56a0)
U 6 (#2b50c3)
L 14 (#465990)
U 3 (#5c9e03)
L 6 (#052cf0)
U 7 (#09d973)
L 10 (#3500b0)
D 11 (#088d63)
L 11 (#473f60)
U 11 (#405733)
L 5 (#414100)
U 5 (#10b5b3)
L 9 (#624920)
U 8 (#10b5b1)
L 10 (#02a810)
U 7 (#29a8c1)
L 14 (#6896c2)
U 7 (#4a0001)
L 6 (#07ef12)
U 4 (#399321)
L 7 (#2054f0)
U 8 (#226a41)
R 8 (#5030e0)
U 6 (#57a921)
R 3 (#3f7160)
U 11 (#4df573)
R 6 (#49fe20)
U 13 (#1c3d03)
R 9 (#4f4362)
U 3 (#0ba303)
R 8 (#75c3f2)
U 13 (#3e1493)
R 12 (#0af520)
U 6 (#3dc1b3)
L 4 (#0e7730)
U 2 (#36f991)
L 8 (#565800)
D 5 (#36f993)
L 6 (#554300)
U 5 (#35a393)
L 8 (#3ff8c0)
U 7 (#345003)
R 11 (#0140c0)
U 5 (#34d343)
R 11 (#0140c2)
U 3 (#3da6b3)
R 2 (#368952)
U 8 (#6c3473)
R 5 (#132af2)
U 5 (#47ae31)
R 11 (#479542)
D 5 (#34c7d1)
R 3 (#096fc2)
D 4 (#00bec1)
R 9 (#1f8712)
D 10 (#317681)
R 3 (#475352)
D 2 (#463703)
R 12 (#2e2f12)
U 4 (#260611)
L 8 (#2fa902)
U 7 (#260613)
L 2 (#5461a2)
U 6 (#463701)
L 11 (#3050d2)
U 11 (#508b33)
L 11 (#258512)
U 14 (#5e2013)
L 4 (#2b63a2)
U 2 (#6c3471)
L 7 (#297132)
U 9 (#0a6333)
L 14 (#4c7b92)
U 4 (#6f3b33)
L 16 (#4c7b90)
U 6 (#09f3c3)
L 15 (#053fa2)
U 5 (#4ad5c3)
R 8 (#1f96b0)
U 7 (#5c6d63)
R 5 (#0835f2)
U 11 (#4d5af3)
R 6 (#525352)
U 8 (#165b63)
R 3 (#5a8940)
U 4 (#099e83)
L 3 (#1f96b2)
U 16 (#1af253)
L 6 (#767070)
U 4 (#231d23)
L 7 (#02a910)
U 9 (#42f673)
L 12 (#0b64d0)
U 3 (#27b9c3)
L 4 (#21b400)
U 10 (#1744e3)
L 12 (#5a75e0)
U 8 (#42c5c3)
L 12 (#199ed2)
U 13 (#4cefc3)
L 9 (#245442)
U 8 (#119c61)
R 10 (#095c02)
U 11 (#68be41)
R 6 (#14ae52)
D 9 (#161161)
R 4 (#03bf22)
D 6 (#121833)
L 4 (#11a032)
D 12 (#1d8a53)
R 8 (#570a92)
D 5 (#4f2d23)
R 9 (#24dc02)
U 6 (#119c63)
R 5 (#230162)
U 9 (#1b8183)
L 13 (#19a6f2)
U 10 (#5dbb13)
R 13 (#200702)
U 7 (#5ee763)
R 5 (#059f22)
D 3 (#5ee761)
R 10 (#1a4342)
D 8 (#394c93)
R 12 (#0a6d32)
U 8 (#5756d1)
R 8 (#1ca732)
D 10 (#22af01)
R 3 (#424712)
D 9 (#53bcc3)
R 9 (#331712)
D 10 (#264913)
R 4 (#244212)
D 7 (#3f48b3)
R 8 (#54dec2)
D 14 (#515d83)
R 4 (#4d5930)
D 8 (#058093)
R 5 (#3738b0)
D 3 (#2b5173)
R 9 (#1f3660)
D 16 (#4c7f03)
R 5 (#6179a0)
D 3 (#548343)
R 5 (#4a2640)
D 3 (#106533)
R 6 (#1cfc70)
U 4 (#184de3)
R 4 (#234e70)
U 9 (#67b7f1)
R 7 (#2a16d0)
U 7 (#24fea1)
R 9 (#564262)
D 4 (#436f31)
R 8 (#564260)
D 10 (#24e101)
R 12 (#4df570)
D 2 (#152b43)
R 9 (#2bcb50)
D 8 (#5e2443)
L 3 (#444350)
D 4 (#13c883)
L 16 (#079a60)
D 2 (#2e75b3)
L 2 (#5ffa70)
D 7 (#3aede3)
L 8 (#0231f0)
D 13 (#0cc973)
R 5 (#3986f0)
D 11 (#0486a3)
R 7 (#34db30)
D 8 (#609e53)
R 3 (#44d400)
D 8 (#4c3ca1)
L 15 (#40a880)
D 5 (#18e851)
R 5 (#24f640)
D 6 (#0cc971)
R 9 (#03f810)
D 8 (#46d213)
R 4 (#2a68f0)
D 18 (#179ca3)
R 3 (#58afe0)
U 18 (#4cf4b3)
R 2 (#2ac350)
U 2 (#18ecd3)
R 10 (#0e0360)
U 5 (#2df743)
R 11 (#4e89a0)
U 13 (#4beca3)
R 6 (#5610e0)
U 5 (#155291)
R 3 (#6dbb30)
U 5 (#03dd31)
R 3 (#4dc0c0)
U 12 (#18d661)
R 11 (#36e652)
U 10 (#4fe7a1)
R 5 (#2f6e32)
U 17 (#2fe1d1)
R 2 (#2cba62)
U 9 (#2930a1)
R 5 (#286d12)
U 7 (#3ee381)
R 12 (#0c4ce0)
U 4 (#286181)
L 17 (#259a80)
U 6 (#5e3323)
R 7 (#4185c0)
U 10 (#5e3321)
R 5 (#2a9270)
U 2 (#11e811)
R 12 (#0edfe0)
U 11 (#053c71)
R 11 (#2abf90)
U 7 (#5f6381)
R 7 (#307120)
U 3 (#17a761)
R 9 (#180940)
U 10 (#0baa11)
R 3 (#5fe2f0)
U 11 (#0baa13)
R 9 (#69f120)
U 5 (#14bc71)
R 7 (#2fe940)
U 16 (#184891)
L 7 (#3e76b0)
U 10 (#74c8b1)
L 13 (#11fe70)
U 9 (#3712e1)
R 6 (#114d30)
U 9 (#26b653)
R 11 (#05c152)
D 9 (#151243)
R 3 (#400370)
U 8 (#6d4e13)
R 17 (#400372)
D 6 (#0ae363)
L 4 (#05c150)
D 5 (#17a753)
R 7 (#10cfc2)
D 15 (#470433)
L 7 (#10cfc0)
D 6 (#37c983)
L 8 (#19e760)
D 6 (#0ab8e3)
R 12 (#5e9970)
D 5 (#1ee3f1)
R 6 (#2b3962)
U 11 (#3a45b1)
R 6 (#3da2a0)
U 6 (#6e96f1)
L 5 (#3da2a2)
U 8 (#2e7501)
R 11 (#2b3960)
U 10 (#657f61)
L 11 (#291930)
U 12 (#04b591)
R 5 (#0c7c20)
U 13 (#043ff3)
R 2 (#14c0b0)
U 11 (#65d263)
R 6 (#060310)
U 7 (#499ce1)
R 3 (#511ff0)
D 10 (#207571)
R 9 (#2e4e30)
D 5 (#33a333)
R 4 (#6ce740)
D 5 (#449c93)
R 3 (#4540d0)
U 9 (#244651)
R 3 (#36cb70)
U 3 (#53f971)
R 12 (#122200)
U 8 (#454131)
R 3 (#0c83f2)
D 7 (#0b87c1)
R 18 (#361a72)
D 7 (#589d41)
R 11 (#31dab2)
D 4 (#589d43)
R 5 (#432802)
D 7 (#0b87c3)
R 7 (#101df2)
D 18 (#32fb11)
R 5 (#597e62)
D 6 (#271ec1)
R 10 (#19d672)
D 3 (#5fe541)
R 12 (#358d42)
D 6 (#258221)
R 6 (#192fd2)
D 10 (#048fa3)
R 7 (#3b17e2)
D 9 (#44d6b3)
R 2 (#456350)
D 8 (#15ae53)
R 5 (#456352)
D 4 (#4d7183)
L 3 (#173ee2)
D 7 (#2754e1)
L 5 (#1df992)
D 13 (#09dc01)
L 7 (#1db1f2)
D 3 (#6660e1)
L 12 (#04b802)
D 2 (#00c7f1)
L 5 (#03d8e2)
D 8 (#1f7303)
L 9 (#05d1e2)
D 6 (#1ded03)
L 7 (#2743f2)
D 2 (#1eebc1)
L 4 (#3c3272)
D 10 (#1eebc3)
L 7 (#15c632)
D 13 (#1ded01)
R 7 (#12ea32)
D 4 (#1f7301)
L 6 (#2b9562)
D 6 (#2ffb01)
L 8 (#5bf420)
U 4 (#422961)
L 8 (#69be80)
U 9 (#0a0141)
L 5 (#006c40)
U 12 (#1da551)
L 2 (#1db1f0)
U 4 (#0769d1)
R 9 (#1be912)
U 4 (#5fe191)
R 6 (#2aa3c2)
U 16 (#2283a1)
L 6 (#0d5b30)
D 6 (#37efc1)
L 4 (#5d2960)
D 9 (#06b111)
L 12 (#72b960)
D 3 (#1bb7f1)
L 2 (#34e3f0)
D 12 (#4ff8b1)
L 10 (#2dbbc0)
D 3 (#46ec21)
L 7 (#248220)
U 11 (#19bc11)
R 11 (#338e40)
U 2 (#24d9e1)
R 3 (#0e7330)
U 10 (#514f71)
L 8 (#3e49e0)
U 6 (#32c963)
L 6 (#344102)
U 10 (#27f3e3)
L 14 (#344100)
D 11 (#2b8c83)
L 9 (#1ed1b0)
U 11 (#400a01)
L 5 (#4a5de0)
U 10 (#3b32b1)
L 5 (#4a5de2)
U 4 (#0b0d11)
L 11 (#3d3140)
U 5 (#508151)
L 5 (#47d872)
D 8 (#132e71)
L 12 (#07e2f2)
D 4 (#40a3b1)
L 4 (#5e24b2)
D 9 (#181e91)
R 16 (#5e24b0)
D 9 (#3042d1)
L 3 (#07e2f0)
D 11 (#638e01)
R 5 (#3de122)
D 8 (#0f9b41)
R 15 (#452fc2)
D 6 (#57e8b1)
R 7 (#2a4e22)
U 14 (#00d391)
R 5 (#435852)
D 10 (#1e6f91)
R 6 (#6a77d2)
D 7 (#217553)
L 6 (#0db942)
D 9 (#36a663)
L 7 (#541100)
D 11 (#547883)
R 6 (#46c250)
D 3 (#1ab863)
L 6 (#0040e0)
D 18 (#28b1d3)
R 6 (#197e32)
D 8 (#3739c3)
R 7 (#540ee2)
D 9 (#572ac3)
R 8 (#2d8722)
U 2 (#0825b3)
R 4 (#1a1be2)
U 13 (#1ef4f1)
R 3 (#35b942)
U 6 (#00ae13)
R 7 (#307ab0)
U 6 (#6d52e3)
R 5 (#307ab2)
U 11 (#1aec73)
R 6 (#1801e2)
D 9 (#09f4f1)
R 8 (#0b72b2)
D 4 (#156b11)
R 16 (#3ea4e2)
D 4 (#2b86f1)
R 8 (#3ea4e0)
D 10 (#3b22e1)
L 6 (#0b72b0)
D 9 (#02e391)
L 11 (#3b40c2)
D 4 (#4b0d21)
L 4 (#436750)
D 3 (#0a2871)
L 11 (#459490)
D 2 (#448131)
L 7 (#4e46d2)
D 6 (#1239c1)
L 2 (#18be72)
D 3 (#01e451)
L 2 (#63d532)
D 8 (#088331)
R 11 (#13fbd2)
D 2 (#76bde1)
R 9 (#010bf2)
D 7 (#093ed1)
R 11 (#34efc2)
D 9 (#346ad1)
R 15 (#5ea842)
D 8 (#3f1461)
R 8 (#075292)
D 5 (#43d301)
R 6 (#5c8642)
D 7 (#515c51)
R 6 (#35e392)
D 4 (#515c53)
L 11 (#3c52e2)
D 11 (#460471)
R 11 (#55f562)
D 4 (#275f23)
R 4 (#6901b2)
U 15 (#058f43)
R 5 (#4cad42)
U 8 (#5ad323)
R 6 (#4180a2)
U 3 (#408241)
R 14 (#3c0f62)
U 3 (#055fa1)
R 9 (#3f6652)
U 3 (#7414f1)
R 3 (#11ae90)
U 9 (#098c31)
L 13 (#4a7ad0)
U 6 (#5dfb41)
R 13 (#1f4c50)
U 8 (#165861)
R 3 (#2d68c2)
U 2 (#715cb1)
R 7 (#2b7e62)
D 6 (#241511)
R 9 (#4e1152)
D 8 (#26ec71)
R 5 (#247332)
D 14 (#051611)
L 9 (#09f002)
D 16 (#366e31)
L 3 (#0d6b12)
D 2 (#6dc513)
L 6 (#1eccb2)
D 7 (#6d5ce3)
R 8 (#4a81b2)
D 9 (#02b891)
L 8 (#282492)
D 5 (#02b893)
R 8 (#1c9a22)
D 13 (#5a47b3)
R 7 (#4287e2)
D 11 (#0aecb3)
R 3 (#285d50)
D 3 (#2fba33)
L 14 (#1115b0)
D 5 (#42d373)
L 5 (#610760)
U 11 (#42d371)
L 14 (#13cda0)
U 3 (#2e73f3)
L 11 (#424cf0)
U 9 (#0e40e3)
L 5 (#2ca0f2)
D 11 (#6284d3)
L 4 (#4f7e52)
D 12 (#00d2d3)
L 8 (#0d1642)
D 8 (#1f9c23)
L 6 (#6648b2)
D 9 (#0101c1)
L 9 (#2cbc52)
D 3 (#094dc1)
L 8 (#35d1a2)
D 2 (#66e3d1)
L 10 (#20ab92)
D 10 (#168e31)
L 8 (#710542)
U 12 (#1e5051)
L 8 (#248cc2)
U 3 (#3fbc61)
L 6 (#64dc10)
U 10 (#2b81c1)
L 11 (#69f840)
D 10 (#4eae41)
L 4 (#5a3aa0)
D 8 (#2bbb71)
L 13 (#574fc2)
D 3 (#1d2801)
L 3 (#1fa5d2)
D 12 (#04b8f1)
L 3 (#136922)
D 4 (#4ec981)
L 11 (#042042)
D 5 (#319921)
L 15 (#5bd8c2)
D 3 (#216d11)
L 3 (#110372)
U 7 (#530633)
L 2 (#2db3d2)
U 10 (#3f8131)
L 4 (#047412)
U 8 (#1f5091)
L 4 (#07efb2)
U 8 (#02d151)
L 4 (#0503b2)
U 4 (#517631)
L 12 (#11df72)
U 4 (#273981)
L 3 (#5a6a72)
D 4 (#1ac7a1)
L 8 (#0aa4c2)
D 4 (#1d29c3)
R 13 (#5f2750)
D 9 (#592b53)
L 13 (#5f2752)
D 8 (#1ff393)
L 7 (#2b1a32)
D 4 (#20d203)
L 18 (#2724e2)
D 4 (#486343)
R 19 (#2ea0e2)
D 2 (#486341)
R 14 (#33e032)
D 6 (#1fb073)
L 17 (#2a4422)
U 4 (#4b9413)
L 6 (#1563d0)
D 8 (#065ed1)
L 8 (#317df0)
U 8 (#02fac3)
L 12 (#2f35c0)
D 4 (#02fac1)
R 9 (#5d1770)
D 7 (#065ed3)
R 7 (#16fa70)
D 17 (#35b073)
R 7 (#0c5930)
D 5 (#400163)
L 9 (#2a1ab2)
D 11 (#3bc7a3)
L 14 (#269eb2)
D 9 (#1ef343)
L 10 (#269eb0)
U 4 (#2d4f23)
R 6 (#38f922)
U 9 (#5a3f31)
L 3 (#1269d2)
U 8 (#2dcad1)
L 7 (#2296c2)
U 9 (#3b97a3)
R 10 (#24c7b2)
U 3 (#67d443)
L 6 (#39a682)
U 8 (#1c8c93)
L 6 (#75d832)
U 3 (#11b393)
L 3 (#441282)
U 9 (#4c45b3)
L 11 (#385732)
U 11 (#1c1a93)
L 7 (#31b132)
U 8 (#25ae53)`

function flood(grid){
    let to_explore = [[0,0]]
    while(to_explore.length > 0){
        let [x, y] = to_explore.pop();
        if (x >= 0 && x < grid[0].length && y >= 0 && y < grid.length) {
            if (grid[y][x] != "#" &&  grid[y][x] != 'O') {
                grid[y][x] = 'O'
                to_explore.push(...[[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]])
            }
        }
    }
}

function contains(trench: number[][], x: number, y: number) {
    return trench.some(item => item[0] == x && item[1] == y);
}

function count_excavated(grid: string[][]): number {
    let count = 0;
    grid.forEach(innerArray => {
        innerArray.forEach(element => {
            if (element !== "O") {
                count++;
            }
        });
    });
    return count;
}

function part1(input) {
    let [x, y] = [0, 0];
    let min_x = 0, min_y = 0, max_x = 0, max_y = 0;
    let trench = [[0, 0]];
    input.split("\n").forEach(
        line => {
            let [direction, number, color] = line.split(" ")
            let dx = 0;
            let dy = 0;
            if (direction == "R") {
                dx = 1;
            }
            if (direction == "L") {
                dx = -1;
            }
            if (direction == "U") {
                dy = -1;
            }
            if (direction == "D") {
                dy = 1;
            }
            for (let i = 0; i < parseInt(number); i++) {
                x += dx;
                y += dy;
                if(x < min_x) min_x = x;
                if(x > max_x) max_x = x;
                if(y < min_y) min_y = y;
                if(y > max_y) max_y = y;
                trench.push([x, y]);
            }
        }
    )

    let grid = [];
    for(let y = min_y - 1; y <= max_y + 1; y++){
        let line = [];
        for(let x = min_x - 1; x <= max_x + 1; x++) {
            if(contains(trench, x, y)){
                line.push("#");
            }else{
                line.push(".");
            }
        }
        grid.push(line);
    }

    // console.log(grid.map(line => line.join("")).join("\n"))
    flood(grid);
    //console.log(grid.map(line => line.join("")).join("\n"))
    return count_excavated(grid);
}

function part2(input){
    let new_input = [];
    input.split("\n").forEach(
        line => {
            let [_1, _2, hex] = line.split(" ");
            let hex_length = hex.substring(2, 7);
            let hex_dir = hex.substring(7, 8);
            console.log(hex_length + " " + hex_dir);
            let direction = {
                "0" : "R",
                "1" : "D",
                "2" : "L",
                "3" : "U"
            }[hex_dir]
            new_input.push(direction + " " + parseInt(hex_length, 16) + " UNUSED")
        }
    )

    let [x, y] = [0, 0];
    let trench_contour = [[0, 0]];
    new_input.forEach(
        line => {
            let [direction, number, _] = line.split(" ")
            let dx = 0;
            let dy = 0;
            if (direction == "R") {
                dx = 1;
            }
            if (direction == "L") {
                dx = -1;
            }
            if (direction == "U") {
                dy = -1;
            }
            if (direction == "D") {
                dy = 1;
            }

            x += dx * number;
            y += dy * number;

            trench_contour.push([x, y]);
        }
    )

    console.log(trench_contour);

    return computeAreaOfPolygon(trench_contour) + calculateCircumference(trench_contour) / 2 + 1 ;

}

function calculateDistance(x1: number, y1: number, x2: number, y2: number): number {
    return Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
}

function calculateCircumference(vertices: number[][]): number {
    let circumference = 0;
    const numVertices = vertices.length;

    if (numVertices < 2) return 0; // Not enough vertices to form a polygon

    for (let i = 0; i < numVertices; i++) {
        const [x1, y1] = vertices[i];
        const [x2, y2] = vertices[(i + 1) % numVertices]; // wrap around to the first vertex
        circumference += calculateDistance(x1, y1, x2, y2);
    }

    return circumference;
}

function computeAreaOfPolygon(vertices) {
    let area = 0;
    const numVertices = vertices.length;

    if (numVertices < 3) return 0; // Not a polygon

    for (let i = 0; i < numVertices - 1; i++) {
        area += vertices[i][0] * vertices[i + 1][1];
        area -= vertices[i][1] * vertices[i + 1][0];
    }

    return Math.abs(area / 2);
}


console.log("Part1 example : " + part1(example));
console.log("Part1 my input : " + part1(my_input));

console.log("Part2 example : " + part2(example));
console.log("Part2 my input : " + part2(my_input));
