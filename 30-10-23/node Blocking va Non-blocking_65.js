// Synchronous or blocking
// - line by line execution

// Asyncronous or non-blocking
// -line by line execution not guaranteed
// - callbacks will fire

const fs = require("fs");
fs.readFile("del.text","utf-8" , (err,data)=>{
    console.log(err,data);
});
console.log("This is a message")
