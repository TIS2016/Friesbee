# Friesbee
Databaza turnajov friesbee

# Návod na inštaláciu
Práca so zdrojovými súbormi je možná bez dodatočných úprav podľa nasledovného návodu len z operačného systému Linux. 

•	Inštalácia python 2.7 + pip.
		sudo apt-get install python2.7
		sudo apt-get install python-pip python-dev build-essential

•	Inštalácia Djanga a doplnkov.
		pip install -r requirements.txt

•	Vytvorenie mysql databázy.
		sudo apt-get install mysql-server
		sudo apt-get install python-mysqldb

•	Vytvorenie prístupu do lokálnej databázy.
		mysql -u root -p

•	Vytvorenie databázy.
		CREATE DATABASE frisbee DEFAULT CHARACTER SET utf8;

•	Nastavenie User a Password vo Frisbee/custom_settings.py
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

•	Následne prejdite do adresára, kde sa nachádza manage.py a spustite nasledujúce príkazy
	  python manage.py makemigrations
		python manage.py migrate
		python manage.py createsuperuser
		python manage.py runserver

