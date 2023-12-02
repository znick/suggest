FROM python:3.12-slim

ADD requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

RUN mkdir /code/
WORKDIR /code/
ADD suggest.py /code/
Add ruwords.txt /code/

EXPOSE 5000

CMD ["/code/suggest.py"]
