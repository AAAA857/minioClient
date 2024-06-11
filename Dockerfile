FROM local.harbor.com/library/python:3.7
RUN mkdir /data
ADD web /data


RUN chmod -R 777 /data
WORKDIR /data/web
CMD ["python web.py"]