# Start from the official Base Image
FROM jupyter/datascience-notebook

# Copy the file with the requirements to the '/app' directory.
COPY requirements.txt .

# Install requirements
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

RUN git clone https://github.com/promptslab/Promptify.git
RUN pip3 install openai