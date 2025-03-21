FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt ./
COPY bin ./bin
RUN pip install setuptools
RUN pip install --no-cache-dir -r requirements.txt --upgrade

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg mkvtoolnix

COPY *.py ./

CMD [ "python", "./optimus.py" ]