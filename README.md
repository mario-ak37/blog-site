# Django Blog

A simple and clean blog built with Django. It supports creating posts, displaying them, filtering by tags, adding comments, and sharing posts by email. The project is minimal, functional, and easy to extend.

## Setup

Clone the repository:

```
git clone https://github.com/mario-ak37/blog-site.git
cd django-blog
```

Install dependencies using uv:

```
uv sync
```

Run migrations:

```
python manage.py migrate
```

Start the server:

```
python manage.py runserver
```

Access the site at:

```
http://localhost:8000/
```

## Features

- Post listing and detail pages
- Pagination
- Tag filtering
- Comment system
- Email sharing

---
