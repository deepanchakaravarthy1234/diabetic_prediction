# Use Node.js
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy all source code
COPY . .

# Vite default port
EXPOSE 5173

# Run Vite dev server and expose to host
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
