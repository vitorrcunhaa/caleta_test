# caleta_test
Caleta Gaming test for full stack programmer position.

## Running the app on your local computer

- `git clone https://github.com/vitorrcunhaa/caleta_test.git` or unpack compressed file(if you got this project via compressed file)

- Go to `caleta_test` dir

To run the Django app on your local computer, set up a Python development environment, including Python, pip, and virtualenv.

Create an isolated Python environment, and install dependencies:

LINUX/MACOS
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
WINDOWS
```
virtualenv env
env\scripts\activate
pip install -r requirements.txt
```
Run the Django migrations to set up your models:
```
python manage.py makemigrations
python manage.py migrate
```
Start a local web server:

`python manage.py runserver`

In your browser, go to http://localhost:8000:


# Using the Django admin console

- Create a superuser. You need to define a username and password.
`python manage.py createsuperuser`

- Start a local web server:
`python manage.py runserver`

- In your browser, go to http://localhost:8000/admin.
