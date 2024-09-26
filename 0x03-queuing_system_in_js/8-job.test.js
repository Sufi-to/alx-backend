import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 5678 to verify your account',
  },
];

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('display a error message if jobs is not an array passing Number', () => {
    expect(() => {
      createPushNotificationsJobs(2, queue);
    }).to.throw('Jobs is not an array');
  });

  it('display a error message if jobs is not an array passing Object', () => {
    expect(() => {
      createPushNotificationsJobs({}, queue);
    }).to.throw('Jobs is not an array');
  });

  it('display a error message if jobs is not an array passing String', () => {
    expect(() => {
      createPushNotificationsJobs('Hello', queue);
    }).to.throw('Jobs is not an array');
  });

  it('should NOT display a error message if jobs is an array with empty array', () => {
    const ret = createPushNotificationsJobs([], queue);
    expect(ret).to.equal(undefined);
  });

  it('should create two new jobs to the queue', (done) => {
    createPushNotificationsJobs(jobs, queue);

    setTimeout(() => {
      expect(queue.testMode.jobs.length).to.equal(2);
      expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
      expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
      expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
      expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
      done();
    }, 100);
  });
});