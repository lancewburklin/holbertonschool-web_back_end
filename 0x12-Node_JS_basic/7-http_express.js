const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.end('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.write('This is the list of our students\n');
  countStudents(process.argv[2]).then((fin) => {
    res.end(fin);
  }).catch((error) => {
    res.end(error.message);
  });
});

app.listen(1245);

module.exports = app;
