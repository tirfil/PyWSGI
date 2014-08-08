Apache version
code is located under /var/www/wsgi
add package mod_wsgi
add to /etc/httpd/conf/httpd.conf (path=/app)

WSGIScriptAlias /app /var/www/wsgi/mywebsite.py
<Directory /var/www/wsgi>
      Options -Indexes -Multiviews +ExecCGI
      Order allow,deny
      Allow from all
</Directory>
<VirtualHost *:80>
      RewriteEngine On
      RewriteCond %{REQUEST_URI} !^/app.*$
      RewriteRule ^(.*)$ /app$1 [L,R=301]
</VirtualHost>
