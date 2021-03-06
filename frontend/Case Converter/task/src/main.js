function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
}


let areaText = document.getElementById("area");
let element1 = document.getElementById("upper-case");
element1.addEventListener("click", function () {
    areaText.value = areaText.value.toUpperCase();
})

let element2 = document.getElementById("lower-case");

element2.addEventListener("click", function () {
    areaText.value = areaText.value.toLowerCase();
})

let element3 = document.getElementById("proper-case")
element3.addEventListener("click", function () {
    let arr = areaText.value.split(" ");
    let arr_upper = arr.map(x => capitalizeFirstLetter(x));
    areaText.value = arr_upper.join(" ");
})

let element4 = document.getElementById("sentence-case")
element4.addEventListener("click", function () {
    let arr = areaText.value.split(". ");
    let arr_upper = arr.map(x => capitalizeFirstLetter(x));
    areaText.value = arr_upper.join(". ");
})

let element5 = document.getElementById("save-text-file");
element5.addEventListener("click", function () {
    let a = document.createElement("a");
    a.href = window.URL.createObjectURL(new Blob([areaText.value], {type: "text/plain;charset=utf-8"}));
    a.download = "text.txt";
    a.click();
})



// var a = document.getElementById("a");
// var file = new Blob([text], {type: type});
// a.href = URL.createObjectURL(file);
// a.download = name;