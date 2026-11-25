# Django Girls Blog

This project follows the [Django Girls tutorial](https://tutorial.djangogirls.org/en/) through dynamic data in templates. The home URL calls the `post_list` view, which uses the Django ORM to load published posts from SQLite in publication order. The HTML template displays each post's title, date, and text.

## Run in VS Code on Windows

Open the inner `django-blog` folder, where `manage.py` is located. In the integrated PowerShell terminal, run these commands with Python 3.10 or newer installed.

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py seed_posts
$env:DJANGO_DEBUG = "1"
.\.venv\Scripts\python.exe manage.py runserver
```

Open [the blog](http://127.0.0.1:8000/). To create posts yourself, run `manage.py createsuperuser` with the same Python executable, then sign in at [Django admin](http://127.0.0.1:8000/admin/). Set a publication date at or before the current time to make a post visible.

## Deploy to PythonAnywhere

In a PythonAnywhere Bash console, choose a Python version that matches your web app. These commands use Python 3.10.

```bash
git clone https://github.com/Chairman-Cyclonus/django-blog.git
cd django-blog/django-blog
python3.10 -m venv ~/.virtualenvs/django-blog
source ~/.virtualenvs/django-blog/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_posts
python manage.py collectstatic --noinput
```

On the **Web** tab, add a web app using **Manual configuration** with the same Python version. Set its virtualenv to `/home/YOUR_USERNAME/.virtualenvs/django-blog`. Add a static files mapping from `/static/` to `/home/YOUR_USERNAME/django-blog/django-blog/static`.

Generate a secret in your Bash console with `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`. Keep that value in the PythonAnywhere WSGI configuration only. Replace the WSGI file linked on the **Web** tab with the following, substituting your own username, exact web app hostname, and generated key.

```python
import os
import sys

sys.path.insert(0, "/home/YOUR_USERNAME/django-blog/django-blog")
os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"
os.environ["DJANGO_ALLOWED_HOSTS"] = "YOUR_USERNAME.pythonanywhere.com"
os.environ["DJANGO_SECRET_KEY"] = "PASTE_YOUR_GENERATED_KEY_HERE"

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
```

Reload the web app, then open its public HTTPS link from the **Web** tab. The two sample posts should appear. For later updates, run `git pull` from the checkout and reload the web app.
