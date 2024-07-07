FROM node:current-alpine as builder
#FROM node:16.17.0-alpine as builder
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH

RUN apk update
RUN apk upgrade

COPY . /app
RUN npm i

ENV NODE_ENV production
RUN npm run build

# production environment
FROM nginx:1.23.2-alpine

RUN apk --no-cache update
RUN apk --no-cache upgrade

COPY --from=builder /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
