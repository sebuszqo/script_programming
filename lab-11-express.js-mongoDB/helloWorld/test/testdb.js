const supertest = require("supertest");
const chai = require('chai');
const chaiJson = require('chai-json');
chai.use(chaiJson);
const server = supertest.agent("http://localhost:3000");
const chaiHttp = require('chai-http');
chai.use(chaiHttp)
const expect = chai.expect

describe("GET /calculate/:operation/:x/:y",()=>{
    it("Should return the correct result for the given operation", (done)=>{
        server
            .get("/calculate/+/3/4")
            .expect(200)
            .end((err,res)=>{
                if (err) return done(err);
                expect(res.text,"3 + 4 = 7")
                done()
            });
    });
    it("should return an error message for invalid operation",(done)=>{
        server
            .get("/calculate/invalid/3/4")
            .expect(500)
            .end((err,res)=>{
                if (err) return done(err);
                expect(res.text, "Invalid operation");
                done()
            });
    });
});