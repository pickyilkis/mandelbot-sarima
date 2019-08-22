FROM mandelbot/base

COPY . .
ENV PYTHONPATH "/"
ENTRYPOINT ["python", "main.py"]
