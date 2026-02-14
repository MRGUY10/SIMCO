# Frontend Dockerfile
FROM node:22-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy application code
COPY . .

# Build for production
RUN npm run build

# Install serve for production
RUN npm install -g serve

# Expose port
EXPOSE 5173

# Serve production build
CMD ["serve", "-s", "dist", "-l", "5173"]
