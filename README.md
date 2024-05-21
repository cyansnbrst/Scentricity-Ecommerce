# Scentricity

An e-commerce application for the Scentriciry perfume store

### [Backend urls](https://github.com/cyansnbrst/Scentricity-Ecommerce/tree/master/scentricity_backend)
- api/v1/auth/
  - users/ [POST + json request] - create a user (register)
  - login/ [POST + json request] - login
  - logout/ [POST] - logout
- api/v1/cart/ [GET] - get current user's cart
  - change/<str:action>/<int:product_id>/ [PUT] - add or delete item from the cart
  - delete/<int:product_id>/ [DELETE] - delete all items of the same product from the cart
- api/v1/payment/create_checkout_session/ [POST] - creates a checkout session for the current user
- api/v1/orders/
  - my_orders/ [GET] - retrieves orders for the current user
  - order_info_stripe_webhook/ [POST + stripe request] - stripe webhook handler
- api/v1/products/ [GET] - get list/retrieve items from the store

### [Frontend urls](https://github.com/cyansnbrst/Scentricity-Ecommerce/tree/master/scentricity_frontend)
- / - home page
- /about - about page
- /shop - shop page (filter by brand or category included)
- /product/:id - product card page
- /account - profile and cart page
- /checkout - successfull checkout page
- /orders - orders page
