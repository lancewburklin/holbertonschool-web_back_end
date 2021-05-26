const Utils = require("./utils.js");
const sendPaymentRequestToApi = require("./5-payment.js");
const sinon = require('sinon');
const { expect } = require('chai');

describe("sendPaymentRequestToApi", function() {
  let testCase;

  beforeEach(function() {
    testCase = sinon.spy(console, 'log')
  });

  afterEach(() => {
    testCase.restore();
  });

  it('...', function() {
    sendPaymentRequestToApi(100, 20);
    expect(testCase.calledWith('The total is: 120')).to.be.true;
    expect(testCase.calledOnce).to.be.true;
  });
  it('...', function() {
    sendPaymentRequestToApi(10, 10);
    expect(testCase.calledWith('The total is: 20')).to.be.true;
    expect(testCase.calledOnce).to.be.true;
  });
});
