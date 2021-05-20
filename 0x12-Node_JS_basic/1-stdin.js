process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.on('readable', () => {
  const info = process.stdin.read();
  if (info) {
    process.stdout.write(`Your name is: ${info}`);
  }
}).on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
