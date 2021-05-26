const assert = require('assert');
const calculateNumber = require("./1-calcul.js");
let res = calculateNumber('SUM', 0, 1);
describe('SUM', function() {
  it('...', function() {
    assert.equal(res, 1);
  })
})
