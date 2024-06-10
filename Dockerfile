FROM local.harbor.com/library/python-flask-docker
RUN mkdir /data/server
ADD . /data/server
CMD ["/data/server/web.py"]