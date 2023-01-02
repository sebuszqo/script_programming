// Application using the 'Pug' template system
const express = require('express'),
    logger = require('morgan');
const {readFile} = require('fs').promises;
const app = express();
let x = 1;
let y = 2;

// *** Functions definitions ***

const sum = (x,y) => x + y;


const results = (res, o, x, y) =>{
    switch (o) {
        case "+":
            return x + y;
            break
        case "-":
            return x - y;
            break
        case "*":
            return  x * y;
            break
        case "/":
            return x / y;
            break;
        default:
            res.send("There is no valid operation");
            res.end();
            break;
    }
}

// Configuring the application
app.set('views', __dirname + '/views');               // Files with views can be found in the 'views' directory
app.set('view engine', 'pug');                        // Use the 'Pug' template system
app.locals.pretty = app.get('env') === 'development'; // The resulting HTML code will be indented in the development environment

// Determining the contents of the middleware stack
app.use(logger('dev'));                            // Add an HTTP request recorder to the stack — every request will be logged in the console in the 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// *** Route definitions ***

// The first route
app.get('/', (req, res) => {
    // res.render('index', {sum: `${x} + ${y} = ${sum(x,y)}`})
    res.render('sum', {sum: `${x} + ${y} = ${sum(x,y)}`}); // Render the 'index' view
});

app.get('/json/:name', async(req,res)=>{

    const fileName = req.params.name
    try {
        const file = await readFile(`./data/${fileName}.json`, "utf-8")
        const data = JSON.parse(file)
        data.forEach(element =>
            element.result = results(res, element.o, element.x, element.y)
        )
        // res.render('index', {table: data})
        res.render('operations',{table: data})
    }
    catch (err){
        res.send(`Error occurred during reading a file: ${fileName}`)
    }
}
);
// The application is to listen on http://localhost:3000
app.listen(3000, function () {
    console.log('The application is available on http://localhost:3000');
});