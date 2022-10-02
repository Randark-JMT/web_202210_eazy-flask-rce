FROM python:3.9
LABEL auther="Randark_JMT"
WORKDIR /app

RUN pip install flask \
    -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY ./src .
COPY ./docker/bin /root/

ENV FLASK_APP=app

ENTRYPOINT ["bash","/root/start.sh"]