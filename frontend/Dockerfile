FROM node:22-bookworm-slim
WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y

RUN npm install
EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host"]