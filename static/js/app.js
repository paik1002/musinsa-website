
let cart =
JSON.parse(localStorage.getItem("cart"))
|| [];




function addCart(name,price){


cart.push({

name:name,

price:price

});


localStorage.setItem(
"cart",
JSON.stringify(cart)
);



renderCart();


}





function renderCart(){


const list =
document.getElementById("cart-list");


list.innerHTML="";


cart.forEach(item=>{


let li=document.createElement("li");


li.innerHTML=

`${item.name}
-
${item.price.toLocaleString()}원`;


list.appendChild(li);


});



document.getElementById("cart-count")
.innerHTML =
"Cart "
+
cart.length;



}




renderCart();
