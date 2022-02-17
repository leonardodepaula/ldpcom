FROM node:lts-alpine

RUN npm install -g http-server

COPY ./frontend /frontend

WORKDIR /frontend

RUN npm install

RUN npm run build

CMD [ "http-server", "dist" ]