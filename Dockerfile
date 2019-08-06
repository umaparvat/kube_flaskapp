FROM python:3.6

# Set the working directory to /app
WORKDIR /app

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY . /app
RUN pip install --trusted-host pypi.python.org virtualenv
RUN virtualenv venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN  /app/venv/bin/pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

CMD ["/app/venv/bin/python", "manage.py", "run"]
