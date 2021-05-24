const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, stuff) => {
      if (err) {
        return reject(new Error('Cannot load the database'));
      }
      const content = stuff.split('\n');
      let i = 0;
      const fields = {};
      const allNames = {};
      let total = 0;
      for (i = 0; i < content.length; i += 1) {
        content[i] = content[i].split(',');
        if (content[i].length !== 1 && i !== 0) {
          total += 1;
          if ((content[i][3] in fields) === false) {
            fields[String(content[i][3])] = 1;
            [allNames[String(content[i][3])]] = content[i];
          } else {
            fields[String(content[i][3])] += 1;
            allNames[String(content[i][3])] = `${allNames[String(content[i][3])]}, `;
            allNames[String(content[i][3])] = allNames[String(content[i][3])] + content[i][0];
          }
        }
      }
      console.log(`Number of students: ${total}`);
      for (const key in fields) {
        if (allNames[key]) {
          const fTotal = fields[key];
          console.log(`Number of students in ${key}: ${fTotal}. List: ${allNames[key]}`);
        }
      }
      return resolve('Yay');
    });
  });
}

module.exports = countStudents;
