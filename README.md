# Django Meta Pages
Django Library To Use Meta Tags And Schema Structure In Any URL Path


# Step 1 Installation
first need install with pip
```bash
pip install django-meta-pages
```

# Step 2 settings.py

First Add To INSTALLED_APPS

Next Step

Add To Templates context_processors

```bash

INSTALLED_APPS = [
    ...
    'meta_pages',
    ...
]

TEMPLATES = [
    {
      ...
        "OPTIONS": {
            "context_processors": [
                ...
                "meta_pages.context_processors.schema",
                "meta_pages.context_processors.meta",

            ],
        },
    },
]
```
# Step 3
Include Meta Template To Your Base Template
```bash
<head>
{% include 'meta_pages/meta.html' with meta=meta %}
</head>
```

# Step 4
**python manage.py migrate**

Done!
