FROM python:3.12 AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y curl unzip && rm -rf /var/lib/apt/lists/*

COPY . .
RUN pip install -r requirements.txt
RUN set -x
&& echo "== which reflex ==" && which reflex || true
&& echo "== reflex --version ==" && reflex --version || true
&& echo "== reflex export --help ==" && reflex export --help || true
&& echo "== list . and .web ==" && pwd && ls -la . && ls -la .web || true
&& echo "== Ejecutando reflex y guardando salida =="
&& sh -c 'reflex export --frontend-only --no-zip > /tmp/reflex.stdout 2> /tmp/reflex.stderr || true'
&& echo "== reflex stdout ==" && sed -n '1,200p' /tmp/reflex.stdout || true
&& echo "== reflex stderr (últimas 200 líneas) ==" && sed -n '1,200p' /tmp/reflex.stderr || true
&& echo "== fin debug reflex =="
RUN reflex export --frontend-only --no-zip

FROM nginx

COPY --from=builder /app/.web/build/client /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

