FROM python:3.6.4
ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt

CMD make clean && make download && make cython && make test && make run
