var updateBtns2 = document.getElementsByClassName('update-wishlist-js')

for (i = 0; i < updateBtns2.length; i++) {
	updateBtns2[i].addEventListener('click', function(){
		var productId2 = this.dataset.product
		var action2 = this.dataset.action
		console.log('productId:', productId2, 'Action:', action2)
		console.log( { 'USER': user })

		if (user == 'AnonymousUser'){
			console.log('User is not authenticated')

		}else{
			updateUserWishlist(productId2, action2)
		}
	})
}

function updateUserWishlist(productId2, action2){
	console.log('User is authenticated, sending data...')

		var url2 = '/update_wishlist/'

		fetch(url2, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			},
			body:JSON.stringify({'productId':productId2, 'action':action2})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    console.log( {'data' : data} )
			location.reload()
		});
}