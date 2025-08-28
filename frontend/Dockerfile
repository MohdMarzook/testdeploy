# Use a lightweight Nginx image as the base
FROM nginx:alpine

# Copy the static HTML file to Nginx's default web root directory
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80 for HTTP traffic
EXPOSE 80

# The CMD instruction is inherited from the base image and is not needed here.
# It will run Nginx when the container starts.
s