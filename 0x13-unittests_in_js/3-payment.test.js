const Utils = require("./utils.js");
const sendPaymentRequestToApi = require("./3-payment.js");
const sinon = require('sinon');
const { expect } = require('chai');

describe("sendPaymentRequestToApi", function() {
  it('...', function() {
    const testCase = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);
    expect(testCase.calledWith('SUM', 100, 20)).to.be.true;
    testCase.restore();
  });
});
