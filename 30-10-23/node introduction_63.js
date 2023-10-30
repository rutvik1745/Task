// a = 50;
// console.log(a);


const http = require('http');
const hostname = '127.0.0.1';
const port = 8000;
const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html');
//   res.end('Hello World');
  res.end(`<!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>iframes</title>
  </head>
  <body>
      <h2>HTML iframes example</h2>
      <p>Use the height and width attributes to specify the size of the iframe:</p>
      <iframe src="https://www.javatpoint.com/" frameborder="0" height="50%" width="70%"></iframe>
      <iframe height="300" width="100%" name="iframe_a"></iframe>
      <p><a href="https://www.javatpoint.com" target="iframe_a">javatpoint.com</a></p>
  </body>
  </html>`);

});
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});