django-jinja-gtm
================

Jinja2 macro to install your Google Tag Manager account in Jinja2
templates (http://www.google.com/tagmanager/)

## Installation and Usage

1. Run `pip install git+https://github.com/dbarchowsky/django-jinja2-gtm#egg=django-jinja2-gtm`
2. Add template directory to the `DIRS` property of `TEMPLATES` in `yourapp/settings.py`:
```python
        os.path.join(DJANGO_ROOT, os.pardir, 'jinja2_gtm', 'jinja2'),
```
3. In `yourapp/settings.py` create a constant to store the Google Tag Manager container id, e.g. `GOOGLE_TAG_ID = 'GTM_XXXXXX'`
4. Import the constant into `yourapp/jinja2.py`, and add it to the Jinja2 environment in order to make it available 
   to all templates.
5. Add `{% from "gtm/gtm.html" import gtm %}` to template.
6. Add `{{ gtm(GOOGLE_TAG_ID) }}` right after the `<body>` tag.

The template that defines the macro is `gtm/gtm.html`, if for any reason it needs to be overridden.
