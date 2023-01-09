import * as express from "express";
import {static as expressStatic, urlencoded} from "express";
import 'express-async-errors';
import * as methodOverride from "method-override";
import {engine} from "express-handlebars";

/**
 * Import to create a connection pool to database when we are starting an app
 */
import "./utils/db";
import { clientRouter } from "./routers/client";
import {dealerRouter} from "./routers/dealer";
import {UserRecord} from "./records/client_db";
import {CarRecord} from "./records/car_db";

// creating an express app
const app = express();

// methodOverride to use with PATCH PUT etc.
app.use(methodOverride('_method'));

// I will use it cuz we will get our data through forms
app.use(urlencoded({
    extended: true,
}));

// I will be serving static data from dir named 'public'
// app.use(expressStatic("__dir"))
app.use(expressStatic("public"));

// layouts engine - I will use express handlebars
app.engine('.hbs', engine({
    extname: '.hbs',
    //helpers: ???,
}));

// setting my view engine to .hbs
app.set('view engine', '.hbs')

// using clientRouter
app.use('/client', clientRouter);
// using dealerRouter
app.use('/dealer', dealerRouter)
//
// app.get('/',async (req, res) => {
//     const user = new UserRecord({id: '212',name:'michal',car:'123'})
//     const rec = await user.insert()
//
//     const car = new CarRecord({num: 10, brand: "e46", model: "bmw", year: 1000, id:"112"})
//     await car.insert()
//     res.send('ok')
// })



//handling errors
// app.use(handleError)


// app is listening on port 3000 - console log to click every time when I need it - I do not have to copy it ;)
app.listen(3000, 'localhost', () => {
    console.log("Listening on http://localhost:3000");
});



