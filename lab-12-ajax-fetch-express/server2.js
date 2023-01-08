const express = require('express');
const logger = require('morgan');
/************* */
const app1 = express();
const app2 = express();
/************* */
app1.use(logger('dev'));
app2.use(logger('dev'));
/************* */
app1.listen(3000, function () {
    console.log('The application is available on port 3000');
});
app2.listen(3001, function () {
    console.log('The application is available on port 3001');
});
/************* */
app1.get('/', function (req, res) {
    res.send('Response from 3000');
});

app2.get('/', function (req, res) {
    res.send('Response from 3001');
});
/************* */
console.log("To stop the server, press 'CTRL + C'");