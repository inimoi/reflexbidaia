FROM python:3.12 AS builder

WORKDIR /app

# herramientas base + Node.js 18 (NodeSource)
RUN apt-get update \
  && apt-get install -y curl unzip ca-certificates gnupg \
  && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
  && apt-get install -y nodejs \
  && rm -rf /var/lib/apt/lists/*

COPY . .

# Python deps + reflex CLI
RUN pip install -r requirements.txt \
  && pip install reflex

# Instalar gestor de paquetes frontend según lockfile (opcional)
# - pnpm-lock.yaml -> pnpm
# - yarn.lock -> yarn
# - package-lock.json -> npm (ya viene con node)
RUN if [ -f pnpm-lock.yaml ]; then npm install -g pnpm; elif [ -f yarn.lock ]; then npm install -g yarn; fi

# (Opcional) instalar dependencias frontend en .web si tu proyecto las necesita
# Ajusta la ruta si tus assets frontend están en otra carpeta
RUN if [ -f .web/package-lock.json ]; then npm ci --prefix .web; \
     elif [ -f .web/pnpm-lock.yaml ]; then pnpm install --prefix .web; \
     elif [ -f .web/yarn.lock ]; then yarn install --cwd .web; \
     fi

# Depuración ligera antes de exportar (puedes quitarlo luego)
RUN echo "== debug reflex ==" && which reflex || true && reflex --version || true && pwd && ls -la

# Export del frontend con reflex
RUN reflex export --frontend-only --no-zip

FROM nginx

COPY --from=builder /app/.web/build/client /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
