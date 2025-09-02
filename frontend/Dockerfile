# Use Node.js base image
FROM node:20-alpine

WORKDIR /app

# Copy only package.json and package-lock.json first
COPY package*.json ./

# Install ALL dependencies including devDependencies
RUN npm install --include=dev

# Copy rest of the frontend code
COPY . .

EXPOSE 3000

# Run vite via npx (uses local node_modules)
CMD ["npx", "vite", "--host"]

