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

RUN pip install keras

RUN pip install tensorflow

RUN pip install keras-crf

RUN pip -q install git+https://www.github.com/keras-team/keras-contrib.git sklearn-crfsuite

RUN pip install seqeval

#related tp health data
#Un comment this package if you want to divide the data
#pip3 install pyneuroner[cpu]



