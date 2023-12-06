let example = `Time:      7  15   30
Distance:  9  40  200`

let my_input=`Time:        53     71     78     80
Distance:   275   1181   1215   1524`

function parse_input(input){
    return input.split("\n").map(s => s.split(":")[1].trim().replace(/\s+/g, " ").split(" ").map(v => parseInt(v)))
}


function part1(input){
    let winsProduct = 1;
    let [times, distances] = parse_input(input);
    for(let i=0; i < times.length; i++){
        let nbWins = 0;
        let time = times[i];
        let distance = distances[i];
        for(let x = 0; x < time; x++){
            let racedDistance = (x*(time-x));
            if(racedDistance > distance){
                nbWins ++;
            }
        }
        winsProduct *= nbWins;
    }
    return winsProduct;
}

console.log("Ways to win part1 example " + part1(example))
console.log("Ways to win part1 my input " + part1(my_input))

// Time:        53717880
// Distance:   275118112151524
// Solve : -x²+53717880x-275118112151524
// We get 2 roots :
// 5733492.1758218 -> 5733493
// 47984387.824178 -> 47984387
// Just compute the number of "races" between those two numbers
let delta = (47984387 - 5733493) + 1
console.log("Ways to win part2 my input" + delta)
