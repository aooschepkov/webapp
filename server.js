const express = require('express');
const path = require('path');
const app = express();
const port = 8383;

var publicPath = path.join(__dirname, 'public');

app.use(express.static(publicPath));

app.get('/', function(req, res){
    res.sendFile(publicPath + '/html/home.html')
})

// app.get('/workoutcalendar', function(req, res){
//     res.sendFile(publicPath + '/html/workoutcalendar.html')
// })

app.listen(port, () => console.log(`Server has started on port: ${port}`));