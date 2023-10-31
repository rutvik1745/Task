const express = require("express");
const path = require("path");
const app = express();
const port = 80;

// For servinf static files
app.use('/static', express.static('static'))

//  set the template engine as pug
app.set('view engine', 'pug')

// set the views directory
app.set('views', path.join(__dirname, 'views'))

// our Pug demo endpoint
app.get("/demo", (req, res) => {
    res.status(200).render('demo', { title: 'Hey harry', message: 'Hello there and thanks for telling me how touse pubg!' })
});

app.get("/",(req, res)=>{
    res.status(200).send("This is  homepage of my first express app with Rutvik");
})
app.get("/about",(req, res)=>{
    res.send("This is about my first express app with Rutvik");
})
app.post("/about",(req, res)=>{
    res.send("This is a post my first express app with Rutvik");
})
app.get("/this",(req, res)=>{
    res.status(404).send("This page is not found");
})


app.listen(port,()=>{
    console.log(`The application started successfuly on port ${port}`);
})