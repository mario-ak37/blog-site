# Django Blog

A fully featured blog application built with Django. It provides clean content publishing, tagging, user comments, email sharing, and advanced search powered by PostgreSQL full-text indexing. The project follows best practices for maintainability, extensibility, and production readiness.

## Key Features

**Content and Publishing**

- Create, manage, and display blog posts
- Tagging system with tag filtering and recommendations
- Markdown support for rich text content

**User Interaction**

- Comment submission with moderation
- Share posts via email

**Search and Discovery**

- Full-text blog search using PostgreSQL
- Weighted search ranking (title prioritized over body)
- Custom template tags and filters
- RSS feed for subscribers
- SEO-friendly sitemap for search engines

**Architecture and Extendibility**

- Clean separation of concerns using Django apps
- Custom template tags for latest posts and most commented posts
- Utilizes Django’s authentication model for post authors
- Designed to run on PostgreSQL for robust search support

## Setup Instructions

### Clone the repository

```
git clone https://github.com/mario-ak37/blog-site.git
cd blog-site
```

### Install dependencies using uv

```
uv sync
```

### Configure PostgreSQL database

Update your `.env` or `settings.py` database configuration with PostgreSQL credentials:

```
DATABASE_URL=postgres://USER:PASSWORD@localhost:5432/blogdb
```

Create the database if it does not exist.

### Run migrations

```
python manage.py migrate
```

### Start the development server

```
python manage.py runserver
```

### Access the application

```
http://localhost:8000/
```

## Project Structure Overview

- `posts` app manages publishing, tagging, search, comments, and feeds
- Custom template tags enhance templates with reusable logic
- PostgreSQL search uses `SearchVector`, `SearchRank`, and `SearchQuery` for weighted results
- RSS feed and sitemap provide content syndication and SEO support
