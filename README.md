# Credit Card Recommendation System

Django REST Framework backend that analyzes credit card statements and recommends optimal cards based on spending patterns.

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cd CreditCardRecommendation
python manage.py migrate
python manage.py runserver         # Runs at http://127.0.0.1:8000
```

## API Endpoints

### Health Check (Milestone 1)

| Endpoint | Response |
|----------|----------|
| `GET /api/checkpoint` | DRF browsable interface |
| `GET /api/checkpoint.json` | `{"status":"OK user"}` |

**Examples:**
```bash
# Browser
http://127.0.0.1:8000/api/checkpoint.json

# curl
curl http://127.0.0.1:8000/api/checkpoint.json
```

## Common Commands

```bash
python manage.py runserver          # Start server
python manage.py makemigrations     # Create migrations
python manage.py migrate            # Apply migrations
python manage.py createsuperuser    # Create admin user
```

## Status

**✅ Milestone 1:** Backend skeleton + health endpoint working  
**Next:** Card catalog models and endpoints

## Tech Stack

- Django 5.0.1
- Django REST Framework 3.14.0
- SQLite (dev)
- Python 3.10+

## Troubleshooting

**"Template does not exist" error:** Add `'rest_framework'` to `INSTALLED_APPS` in `settings.py`

**Port in use:** `python manage.py runserver 8001`

---

For implementation details, see [DOCUMENTATION.md](./DOCUMENTATION.md)
