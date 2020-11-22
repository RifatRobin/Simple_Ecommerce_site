$(".card-text").hide();

$(".qv").click(function () {
    $(".card-text").show(2000);
});

$("#searchbtn").click(function () {
    var btnValue = document.getElementById("queryset").value;
    if (btnValue == "") {
        alert("Enter something to search");
    }
});


