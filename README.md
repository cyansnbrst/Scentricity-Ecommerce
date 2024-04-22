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
