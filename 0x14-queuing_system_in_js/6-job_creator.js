const kue = require('kue');
const queue = kue.createQueue();

const ObjJob = {
  phoneNumber: "555-555-5555",
  message: "Pineapples",
}

const Job = queue.create('push_notification_code', ObjJob).save();

Job.on('enqueue', function() {
  console.log(`Notification job created: ${Job.id}`);
});

Job.on('complete', function() {
  console.log('Notification job completed');
});

Job.on('failed', function() {
  console.log('Notification job failed');
});
