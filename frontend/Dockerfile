# Stage 1: Build the frontend
FROM node:20-alpine AS build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json first
COPY package*.json ./

# Install ALL dependencies (including devDependencies like Vite)
RUN npm install

# Copy the rest of the app
COPY . .
EXPOSE 3000
# Run Vite dev (for development) OR build for production
# For now we keep dev mode
CMD ["npm", "run", "dev", "--", "--host"]

# Stage 2 (optional): Serve build files with nginx if production
# Uncomment this if you want a production build instead of dev mode
# FROM nginx:alpine
# COPY --from=build /app/dist /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]
