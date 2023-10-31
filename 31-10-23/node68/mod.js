console.log("this is Module");

function average(arr){
    let sum = 0;
    arr.forEach(x => {
        let sum = 0;
        sum += x;
    });
    return sum/arr.length;
}

module.exports = {
    avg : average,
    name: "Harry",
    repo : "gitHub"
};
