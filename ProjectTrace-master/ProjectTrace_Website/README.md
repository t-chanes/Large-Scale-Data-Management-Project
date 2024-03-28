# Website Replication Instructions
## AWS Virtual Machine Setup
Create an account at [aws.amazon.com](https://aws.amazon.com/).
The account will have free-tier benefits for 1 year after creation.
### Create a new EC2 instance
1.) Navigate to the EC2 Dashboard in the Management Console\
2.) Navigate to the 'Instances' tab and select 'Launch Instance'\
3.) Enter a name for your instance\
4.) Under 'Application and OS Images' select 'Ubuntu Server 22.04 LTS (HVM), SSD Volume Type' as your Amazon Machine Image\
5.) Under 'Instance Type' select 't2.micro' as your Instance type\
6.) Under 'Key Pair (login)' create a new key pair. This will create and download a .pem file that you will need in order to connect to your instance.\
7.) Under 'Network Settings' allow SSH, HTTPS, and HTTP traffic.\
8.) Under 'Configure Storage' allocate 30GiB gp2 Root volume.

After creating the instance with these settings, you will see it listed in your 'Instances' tab. Once it is running, you can select 'Connect' and follow the instructions given to connect to the instance.

While it isn't necessary, it is recommended to create an Elastic IP for your instance. This will prevent your instance's url from changing if it were to crash or be stopped.

## Nginx Setup
### Install Nginx Web Server and PHP
$sudo apt-get update\
$sudo apt-get upgrade\
$sudo apt-get install nginx\
$sudo apt-get install php-fpm

### SSL Configuration
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt\
sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048\
sudo vi /etc/nginx/snippets/self-signed.conf
```
ssl_certificate /etc/ssl/certs/nginx-selfsigned.crt;
ssl_certificate_key /etc/ssl/private/nginx-selfsigned.key;
```
sudo vi /etc/nginx/snippets/ssl-params.conf
```
ssl_protocols TLSv1.2;
ssl_prefer_server_ciphers on;
ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";
ssl_ecdh_curve secp384r1;
ssl_session_cache shared:SSL:10m;
ssl_session_tickets off;
ssl_stapling on;
ssl_stapling_verify on;
resolver 8.8.8.8 8.8.4.4 valid=300s;
resolver_timeout 5s;
add_header Strict-Transport-Security "max-age=63072000; includeSubdomains";
add_header X-Frame-Options DENY;
add_header X-Content-Type-Options nosniff;
ssl_dhparam /etc/ssl/certs/dhparam.pem;
```

### Web Server Configuration
sudo vi /etc/nginx/sites-available/default
```
Remove from SSL Directives:
	'listen 80*' directives
Add to SSL Directives:
	listen 443 ssl http2 default_server;
	listen [::]:443 ssl http2 default_server;
	include snippets/self-signed.conf;
	include snippets/ssl-params.conf;
	
	location ~ \.php$ {
		root /var/www/html;
		try_files $uri =404;
		fastcgi_split_path_info ^(.+\.php)(/.+)$;
		fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
		fastcgi_index index.php;
		fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
		include fastcgi_params;
		fastcgi_read_timeout 300;
	}
	
Modify in SSL Directives:
	index index.html index.php
	server_name [YOUR SERVER NAME (ec2.example.amazonaws.com)];
	
Create New Server Directive:
	server {
		listen 80 default_server;
		listen [::]:80 default_server;
		server_name [YOUR SERVER NAME (ec2.example.amazonaws.com)];
		return 302 https://$server_name$request_uri;
	}
```
### Restart Webserver
sudo nginx -t\
sudo service nginx reload

### Navigate to Webpage Directory
cd /var/www/html\
*Place .html/.php/etc files here*
