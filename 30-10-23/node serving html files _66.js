//Serving html File using NodeJs 
// const http = require('http');
// const hostname = '127.0.0.1';
// const port = 8000;
// const server = http.createServer((req, res) => {
//   res.statusCode = 200;
//   res.setHeader('Content-Type', 'text/plain');
//   res.end('Hello World');
// });
// server.listen(port, hostname, () => {
//   console.log(`Server running at http://${hostname}:${port}/`);
// });

const http = require('http')
const fs = require("fs")
const fileContent = fs.readFileSync('Box and text shadow_34.html')

const server = http.createServer((req,res)=>{
    res.writeHead(200, {'Content-type':'text/html'});
    res.end(fileContent)
})
server.listen(80,'127.0.0.1',()=>{
    console.log("Listening on port 80")
})