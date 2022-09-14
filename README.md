For create image in docker need write next:

"docker run -d -p 5672:5672 -p 15672:15672 rabbitmq:3-management"

For run celery worker need write next:

"celery -A celery_worker worker --loglevel=INFO --purge --pool=solo"