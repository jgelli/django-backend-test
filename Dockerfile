FROM python:3.11-slim as builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Cria usuário não-root por segurança
RUN useradd -ms /bin/bash django
USER django

EXPOSE 8000


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "walletapi.wsgi"]