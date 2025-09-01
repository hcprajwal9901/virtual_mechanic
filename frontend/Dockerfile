FROM node:20-alpine
WORKDIR /app
COPY package.json /app/
RUN npm install --no-audit --fund=false
COPY index.html /app/index.html
COPY vite.config.js /app/vite.config.js
COPY src /app/src
COPY public /app/public
EXPOSE 3000
ENV VITE_API_BASE=
CMD ["npm", "run", "preview"]