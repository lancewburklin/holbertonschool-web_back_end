const { assert } = require("chai");
const getPaymentTokenFromAPI = require("./6-payment_token.js");

describe('getPaymentTokenFromAPI', function() {
  it('...', function(done) {
    getPaymentTokenFromAPI(true).then(res => {
      assert.equal(res, {data: 'Successful response from the API' });
    }).catch(err => {
      assert.equal(typeof res, 'undefined');
    });
    done();
  });
});
