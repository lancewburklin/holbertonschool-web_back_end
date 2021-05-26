const assert = require('assert');
const calculateNumber = require("./0-calcul.js");
let res = calculateNumber(0, 3);
describe('calculateNumber', function() {
    it('...', function(){
      assert.equal(res, 3);
    });
    it('...', function(){
      res = calculateNumber(.3, 5)
      assert.equal(res, 5);
    });
    it('...', function(){
      res = calculateNumber(2, .5)
      assert.equal(res, 3);
    });
    it('...', function(){
      res = calculateNumber(.5, .5)
      assert.equal(res, 2);
    });
    it('...', function(){
      res = calculateNumber(2, .1)
      assert.equal(res, 2);
    });
});
