# Django Girls Blog

A small Django project covering the [Django Girls tutorial](https://tutorial.djangogirls.org/en/) through the Django admin chapter. The blog uses SQLite and has a Post model registered in Django admin.

## Run it on Windows

Open this folder in VS Code and run these commands in the integrated terminal. Use Python 3.10 or newer.

```powershell
py -m venv myvenv
.\myvenv\Scripts\python.exe -m pip install -r requirements.txt
.\myvenv\Scripts\python.exe manage.py migrate
.\myvenv\Scripts\python.exe manage.py createsuperuser
.\myvenv\Scripts\python.exe manage.py runserver
```

On macOS or Linux, use `python3 -m venv myvenv` for the first command and `./myvenv/bin/python` for the rest.

Open [Django admin](http://127.0.0.1:8000/admin/), sign in with the superuser you just created, and choose **Posts → Add** to create a practice post.
