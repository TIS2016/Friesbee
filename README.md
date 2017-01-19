# Friesbee
Databaza turnajov friesbee

Instalacia python 2.7 + pip.

sudo apt-get install python2.7

sudo apt-get install python-pip python-dev build-essential

Instalacia Djanga a doplnkov.
pip install -r requirements.txt

Vytvorenie mysql databazy.
sudo apt-get install mysql-server
sudo apt-get install python-mysqldb

Vytvorenie pristupu do lokalnej Db.
mysql -u root -p

Vytvorenie db.
CREATE DATABASE frisbee DEFAULT CHARACTER SET utf8;

Nastavit User a Password v Frisbee/custom_settings.py
DATABASES = {
  'default':{
      'ENGINE':'django.db.backends.mysql',
      'NAME': 'frisbee',
      'USER': '...',
      'PASSWORD': '...',
      'HOST': '127.0.0.1',
      'PORT': '3306',
  }
}


Prejst do adresara s manage.py a spustit nasledujuce prikazy

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
