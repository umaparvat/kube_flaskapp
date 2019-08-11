FROM python:3.6

VOLUME /app
# Set the working directory to /app
WORKDIR /app

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY ./requirements.txt  /app
RUN pip install --trusted-host pypi.python.org virtualenv
RUN virtualenv venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN  pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000

# CMD ["/app/venv/bin/python", "manage.py", "run"]
CMD ["gunicorn", "-b", "0.0.0.0:5000", "manage:app"]

