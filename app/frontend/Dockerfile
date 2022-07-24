FROM node:13.12.0-alpine

WORKDIR /frontend

ENV PATH /frontend/node_modules/.bin:$PATH

COPY yarn.lock ./

RUN yarn install

COPY . ./