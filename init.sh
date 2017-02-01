rm /etc/nginx/sites-enabled/default
ln -fs /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
/etc/init.d/nginx restart
ln -sf /home/box/web/etc/gunicorn_wsgi.conf /etc/gunicorn.d/hello.py
/etc/init.d/gunicorn restart

gunicorn -c /home/box/web/etc/django.py wsgi --daemon
