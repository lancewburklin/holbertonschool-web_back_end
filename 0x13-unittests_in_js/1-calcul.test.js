const assert = require('assert');
const calculateNumber = require("./1-calcul.js");
let res = calculateNumber('SUM', 0, 1);
describe('SUM', function() {
  it('...', function() {
    assert.equal(res, 1);
  });
});
describe('SUBTRACT', function() {
  it('...', function() {
    res = calculateNumber('SUBTRACT', 3, 2);
    assert.equal(res, 1);
  });
});
describe('DIVIDE', function() {
  it('...', function() {
    res = calculateNumber('DIVIDE', 4, 2);
    assert.equal(res, 2);
  });
  it('...', function() {
    res = calculateNumber('DIVIDE', 4, 0);
    assert.equal(res, 'Error');
  });
});
