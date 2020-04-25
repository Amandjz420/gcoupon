Dependency for the Gcoupon:

    Install Postgres
        create a database gcoupon
        user for postgres aman with password 12344321
    Install Celery
    Install Redis

    Make virtualenv gcoupon
    Install python library dependencies
        pip install -r requirement.txt
    
After Installing all the dependencies
Run the following command:
    
    # Creating tables in db
    python manage.py migrate
    # Populating the data from json file
    python manage.py populate_coupons -p db_data/deals.json   

Run the project using command:
    
    python manage.py runserver    
    
To run celery beat (task giver):

celery -A gcoupon beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

To start celery worker

celery -A gcoupon worker -l INFO --scheduler 

For seeing the dashboard go to:
    
    http://localhost:8000/admin

For coupon List api:

    http://localhost:8000/api/coupons/coupon/
    
For Category List api:
    
    http://localhost:8000/api/coupons/coupon/