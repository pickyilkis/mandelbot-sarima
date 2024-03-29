FROM mandelbot/base:0.5

COPY . .
RUN pip install gunicorn
ENV PYTHONPATH "/"
CMD exec gunicorn --bind :8080 --workers 1 --threads 8 app:app
