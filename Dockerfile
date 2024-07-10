FROM alpine:latest

WORKDIR /usr/src/app

RUN \
  apk update \
  && apk add \
  python3 \
  && apk upgrade 

COPY tfn_validator.py .

RUN \
  echo '' > /etc/passwd \
  && echo '' > /etc/shadow \
  && echo '' > /etc/group \
  && adduser -s /bin/sh -DH python \
  && chown -R python /usr/src/app \
  && chmod -R 755 /usr/src/app

USER python

ENTRYPOINT [ "python3", "tfn_validator.py" ]