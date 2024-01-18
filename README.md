# Flask_Blog

### Introduction

A blog website with functionalities, including: user registration, login, post creation, post update, post deletion, and password reset.

- Language: \
  Python
- Framework:\
  Flask

### Structure
```
.
├── README.md
├── flaskblog
│   ├── __init__.py
│   ├── config.py
│   ├── errors
│   │   ├── __init__.py
│   │   └── handlers.py
│   ├── main
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── models.py
│   ├── posts
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── routes.py
│   ├── static
│   │   ├── main.css
│   │   └── profile_pics
│   │       ├── 6d753ce3e3fe0405.jpg
│   │       ├── b6e1c53325f88b74.png
│   │       └── default.jpg
│   ├── templates
│   │   ├── about.html
│   │   ├── account.html
│   │   ├── create_post.html
│   │   ├── errors
│   │   │   ├── 403.html
│   │   │   ├── 404.html
│   │   │   └── 500.html
│   │   ├── home.html
│   │   ├── layout.html
│   │   ├── login.html
│   │   ├── post.html
│   │   ├── register.html
│   │   ├── reset_request.html
│   │   ├── reset_token.html
│   │   └── user_posts.html
│   └── users
│       ├── __init__.py
│       ├── forms.py
│       ├── routes.py
│       └── utils.py
├── instance
│   └── site.db
└── run.py
```
