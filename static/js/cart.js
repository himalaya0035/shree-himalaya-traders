var updateBtns = document.getElementsByClassName('update-cart')
var updateBtns2 = document.getElementsByClassName('update-cart2')
for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product /* to access our custom defined data attribute */
        var action = this.dataset.action
        console.log(productId, action)
        var windowLoc = $(location).attr('pathname'); // for getting the path name
        switch(windowLoc){
            case  "/products/":
                price = getPrice(productId)  //this is in the form of string
                break
            case "/cart/" :
                var iditem = this.dataset.item
                console.log(iditem)
                var ele = document.getElementsByClassName(iditem)[0].innerHTML.replace("Rs","")
                console.log(ele)
                price = ele  // this is in the form of a number
                break
        }
        console.log(price) 
        console.log('User:', user)
        
        if (user == 'AnonymousUser') {
           // console.log('add cookie fn checkpoint')
            //addCookieItem(productId, action)
             console.log('user is unauthenticated')
        } else {
            console.log('user is logged in')
            switch(windowLoc){
                case "/products/":
                    console.log('products page')
                    updateUserOrder(productId, action,price)
                    break
                case "/cart/":
                    console.log("cart page")
                    updateUserOrderTwo(productId, action,price)
                    break
            }
        }
    })
}

function getPrice(productId){
    var radio = document.getElementsByName(productId)
    for (var i= 0; i<radio.length; i++){
        if (radio[i].checked){
            return radio[i].value
        }
    }
}

function updateUserOrder(productId, action,price) {
    console.log('user is authenticated')
    // with this fn we will send data back to the backend, where we will process it
    var url = '/update_item/'

    fetch(url, { // the url we want to send data to
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'product-id': productId,
                'action': action,
                'price':price
            }) // the actual data that we need to send
        })
        // fetch is used to fetch information across webpages
        .then((response) => {
            return response.json()
        })
        // response fetched from that url
        .then((data) => {
            console.log('data:', data)
        })
    // printing the response recieved
}

function updateUserOrderTwo(productId, action,price) {
    console.log('user is authenticated')
    // with this fn we will send data back to the backend, where we will process it
    var url = '/update_item/'

    fetch(url, { // the url we want to send data to
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'product-id': productId,
                'action': action,
                'price':price
            }) // the actual data that we need to send
        })
        // fetch is used to fetch information across webpages
        .then((response) => {
            return response.json()
        })
        // response fetched from that url
        .then((data) => {
            console.log('data:', data)
            location.reload()
        })
     // printing the response recieved
}
/* for store search box */

var searchBox = document.getElementById('id_name');
searchBox.placeholder = "Search Products..";
searchBox.ariaLabel = "search products here"

