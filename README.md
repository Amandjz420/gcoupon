

To run celery beat (task giver):

celery -A gcoupon beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

To start celery worker

celery -A gcoupon worker -l INFO --scheduler 


