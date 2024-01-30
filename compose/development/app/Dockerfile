FROM python:3.10.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Node.js for Tailwind CSS
RUN apt update && apt install -y ca-certificates curl gnupg
RUN mkdir /etc/apt/keyrings && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
RUN echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_20.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list
RUN apt update && apt install nodejs -y

# Copy script helpers
COPY ./compose/development/app/runserver /usr/bin/runserver
RUN sed -i 's/\r$//g' /usr/bin/runserver && chmod +x /usr/bin/runserver

COPY ./compose/development/app/runtailwind /usr/bin/runtailwind
RUN sed -i 's/\r$//g' /usr/bin/runtailwind && chmod +x /usr/bin/runtailwind

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies
COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/development.txt

# Prepare Django dir
ENV APP_HOME /app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
