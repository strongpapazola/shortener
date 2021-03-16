FROM bisaai/product:frontend_template 
RUN rm -rf /var/www/html/* 
COPY . /var/www/html/ 
RUN rm -rf /var/www/html/.git*;
RUN chown -R www-data:www-data /var/www/html;
CMD apachectl -D FOREGROUND
