FROM alpine:latest

WORKDIR /app

ADD ./pdqhashing /app/pdqhashing
ADD main.py /app
ADD requirements.txt /app


RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
    apk update  && \
    apk add python3 py3-pip && \
    rm -rf /tmp && \
    pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt  -i https://pypi.tuna.tsinghua.edu.cn/simple/


EXPOSE 9000

#CMD ["flask","--app","main","run", "--host=0.0.0.0"]
CMD ["python3", "main.py"]