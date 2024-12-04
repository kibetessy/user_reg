# django-auth-example

## Setup Instructions

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone <repo-url>
   cd django-auth-example
   ```
2. Create a virtual env
   ```bash
   python3 -m venv path/to/venv
   source path/to/venv/bin/activate
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables

   ### Open auth_project/settings.py and set the following configurations:

   ```bash
   # email configs
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = "smtp.gmail.com"
   EMAIL_PORT = 465
   EMAIL_USE_SSL = True
   EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "youremail")
   EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "yourpassword")

   # database configs
   DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'test1',  # Replace with your database name
       'USER': 'postgres',  # Replace with your database user
       'PASSWORD': 'admin',  # Replace with your database password
       'HOST': 'localhost',
       'PORT': '5432',
   }}
   ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
7. Visit http://127.0.0.1:8000/ to register a user and test the functionality.
