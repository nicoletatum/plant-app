rm -rf plantappapi/migrations

rm db.sqlite3

python manage.py makemigrations plantappapi

python manage.py migrate 

python manage.py loaddata users
python manage.py loaddata plantowners
python manage.py loaddata tokens

