"use strict";

// IF AND ELSE

// if (conditions){statments}

const ps = require("prompt-sync");

const prompt = ps();

let time = prompt("What is the time? ")

if (time >= 6 && time < 12){
    console.log("Good Morning")
}
else if (time === 12){
    console.log("Good Noon")
}

else console.log("Good after noon")


// SWITCH CASE

// switch (variables){case statements}


let nutrition = prompt("Type the nutrion type: ")
 
switch (nutrition){
    case 'omni':
        console.log("Human")
        break;
    case 'herbi':
        console.log("Sheep, Goat...")
        break;
    case 'carni':
        console.log("Lion, Tiger...") 
    default:
        console.log("Unknown!")
};


// FOR LOOP
// for (initiation; condition; increment){ statement}

for (let i = 0; i <= 5; i++) {
    console.log(i+1, 'Hey Mike')
}

for (let i = 1; i <=10; i++){
    if (i%2 === 0) console.log(i, "even")
    else console.log(i, "odd")
}


// While Loop

let i = 10;

while (i !== 0){
    if (i % 2 !== 0) console.log(i, "Odd")
    else console.log(i, "even")
    i --
}


// DO WHILE LOOP

let j = 1;

do {
    if (j % 2 !==0) console.log(j, "Is odd num");
    j++;
}while(j<10);


//FOR-IN LOOP  TO OBJECTS

let guy = {"name": "mike", "age": 26}


for (let i in guy) console.log(i, guy[i])

 let members = ["s1", "s2", "s3", "s4"]

 for (let i in members) console.log(members[i])


// FOR-OF LOOP

for (let mem of members) console.log(mem)



// BREAK AND CONTINUE

let k = 0;

while (true){
    
    if (k > 0) console.log("Positive num")
    k++  
    if(k > 5)break; 
}

// MAX OF 2 NUMS



// let n = max (5, 9)

// console.log(n)





















