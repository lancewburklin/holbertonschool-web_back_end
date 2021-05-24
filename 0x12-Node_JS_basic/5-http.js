const http = require('http');
const countStudents = require('./3-read_file_async');

const app = (req, res) => {
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  }
  if (req.url === '/students') {
    res.write('This is the list of our students\n');
    countStudents(process.argv[2]).then((fin) => {
      res.end(fin);
    }).catch((error) => {
      res.end(String(error));
    });
  }
};

const server = http.createServer(app);
server.listen(1245);

module.exports = app;
