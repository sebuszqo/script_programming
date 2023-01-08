import fetch from "node-fetch";

import express from "express";

import logger from "morgan";

const app1 = express();
const app2 = express();

app1.use(logger('dev'));
app2.use(logger('dev'));

app2.get('/', function (req, res) {
	res.send('Response from 3001');
});

app1.get('/', (req,res)=>{
    res.send(`
    <html>
      <head>
        <title>World Time</title>
      </head>
      <body>
        <form>
          <label for="area">Area:</label><br>
          <input type="text" id="area" name="area"><br>
          <label for="location">Location:</label><br>
          <input type="text" id="location" name="location"><br>
          <button type="button" onclick="getTime(this)">Get Time</button>Get Time</button>
        </form>
        <br>
        <h1>Remote</h1>
        <div id='remote'>Remote date and time</div>
        <h1>Local</h1>
        <div id='local'>Local date and time</div>
        <script>
          function getTime(form) {
            const area = document.getElementById('area').value;
            const location = document.getElementById('location').value;
            const remoteDiv = document.getElementById('remote');
            const localDiv = document.getElementById('local');
    
            remoteDiv.innerHTML = 'Downloading data';
            localDiv.innerHTML = new Date().toString();
    
            fetch('https://worldtimeapi.org/api/timezone/' + area + '/' + location)

                .then(response => {
        if (response.ok) {
            console.log(response)
            return response.json();
        } else {
            throw new Error('The server is overloaded');
        }
    })
        .then(data => {
            console.log("ss",data)
            const dateString = data.datetime;
            remoteDiv.innerHTML = dateString+" (CET)";
        })
        .catch(error => {
            
            remoteDiv.innerHTML = error.message;
        });
}
</script>
      </body>
    </html>`)
});

app1.listen(3000, function () {
    console.log('The application is available on port 3000');
});

app2.listen(3001, function () {
    console.log('The application is available on port 3001');
});
console.log("To stop the server, press 'CTRL + C'");


