# Start from the official Base Image
FROM jupyter/datascience-notebook

RUN git clone https://github.com/promptslab/Promptify.git

# Copy the file with the requirements to the '/app' directory.
COPY requirements.txt .

# Install requirements
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

RUN pip install -U spacy

RUN python -m spacy download en

RUN python -m spacy download en_core_web_sm




