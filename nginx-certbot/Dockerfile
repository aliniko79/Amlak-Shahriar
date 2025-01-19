FROM nginx:latest
RUN apt-get update && apt-get install -y certbot python3-certbot-nginx cron
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY renew-certs.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/renew-certs.sh
RUN echo "0 0 * * * /usr/local/bin/renew-certs.sh" > /etc/cron.d/certbot