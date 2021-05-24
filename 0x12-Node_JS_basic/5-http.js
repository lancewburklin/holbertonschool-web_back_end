const http = require('http');
const countStudents = require('./3-read_file_async');

const app = (req, res) => {
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  }
  if (req.url === '/students') {
    res.end('This is the list of our students');
    countStudents(process.argv[2]).then().catch((error) => { res.send(error); });
  }
};

const server = http.createServer(app);
server.listen(1245);

module.exports = app;
