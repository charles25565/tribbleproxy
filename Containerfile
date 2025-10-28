FROM docker.io/mitmproxy/mitmproxy:latest

COPY src/ /app

EXPOSE 8080

ENTRYPOINT ["/usr/bin/env", "mitmdump", "-s", "/app/main.py"]