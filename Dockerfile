FROM mandelbot/base

WORKDIR /home
COPY . .
ENV PYTHONPATH "/home"
ENTRYPOINT ["python", "main.py"]
