sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE USER 'admin'@'localhost'"
mysql -uroot -e "SET PASSWORD FOR 'admin'@'localhost' = PASSWORD('qweqwe123')"
mysql -uroot -e "CREATE DATABASE mybase"
mysql -uroot -e "GRANT ALL ON mybase.* TO 'admin'@'localhost'"