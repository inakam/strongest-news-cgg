FROM node:16-stretch-slim AS base
WORKDIR /usr/src/app

FROM base AS dev
COPY package.json yarn.lock ./
RUN yarn install
ENTRYPOINT [ "yarn", "start" ]

# 参考実装¥
FROM base AS prod
ENV PATH /usr/src/app/node_modules/.bin:$PATH
COPY . .
RUN yarn install
RUN yarn add serve -g
ENTRYPOINT [ "yarn", "prod" ]