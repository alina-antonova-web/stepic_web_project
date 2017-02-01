sudo rm /etc/nginx/sites-enabled/default
sudo ln -fs /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn_wsgi.conf /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
gunicorn -c /home/box/web/etc/django.py wsgi
