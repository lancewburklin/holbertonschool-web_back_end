const http = require('http');

const app = (req, res) => {
  res.writeHead(200);
  res.end('Hello Holberton School!');
};

const server = http.createServer(app);
server.listen(1245);

module.exports = app;
