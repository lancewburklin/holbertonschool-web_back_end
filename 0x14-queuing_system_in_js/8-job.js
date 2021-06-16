const kue = require('kue');

export default function createPushNotificationsJobs(jobs, queue) {
  if (Array.isArray(jobs) === false) {
    return (new Error('Jobs is not an array'));
  }
  let i;
  for (i = 0; i < jobs.length; i++) {
    const Job = queue.create('push_notification_code_3', jobs[i]).save((err) => {
      console.log(err);
    });

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
}
