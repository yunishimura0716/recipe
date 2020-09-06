# recipe app api
### Package/Framework in this repo
- Django
- Django rest api
- Docker, docker-compose
- Unittests, Travis CI
### Rest API endpoinnt
- api/user/
  - create/ : create user account
  - token/ : give user token to validate password authentication
  - me/ : give user information
- api/recipe/
  - tags/ : create, retrieve, list tags for recipe
  - ingredients/ : create, retrieve, list ingredients for recipe
  - recipes/ : create, retrieve, list recipes and upload image for it.
