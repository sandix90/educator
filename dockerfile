FROM python:3.6-alpine as builder

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt


FROM nginx:stable-alpine
COPY --from=builder . .
COPY --from=builder /app/nginx.site.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/nginx.conf /etc/nginx/nginx.conf

WORKDIR /app/
RUN chmod 755 /app/.docker_entrypoint.sh
ENTRYPOINT ["/app/.docker_entrypoint.sh"]