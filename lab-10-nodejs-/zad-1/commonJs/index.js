const things = require('./module.js');

// gives me 2 lat parameters
let args = process.argv.slice(-2)


// console.log(args)

let op = new things.Operation(args[0], args[1]);

// node index "43" 3
console.log(op.sum())

// Call: node index.js 112 1008