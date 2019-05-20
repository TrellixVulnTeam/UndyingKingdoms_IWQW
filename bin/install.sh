#!/bin/bash
# install all necessary things to develop this app.

# This script uses sudo only where absolutely necessary.
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path/.."  # make sure you are in the udk directory

# install modules
sudo apt-get update
sudo apt install python3 python3-venv python3-dev libmysqlclient-dev mysql-server
sudo -k

# setup virtual environment
rm -rf ~/virtual_envs/udk_env
python3 -m venv ~/virtual_envs/udk_env
rm -f activate
ln -s ~/virtual_envs/udk_env/bin/activate bin/activate
# allow activate script to auto start mysql
echo "
# Inject mysql startup into environment activation
sudo service mysql start
sudo -k
" >> bin/activate
. bin/activate
pip install -U pip
echo "Pip activated\n: $( pip --version )"

# install app
pip install .
echo "Downgrading Werkzeg ..."
pip install Werkzeug==0.14.1
deactivate

# Install mysql stuff
# Add new user with access to UDK tables.
read -s -p "Enter a new (or your old) mysql root password: " mysql_passwd
echo "
This next bit is a bit confusing:
1. Enter _your_ root password to gain access up mysql.
2. Then enter you current mysql root password
  (or leave it blank if you haven't set one).
  The previous mysql password doesn't count.
"
sudo mysql -u root -p -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '$mysql_passwd';"
sudo -k
mysql_cnf=~/.udk_mysql_config.cnf
rm -rf $mysql_cnf
echo "
[client]
user = root
password = $mysql_passwd
# Before use set file to read-only with \$ chmod 400 $mysql_cnf'
" > $mysql_cnf
chmod 400 $mysql_cnf
udk_user="elthran"
udk_db="undyingkingdoms"
mysql --defaults-file=$mysql_cnf -e "CREATE USER '$udk_user'@'localhost'IDENTIFIED BY '$mysql_passwd';"
mysql --defaults-file=$mysql_cnf -e "GRANT ALL ON $udk_db.* TO '$udk_user'@'localhost' WITH GRANT OPTION;"
mysql --defaults-file=$mysql_cnf -e "GRANT ALL ON ${udk_db}_test.* TO '$udk_user'@'localhost' WITH GRANT OPTION;"
chmod 600 $mysql_cnf
sed -i 's/root/'${udk_user}'/g' $mysql_cnf
chmod 400 $mysql_cnf
