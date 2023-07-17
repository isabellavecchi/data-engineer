# Use the official MongoDB Docker image as the base image
FROM mongo

# Set the environment variables
ENV MONGO_INITDB_ROOT_USERNAME=admin
ENV MONGO_INITDB_ROOT_PASSWORD=password
ENV MONGO_INITDB_DATABASE=database

# Copy the initialization script to the container
COPY init.js /docker-entrypoint-initdb.d/

# Expose the MongoDB port
EXPOSE 27017