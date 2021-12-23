# safe-project
This project is the backend for a simple e-commerce app. Built with Python/Django/Django REST framework.


### Features
A few of the things you can do with this app:

- Admin can create/update/delete product, category, company and cpu
- Authenticated users can make GET requests to product, category, company and cpu
- Unauthenticated users can't  make GET requests
- Users can login to be authorized

### Installing Dependencies for the project

1. **Python** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, run:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.

#### Key Dependencies

- [Django](https://www.djangoproject.com/) is a Python-based free and open-source web framework that follows the model–template–views architectural pattern

- [Django REST framework](https://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

- [PostgreSQL](https://www.postgresql.org/) The World's Most Advanced Open Source Relational Database

### Running the server

First ensure you are working using your created virtual environment.

To run the server locally, execute:

```bash
python manage.py runserver --settings=safeProject.settings_local
```

### API Reference
The app is deployed to [Heroku](https://www.heroku.com/home)

[Base URL](https://safe-project0.herokuapp.com/)

[API Documentation](https://safe-project0.herokuapp.com/docs)


### Admin Credentials
Username: ```admin```

Password: ```admin```

### User Credentials
Username: ```user```

Password: ```Aa1234500```


### Testing
Run test cases
```bash
python manage.py test --settings=safeProject.settings_local
```
