FROM python:3.12

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1

RUN mkdir -p /code
# A workaround for missing `setup.py` to allow absolute imports
RUN ln -s /code/app /usr/local/lib/python3.12/site-packages/

RUN pip install --upgrade pip

COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt

WORKDIR /code
COPY start.sh /code/
COPY . /code/

CMD ["/bin/bash"]
