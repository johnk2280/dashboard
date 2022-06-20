# dashboard

### Реализованный функционал приложения:
1. Получает данные из google sheets при помощи Google API (ссылка на документ: https://docs.google.com/spreadsheets/d/1-bXdvjnBLdl5a3zAsMolx4i3LbP3MgXYYDG3rPVAzUw/edit?usp=sharing).
2. К данным таблицы добавляется колонка "стоимость в руб.".
3. Для перевода в рубли используются курсы ЦБ РФ.
4. Данные добавляются в БД (используется PostgreSQL).
5. Реализован функционал проверки истечения срока поставки. В случае, если срок прошел, отрправляется сообщение в Telegram.
6. Реализовано одностроничное web-приложение на основе Django. Fron-end - шаблонизатор Django.
7. Скрипт работает постоянно.

### TODO:
1. Упаковать в docker контейнер.
2. Фронтенд реализовать на основе React.

### Применяемый стек:
- Python 3.10
- Django 4.0.5
- PostgreSQL

### Инструкция по установки на локальнй хост.
1. Склонируйте текущий репозиторий командой:

          $ git clone https://github.com/johnk2280/dashboard.git
          
2. В корневой папке **dashboard** установите виртуальное окружение.
3. Обновите пакет **pip** командой:

          $ python -m pip install --upgrade pip
          
4. Установите зависимости командой:

          $ pip3 install -r requirements.txt
          
5. В директории основного приложения **numbers_dushboard** создайте файл **.env**
                   
5. Создайте базу данных:


        $ sudo -u postgres psq
        
        postgres=# CREATE DATABASE <db_name> OWNER <owner_name>;

4. Подключить БД в настройках (../numbers_dushboard/settings.py):


        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': env('DB_NAME'),
                'USER': env('DB_USER'),
                'PASSWORD': env('DB_PASSWORD'),
                'HOST': 'localhost',
            }
        }
