const friend1 = {
    name: "robo",
    age: 25,
    city: "tbilisi",
    hobby: "dance",
    profession: "pupil"
};

const friend2 = {
    name: "nika",
    age: 25,
    city: "tbilisi",
    hobby: "dance",
    profession: "pupil"
};

const friend3 = {
    name: "roma",
    age: 25,
    city: "tbilisi",
    hobby: "dance",
    profession: "pupil"
};

console.log("Friend 1:", friend1);
console.log("Friend 2:", friend2);
console.log("Friend 3:", friend3);

console.log("Friend 1's original age:", friend1.age);
friend1.age = 30; 
console.log("Friend 1's new age:", friend1.age);

