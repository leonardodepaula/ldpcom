FROM node:lts-alpine as build-stage

COPY ./frontend /frontend

WORKDIR /frontend

RUN npm install
RUN npm run build

FROM nginx:latest as production-stage

RUN mkdir -p /var/www/challenges/

# Config
COPY ./nginx/conf/nginx-localhost.conf /etc/nginx/nginx.conf
COPY ./nginx/conf/gzip.conf /etc/nginx/gzip.conf

# Static
COPY ./backend/app/static /static

# Vue.js dist
COPY --from=build-stage /frontend/dist /usr/share/nginx/html

# make all files belong to the nginx user
RUN chown nginx:nginx /usr/share/nginx/html