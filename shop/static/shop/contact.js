$(".btn").click(function () {
    var n = document.getElementById("name").value;
    var e = document.getElementById("email").value;
    var p = document.getElementById("problem").value;
    if (n == "" && e == "" && p == "") {
        alert("fill up the form");
    }
    else {
        alert("successfully submited, Thanks for contacting with us.");
    }
});