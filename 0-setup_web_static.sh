#!/usr/bin/env bash
# install nginx if it doesn't exist
if [ "$(which nginx | wc -l)" == 0 ]; then
    # install nginx
    apt-get -y update
    apt-get -y install nginx
fi

# shellcheck disable=SC2230
# create structure folders
mkdir -p /data/web_static/{releases/test,shared}
home_page="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

# create fake home page
echo "$home_page" > /data/web_static/releases/test/index.html

# a symbolic link linked to our release folder
[ -d /data/web_static/current ] && rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test /data/web_static/current

# give ownership to ubuntu user
chown -R ubuntu:ubuntu /data

mystr="\n\tlocation = \/hbnb_static \{\n\t\talias \/data\/web_static\/current\/\;\n\t\ttry_files \$uri \$uri\/ =404\;\n\t\}"
replace="server {"
sed -i "0,/$replace/{s/$replace/$replace$mystr/}" /etc/nginx/sites-available/default

# override the link to default
# ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
# check if nginx is started to restart it
if [ "$(pgrep -c nginx)" -le 0 ]; then
	service nginx start
else
	service nginx restart
fi
