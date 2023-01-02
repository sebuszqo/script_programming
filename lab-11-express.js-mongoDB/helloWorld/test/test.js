//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
const supertest = require("supertest");
var chai = require('chai');
var expect = chai.expect;
const fs = require('fs');
const path = require("path");
chai.use(require('chai-json'))
const server = supertest.agent("http://localhost:3000");
chai.should()



// UNIT test begin
describe('GET /', function() {
    it('respond with html', function(done) {
        server
            .get('/')
            .expect('Content-Type', /html/)
            .expect(200, done);
    });
});

describe('GET /', function (){
    it("My first Test", function (done){
        server
            .get('/')
            .expect('Content-Type', /html/)
            .expect(200,done)
    })
})

describe("Checking GET /json/example", function (){
    it('Response',function (done){
        server.get('/json/example').expect('Content-Type',/html/).expect(200,done)
    });

    it('Check /json/example route content',function (done){
        server
            .get('/json/example')
            .expect('Content-Type', /html/)
            .expect(async (res)=>{
                chai.expect(res.text, `<table>
    <thead>
    <tr>
        <th> x </th>
        <th> Operation </th>
        <th> y </th>
        <th> Result </th>
    </tr>
    </thead>
    <tbody>
     <tr><td> 4 </td><td> + </td><td> 6 </td><td> 10 </td></tr><tr><td> 11 </td><td> - </td><td> 24 </td><td> -13 </td></tr><tr><td> 15 </td><td> * </td><td> 3 </td><td> 45 </td></tr><tr><td> 21 </td><td> / </td><td> 7 </td><td> 3 </td></tr><tr><td> 21 </td><td> + </td><td> 7 </td><td> 28 </td></tr>
    </tbody>
    </table>
`)}).end(done)
    });
});


describe('Check returning sum /', function (){
    it("Check / route content", function (done){
        server
            .get('/')
            .expect('Content-Type', /html/)
            .expect(async (res)=>{
                chai.expect(res.text, '<h1>Summing numbers that were hardcoded inside!</h1><p>1 + 2 = 3</p>')
            }).end(done);
    });
});

describe('Checking JSON files',function (){
    it("Propper JSON", function (done){
        const filePath = path.join(__dirname, 'data', 'example.json');
        chai.expect(".\\data\\example.json").to.be.jsonFile();
        done()

    })
})



// npm run test - uruchomienie testu
//