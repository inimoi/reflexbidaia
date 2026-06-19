FROM python:3.12 AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y curl unzip && rm -rf /var/lib/apt/lists/*

COPY . .
RUN pip install -r requirements.txt
RUN reflex --version && reflex export --help || true
RUN reflex export --frontend-only --no-zip

FROM nginx

COPY --from=builder /app/.web/build/client /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

