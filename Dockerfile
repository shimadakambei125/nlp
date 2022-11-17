# dokcerfile, Image, Container
# https://www.youtube.com/watch?v=0UG2x2iWerk
# https://hub.docker.com/_/python
# I had to do a quick reading with regrads to dockerfile as this is something enew to me

# We selct the ppython version we are using
FROM python:3.10

# We add the file/select the file we want to to run
ADD garden_file.py .

# We pip install space module
RUN pip install spacy

# We again run the english module
# https://stackoverflow.com/questions/63497243/spacy-load-model-in-docker
#I learned how to do it 
RUN python -m spacy download en_core_web_sm

CMD ["python","./garden_file.py"]