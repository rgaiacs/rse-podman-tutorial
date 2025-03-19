FROM docker.io/alpine:3.21.3

RUN apk add --no-cache \
    python3 \
    py3-pip \
    py3-virtualenv

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3 -m pip install \
    Flask==3.1.0

WORKDIR /var/app

EXPOSE 5000

ENTRYPOINT [ \
    "flask", \
    "run", \
    "--host", \
    "0.0.0.0", \
    "--port", \
    "5000", \
    "--reload", \
    "--debugger" \
]
