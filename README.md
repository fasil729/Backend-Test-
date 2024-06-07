# Backend-Test-

Backend Test Project using Fast Api


- Utilize token-based authentication for the "AddPost" and "GetPosts" endpoints, obtainable from the "Login" endpoint.
- Implemented request validation for the "AddPost" endpoint to ensure the payload does not exceed 1 MB.
- Used in-memory caching for "GetPosts" to cache data for up to 5 minutes, employing tools like `cachetools` for this purpose.
- Ensured validation to guarantee the accuracy and integrity of data being processed. 


```
fastapi_app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── deps.py
│   │   ├── endpoints
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── posts.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── security.py
│   ├── crud
│   │   ├── __init__.py
│   │   ├── crud_user.py
│   │   ├── crud_post.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── post.py
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── token.py
│   │   ├── user.py
│   │   ├── post.py
│   ├── db
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── session.py
│   ├── utils
│   │   ├── __init__.py
│   │   ├── security.py
│   ├── alembic
│   │   ├── versions
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   ├── README
│   ├── .env
├── requirements.txt
├── alembic.ini
└── README.md
```
