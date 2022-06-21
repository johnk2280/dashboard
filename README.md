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
- OS: Ubuntu 20.04
- Python 3.10
- Django 4.0.5
- PostgreSQL

### Инструкция по установке на локальнй хост.
1. Склонируйте текущий репозиторий командой:

          $ git clone https://github.com/johnk2280/dashboard.git
          
2. В корневой папке **dashboard** установите виртуальное окружение.
3. Обновите пакет **pip** командой:

          $ python -m pip install --upgrade pip
          
4. Установите зависимости командой:

          $ pip3 install -r requirements.txt
          
                   
5. Создайте базу данных:


           $ sudo -u postgres psq

           postgres=# CREATE DATABASE <db_name> OWNER <owner_name>;


6. В директории основного приложения **./numbers_dashboard** создайте файл **.env** и заполните на основе шаблона **.env.template**
7. Перейдите в директорию проекта и выполните миграции командой:
            
           $ python manage.py migrate
           
8. Если миграций не случилось и вылетело исключение, необходимо удалить файлы из директории:
**./numbers_dashboard/mainapp/migrations/0001_initial.py**
9. Создайте и выполните миграции заново:

           $ python manage.py makemigrations

           $ python manage.py migrate

10. Запустите проект (по умолчанию проект запускается на 8000 порту):

           $ python manage.py runserver
           
11. Перейдите по адресу: http://127.0.0.1:8000/orders/
