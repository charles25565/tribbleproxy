# Copyright 2025 Charles

FROM docker.io/mitmproxy/mitmproxy:latest

COPY src/ /app

EXPOSE 8080
CMD ["/usr/bin/env", "mitmdump", "-s", "/app/main.py"]
