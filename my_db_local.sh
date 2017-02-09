sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE USER 'admin'"
mysql -uroot -e "SET PASSWORD FOR 'admin' = PASSWORD('123qweqwe123')"
mysql -uroot -e "CREATE DATABASE mybase"
mysql -uroot -e "GRANT ALL ON mybase.* TO 'admin'"
