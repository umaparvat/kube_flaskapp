FROM python:3.6

# VOLUME /app
# Set the working directory to /app
RUN mkdir /app
WORKDIR /app

ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

COPY .  /app/
RUN pwd
RUN ls -latr /app/
RUN mkdir -p /app/gunicorn/var/log/ /app/gunicorn/var/run
RUN pip install --trusted-host pypi.python.org virtualenv
RUN virtualenv venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN  pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8443

# CMD ["/app/venv/bin/python", "manage.py", "run"]
#CMD ["gunicorn", "-b", "0.0.0.0:5000", "manage:app"]
#ENTRYPOINT [ "/bin/bash", ./entrypoint.sh" ]
CMD ["/bin/bash","-c", "./entrypoint.sh web && tail -f /dev/null"]

