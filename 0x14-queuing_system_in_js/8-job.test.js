import kue from 'kue';

import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

before(function() {
  queue.testMode.enter();
});

afterEach(function() {
  queue.testMode.clear();
});

after(function() {
  queue.testMode.exit()
});

describe('createPushNotificationsJobs', () => {
  let jobs = [
    {
      phoneNumber: '12345',
      message: 'Cheese'
    }
  ];
  it('createPushNotificationsJobs', function() {
    createPushNotificationsJobs(jobs, queue);
    console.log(queue.testMode.jobs);
  });
});
