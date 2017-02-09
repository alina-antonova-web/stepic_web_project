sudo rm /etc/nginx/sites-enabled/default
sudo ln -fs ~/stepic_web_project/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf ~/stepic_web_project/etc/gunicorn_wsgi_local.conf /etc/gunicorn.d/hello.py
sudo ln -sf ~/stepic_web_project/etc/gunicorn_ask_local.conf /etc/gunicorn.d/ask.py
sudo /etc/init.d/gunicorn restart
