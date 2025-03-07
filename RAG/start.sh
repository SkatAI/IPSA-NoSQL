#!/bin/bash

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "Please update the .env file with your MongoDB connection details before running the application."
    exit 1
fi

# Start the application
echo "Starting the RAG Search Application..."
docker-compose up
