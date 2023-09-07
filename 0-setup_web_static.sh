#!/usr/bin/env bash
# Sets up web servers for deployment of `web static`

# Install nginx if not already installed
if ! command -v nginx &> /dev/null; then
	sudo apt-get -y update
	sudo apt-get -y install nginx
	sudo ufw allow 'Nginx HTTP'
fi

# Create /data/web_static/releases/test, /data/web_static/current, and /data/web_static/shared if they don't exist
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Grant ownership of /data/ and it's contents to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Create fake HTML to test Nginx configuration
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symlink  /data/web_static/current to /data/web_static/releases/test/.
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set up nginx to serve static html from /data/web_static/current to hbnb_static
SERVER_CONFIG=\
"server {
        listen 80 default_server;
        listen [::]:80 default_server;
        index index.html;
        server_name _;

        location /hbnb_static/ {
        	alias /data/web_static/current/;
			try_files \$uri \$uri/ =404;
        }
		location / {
                try_files \$uri \$uri/ =404;
        }
}"

echo -e "Ceci n'est pas une page\n" > /var/www/html/404.html

# Update config file for nginx
echo "$SERVER_CONFIG" > /etc/nginx/sites-available/default

# Restart nginx
sudo service nginx restart
