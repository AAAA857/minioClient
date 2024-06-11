FROM local.harbor.com/library/python:3.7
RUN mkdir /data
ADD web /data
RUN chmod -R 777 /data
WORKDIR /data
CMD ["python","web.py"]