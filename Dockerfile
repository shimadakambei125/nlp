# dokcerfile, Image, Container
FROM python:3.10

ADD garden_file.py .

RUN pip install spacy

RUN python -m spacy download en_core_web_sm

CMD ["python","./garden_file.py"]