FROM node:current-alpine

RUN apk update && apk add git &&\ 
    git clone https://github.com/decentaur/dolfje.git /root/dolfje && \
    apk del git
WORKDIR /root/dolfje

RUN npm install dotenv localizify @slack/bolt mysql2

EXPOSE 6262

CMD ["index.js"]
