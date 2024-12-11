# Build stage
FROM --platform=$BUILDPLATFORM node:20-slim as build

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Build the application (only for production)
RUN if [ "$NODE_ENV" = "production" ] ; then npm run build ; fi

# Development stage (default)
FROM build as dev
CMD ["npm", "run", "dev"]

# Production stage
FROM --platform=$BUILDPLATFORM nginx:alpine as prod

# Copy built assets from build stage
COPY --from=build /app/dist /usr/share/nginx/html

# Copy nginx config
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf

# Expose port
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"] 