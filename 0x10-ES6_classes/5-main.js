import Building from './5-building.js';

const b = new Building(100);
console.log(b);

class TestBuilding extends Building {}
class TestBuilding2 extends Building {}

try {
    new TestBuilding(200)
}
catch(err) {
    console.log(err);
}

try {
    new TestBuilding2(200)
}
catch(err) {
    console.log(err);
}
