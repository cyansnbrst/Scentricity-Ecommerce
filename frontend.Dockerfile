FROM node:latest

WORKDIR /frontend
EXPOSE 8080

COPY scentricity_frontend/package*.json ./

RUN npm install

COPY scentricity_frontend /frontend

CMD ["npm", "run", "serve"]
