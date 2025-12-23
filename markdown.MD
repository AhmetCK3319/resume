# DJANGO KURULUMU
### - pip install Django
### - django-admin startproject resume .
### - python manage.py startapp core
### - pip install virtualenv
### - .gitignore kur (toptal)
### - pip install virtualenv
### - virtualenv myenv
### - source myenv/bin/activate
### - deactivate
### - python manage.py makemigrations
### - python manage.py migrate
### - python manage.py createsuperuser
### - python manage.py runserver

## GİT KOMUTLARI
### - git init
### - git add .
### - git commit -m 'commit message'
### - git branch -M main
### - git remote add origin git@github.com:AhmetCK3319/resume.git
### - git push -u origin main
### - git clone git@github.com:AhmetCK3319/resume.git
### - git pull

# AKTİF OLAN SAYFANIN YAZISINI KOYU YAPMAK
### {% if request.resolver_match.url_name == 'index' %} active {% endif %}