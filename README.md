# Cleaner App

This is a shared marketplace application for hiring cleaners.

## Getting setup
Make sure you have docker installed. Then type the following command into bash:

    docker run --name cleaner -e POSTGRES_PASSWORD=password -dp 5432:5432 postgres

Create a `.env` file in root of project. It should look like this:

    DB_USER=postgres
    PASSWORD=password
    SECRET_KEY=your-key

Check your setup works by running the tests: 

    PYTHONPATH=src/ nose2 -s tests/
