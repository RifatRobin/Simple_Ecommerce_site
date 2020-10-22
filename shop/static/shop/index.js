console.log('statrted working');
$(".card-text").hide();
$(".details").click(function () {
    $(".card-text").show(2000);
});


if (localStorage.getItem('cart') == null) {
    var cart = {};
}
else {
    cart = JSON.parse(localStorage.getItem('cart'));
    document.getElementById('crt').innerHTML = Object.keys(cart).length;
}

$('.cart').click(function () {
    var prd_id = this.id.toString();
    //console.log("you clicked on " + prd_id);
    if (cart[prd_id] == null) {
        cart[prd_id] = 1;
    }
    else {
        cart[prd_id] = cart[prd_id] + 1;
    }//this will allow to see how many cart you clicked & it will endup with session reload
    console.log(cart);

    //now lets update the cart as it clicked
    localStorage.setItem("cart", JSON.stringify(cart));
});

