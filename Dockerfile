FROM local.harbor.com/library/python-flask-docker

ADD . /
CMD ["./web.py"]