# Simple Task Assignment API


repo: https://github.com/syntaxland/simple-task-assignment-api


# Basic Django Setup

# 1. Create the virtual environment
python3 -m venv venv

# 2. Activate it (Linux syntax)
source venv/bin/activate

# 3. Upgrade pip just to be safe
pip install --upgrade pip

# 4. Install the requirements
pip install -r requirements.txt


# 5. Initialize project in current directory (notice the dot '.')
django-admin startproject core .

# 6. Create your main API app
python manage.py startapp api

# 7. Run initial migrations to setup the local SQLite database
python manage.py migrate

# 8. Create an admin user (highly recommended to have ready)
python manage.py createsuperuser


# 9. Start the server to ensure everything boots up
python manage.py runserver


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    'corsheaders',
    
    # my apps
    'api',
]
