const fs = require("fs");
let text = fs.readFileSync("del.text","utf-8")
text = text.replace("browser", "Rohan")

console.log("The content of the file is")
console.log(text);

console.log("Creating a new file ..")
fs.writeFileSync("Rohan.text",text);
