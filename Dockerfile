FROM python:3.11.0

WORKDIR /home/api

COPY server server
COPY requirements.txt requirements.txt
COPY serverConfig.py serverConfig.py

RUN apt full-upgrade -y && \
    python3 -m venv . && \
    pip install -r requirements.txt && \
    rm -rf /var/lib/apt/lists

ENTRYPOINT ["uvicorn", "server:app", "--port", "7878", "--host", "*"]
