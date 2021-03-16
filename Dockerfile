FROM bisaai/product:frontend_template 
RUN rm -rf /var/www/html/* 
COPY . /var/www/html/ 
RUN rm -rf /var/www/html/.git*; 
CMD apachectl -D FOREGROUND
