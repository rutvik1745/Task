const express = require("express");
const path = require("path");
const app = express();
const port = 5000;

// Express Specific Stuff
app.use('/static',express.static('static'))// for serving static files
app.use(express.urlencoded())

// pug specific stuff
app.set('view engine','pug') // set the template engine as pug
app.set('views',path.join(__dirname,'views'))// set the views directory

// Endpoints
app.get('/',(req,res)=>{
    const params = { }
    res.status(200).render('home.pug',params);
})                                    
app.get('/contact',(req,res)=>{
    const params = { }
    res.status(200).render('contact.pug',params);
})                                    
                         
// Start The Server
app.listen(port,()=>{
    console.log(`The application started successfuly on port ${port}`);
})
