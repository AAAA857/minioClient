FROM local.harbor.com/library/python-flask-docker
RUN mkdir /data
ADD . /data
RUN chmod -R 777 /data
CMD ["./data/web.py"]