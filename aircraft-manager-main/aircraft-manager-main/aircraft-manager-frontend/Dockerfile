# Start with a Node.js base image
FROM node:14

# Setting working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy application code
COPY . .

# Exposes the port 
EXPOSE 3000

# Command ran when starting container
CMD ["npm", "start"]
