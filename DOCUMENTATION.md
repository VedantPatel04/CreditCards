# Credit Card Recommendation System - Implementation Log

**Tech:** Django 5.0.1, DRF 3.14.0, Python 3.10+  
**Project:** `CreditCardRecommendation`

---

## Milestone 1: Backend Skeleton

**Goal:** Django + DRF running with a working health endpoint

### Implementation Steps

#### 1. Dependencies (`requirements.txt`)
```
Django==5.0.1
djangorestframework==3.14.0
python-decouple==3.8
```

#### 2. Initialize Project
```bash
django-admin startproject CreditCardRecommendation
python manage.py startapp api
```

#### 3. Register Apps (`settings.py`)
```python
INSTALLED_APPS = [
    'api',              # Custom API app
    'rest_framework',   # DRF - must be registered!
    # ... Django defaults
]
```

#### 4. Create Endpoint (`api/views.py`)
```python
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def checkpoint(request, format=None):
    return Response({'status': 'OK user'})
```

**Note:** `format=None` param required in view func definition for format suffix support

#### 5. Configure URLs (`urls.py`)
```python
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import checkpoint

urlpatterns = [
    path('api/checkpoint', checkpoint),  # No trailing slash
]
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
```

#### 6. Run Server
```bash
python manage.py migrate
python manage.py runserver
```

### Testing

| URL | Result |
|-----|--------|
| `/api/checkpoint` | DRF browsable interface |
| `/api/checkpoint.json` | Pure JSON |
| `/api/checkpoint.api` | DRF browsable interface (explicit url -- notice the '.api' at the end) |

---

## Errors & Solutions

### Error 1: `TemplateDoesNotExist - rest_framework/api.html`

**Cause:** `rest_framework` installed but not in `INSTALLED_APPS`  
**Solution:** Add `'rest_framework'` to `INSTALLED_APPS`

### Error 2: `checkpoint() got unexpected keyword argument 'format'`

**Cause:** Using `format_suffix_patterns` but view doesn't accept `format` parameter  
**Solution:** Change `def checkpoint(request):` to `def checkpoint(request, format=None):`

### Error 3: `/api/checkpoint.html` returns 404

**Cause:** `.html` is not a DRF format  
**Solution:** Use `.api` for browsable interface or `.json` for JSON

---

## ✅ Milestone 1 Complete

- Django + DRF configured
- Health endpoint working
- Format suffixes enabled
- Server boots cleanly

---

## Next: Milestone 2 - Card Catalog

1. Create `Card` and `EarningRule` models
2. Register in Django admin
3. Build `GET /api/cards` endpoint

---

## Resources

- [Django Docs](https://docs.djangoproject.com/)
- [DRF Docs](https://www.django-rest-framework.org/)
- [Format Suffixes](https://www.django-rest-framework.org/api-guide/format-suffixes/)
