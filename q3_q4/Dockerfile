# Use the official MySQL image as the base image
FROM mysql:latest

# Environment variables for MySQL configuration
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=av2_db
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=root
COPY index.sql .
# Expose the MySQL port
EXPOSE 3306