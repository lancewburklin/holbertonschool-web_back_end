const Utils = require("./utils.js");
const sendPaymentRequestToApi = require("./4-payment.js");
const sinon = require('sinon');
const { expect } = require('chai');

describe("sendPaymentRequestToApi", function() {
  it('...', function() {
    const testCase = sinon.spy(console, 'log');
    const testStub = sinon.stub(Utils, 'calculateNumber')
    testStub.returns(10);
    sendPaymentRequestToApi(100, 20);
    expect(testStub.calledWith('SUM', 100, 20)).to.be.true;
    expect(testStub.alwaysReturned(10)).to.be.true;
    expect(testCase.calledWith('The total is: 10')).to.be.true;
    testCase.restore();
    testStub.restore();
  });
});
