console.log("working")
$(".po").click(function () {
    var fn = document.getElementById("firstName").value;
    var ln = document.getElementById("lastName").value;
    var e = document.getElementById("Bemail").value;
    var p = document.getElementById("phone").value;
    var q = document.getElementById("quantity").value;
    var a = document.getElementById("address").value;
    var d = document.getElementById("district").value;
    var z = document.getElementById("zipcode").value;
    if (fn == "" && ln == "" && e == "" && p == "" && q == "" && a == "" && d == "" && z == "") {
        alert("fill up the form");
    }
    else {
        alert("successfully placed the order, We will contact you");
    }
});