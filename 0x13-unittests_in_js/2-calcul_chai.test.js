const chai = require('chai');
const expect = chai.expect;
const calculateNumber = require("./1-calcul.js");
let res = calculateNumber('SUM', 0, 1);
describe('SUM', function() {
  it('...', function() {
    expect(res).to.equal(1);
  });
});
describe('SUBTRACT', function() {
  it('...', function() {
    res = calculateNumber('SUBTRACT', 3, 2);
    expect(res).to.equal(1);
  });
});
describe('DIVIDE', function() {
  it('...', function() {
    res = calculateNumber('DIVIDE', 4, 2);
    expect(res).to.equal(2);
  });
  it('...', function() {
    res = calculateNumber('DIVIDE', 4, 0);
    expect(res).to.equal('Error');
  });
});
