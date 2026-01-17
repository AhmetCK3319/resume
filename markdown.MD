

```bash
docker exec -it app python manage.py makemigrations
docker exec -it app python manage.py migrate
docker exec -it app python manage.py createsuperuser
docker exec -it app pip freeze > requirements.txt  
```

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

# Eğer Layout fonksiyonu varsa database hatası almamak için, 
    def get_setting(key, MODEL=None, parameter_name=None):
        if not parameter_name:
            parameter_name = 'parameters'
        if not MODEL:
            MODEL = GeneralSetting
        general_setting = MODEL.objects.filter(name=key).first()
        if general_setting:
            return getattr(general_setting, parameter_name)
        else:
            return '' 