FROM tiagopeixoto/graph-tool:latest

WORKDIR /app
COPY . .

RUN python3 -m venv /opt/.venv --system-site-packages && \
    /opt/.venv/bin/pip install --upgrade pip && \
    /opt/.venv/bin/pip install -r requirements.txt

ENV PATH="/opt/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

WORKDIR /app/src

EXPOSE 30301 30302 30303 30304 30305

CMD ["sh", "-c", "exec gunicorn --timeout ${GUNICORN_TIMEOUT:-1200} --bind ${SERVICE_IP_ADDRESS:-0.0.0.0}:${SERVICE_PORT:-30301} flask_layout_service:app"]
