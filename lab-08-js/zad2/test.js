// "use strict";
// let expect = chai.expect;
//
// function sum(x,y) {
//     return x+y;
// }
//
// describe('The sum() function', function() {
//     it('Returns 4 for 2+2', function() {
//         expect(sum(2,2)).to.equal(4);
//     });
//     it('Returns 0 for -2+2', function() {
//         expect(sum(-2,2)).to.equal(0);
//     });
//     it('Returns 6 for 2+2', function() {
//         expect(sum(3,3)).to.equal(6);
//     });
// });

let arrToSum = []
let sum = 0

const addDigits = (string) => {
    let arr = string.split("")
    return arr.filter(char => Boolean(Number(char))).reduce((prev, curr)=> Number(prev) + Number(curr), 0)
}

const countLetters = (string) =>{
    let arr = string.split("");
    return arr.filter(char => !Boolean(Number(char))).length
    // arr = arr.filter(char => !Boolean(Number(char)))
}

const addAllNumbers = (string) =>{
    let arr = string.split("");
    return (Number(arr[0]) ? sum += Number(arr.filter(char => Boolean(Number(char))).join("")) : sum )
    // if (Number(arr[0])){
    //     arr = arr.filter(char => Boolean(Number(char)))
    //     return sum += Number(arr.join(""))
    // }
    // return sum

}

console.log(addAllNumbers('111'))
console.log(addAllNumbers('11aa'))
console.log(addAllNumbers('b3345b'))

// console.log(addDigits('111'))
// console.log(countLetters('aAA2s2'))