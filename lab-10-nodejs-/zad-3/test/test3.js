//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
let supertest = require("supertest");

// This agent refers to PORT where program is runninng.
let server = supertest.agent("http://localhost:8000");

// UNIT test begin
describe('GET /submit?name=John', function () {
    it('Brak takiego pliku', function (done) {
        server
            .get('/submit?name=John')
            .expect('Content-Type', /text\/plain/)
            .expect(200, "Nie udało mi się znaleźć tego pliku/katalogu, chyba nie istnieje :o.", done);
    });
});

describe('GET /submit?name=/etc', function (){
    it('To jest katalog', function (done){
        server
            .get('/submit?name=/etc')
            .expect('Content-Type', /text\/plain/)
            .expect(200, "To jest katalog.", done);
    });
});

describe('GET /submit?name=plik.txt', function (){
    it('To jest plik', function (done){
        server
            .get('/submit?name=plik.txt')
            .expect('Content-Type', /text\/plain/)
            .expect(200,    'To jest nazwa pliku. A oto zawartość pliku:\n' +
                `Zawartość tego pliku jest bardzo prosta: Programowanie Skryptowe jest super`, done);
    });
});

// //Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
// let supertest = require("supertest");
//
// // This agent refers to PORT where program is runninng.
// let server = supertest.agent("http://localhost:8000");
//
// // UNIT test begin
// describe('GET /submit?name=John', function () {
//     it('respond with "Hello John"', function (done) {
//         server
//             .get('/submit?name=John')
//             .expect('Content-Type', /text\/plain/)
//             .expect(200, "Hello John", done);
//     });
// });

