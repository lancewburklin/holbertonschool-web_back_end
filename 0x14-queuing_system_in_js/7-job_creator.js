const kue = require('kue');

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

const queue = kue.createQueue();

let i;
for (i = 0; i < jobs.length; i++) {
  const Job = queue.create('push_notification_code_2', jobs[i]).save();

  Job.on('enqueue', function() {
    console.log(`Notification job created: ${Job.id}`);
  });
  
  Job.on('complete', function() {
    console.log(`Notification job ${Job.id} completed`);
  });
  
  Job.on('failed', function(error) {
    console.log(`Notification job ${Job.id} failed: ${error}`);
  });

  Job.on('progress', function(progress) {
    console.log(`Notification job ${Job.id} ${progress}% complete`);
  });
}
