FROM node:16.10.0-alpine

WORKDIR /frontend

ENV PATH /frontend/node_modules/.bin:$PATH

COPY yarn.lock ./

COPY package.json ./

RUN yarn install

COPY . ./