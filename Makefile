
celery:
	celery -A scrapy worker -l info

run:
	python3 manage.py runserver
