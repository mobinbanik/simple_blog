# Weblog with Django

## Description
This is a simple weblog built using Django framework. Users can register and then post articles and comments. There are also API endpoints available for fetching a list of articles and their titles, filtered by category.

## Installation
To run the weblog locally, follow these steps:
1. Clone the repository
2. Install the requirements using `pip install -r requirements.txt`
3. Run the migrations using `python manage.py migrate`
4. Start the server using `python manage.py runserver`

## URLs
- Login: `/login/`
- Logout: `/logout/`
- Register: `/register/`
- admin panel: `/admin/`
- Home: `/`
- Create Post: `post/create`
- Edit Post: `post/edit/<POST ID>/`
- Delete Post: `post/delete/<POST ID>/`
- Show Post: `post/<POST ID>/`

## API Endpoints
1. `/api/` - GET: Get a list of all posts
2. `/api/title/` - GET: Get a list of post titles


## Login Detail
superuser: admin
pass: admin

## Contributors
- [MobinBanikarim](https://github.com/Mobinbanikarim)