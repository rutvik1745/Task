const express = require("express");
const { request } = require("http");
const path = require("path");
const fs = require("fs");
const app = express();
const port = 80;

// Ecpress Specific Stuff
app.use('/static', express.static('static'))
app.use(express.urlencoded())

//Pub specific Stuff
app.set('view engine', 'pug')// set the views directory
app.set('views', path.join(__dirname, 'views'))// our Pug demo endpoint

//EndPoint
app.get('/' , (req,res)=>{
    const con = "This is the best content on the internet"
    const params = {'title': 'pubg is the best game', "content":con}
    res.status(200).render('index.pug', params)
})
app.post('/',(req,res)=>{
    name = req.body.name
    age = req.body.age
    gender = req.body.gender
    address = req.body.address
    more = req.body.more
    let outputToWrite = `the name of the client is ${name},${age} years old , ${gender}, residing at ${address}. More about  him/her : ${more}`
    fs.writeFileSync("output.text",outputToWrite)
    // console.log(req.body)
    const params = {'message': 'Your form has been submitted successfully'}
    res.status(200).render('index.pug', params)

})


// Start The Server
app.listen(port,()=>{
    console.log(`The application started successfuly on port ${port}`);
})