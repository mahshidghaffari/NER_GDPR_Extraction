# Start from the official Base Image
FROM python:3.10

# Update
RUN apt-get -y update
RUN apt-get -y install vim

# Copy the file with the requirements to the '/app' directory.
COPY requirements.txt .

# Install requirements
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt