FROM docker.io/mitmproxy/mitmproxy:latest

COPY src/ /app

EXPOSE 8080

ENTRYPOINT ["/app/run.sh"]