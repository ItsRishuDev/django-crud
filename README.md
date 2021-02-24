Setup
The first thing to do is to clone the repository:

$ git clone https://github.com/ItsRishuDev/django-crud.git
$ cd django-crud

Install virtualenv

$ pip install virtualenv
$ pip install virtualenvwrapper

Create a virtual environment to install dependencies in and activate it:

$ mkvirtualenv crud-env
activate virtual environment by
$ workon env
Then install the dependencies:

(crud-env)$ pip install -r requirements.txt
Note the (crud-env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv.

Once pip has finished downloading the dependencies:

(crud-env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000/.

Now You Can perform CRUD Operations on your own system.
C - Create
R - Read
U - Update
D - Delete

Note : To perform Create, Update and Delete operations you need to register/login yourself.


If you want to use your own database then

Go to settings

inside the Database
replace
'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dcch********',
        'USER': 'kxuj******mh',
        'PASSWORD': 'f1**************************55b8c7cb01e',
        'HOST': 'ec2-52-203-27-62.compute-1.amazonaws.com',
        'PORT': '5432',
    }
    
with 

  'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
