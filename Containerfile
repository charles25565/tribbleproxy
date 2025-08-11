FROM docker.io/mitmproxy/mitmproxy:latest

COPY tribbleproxy.py /tribbleproxy.py

EXPOSE 8080
CMD ["/usr/bin/env", "mitmdump", "-s", "/tribbleproxy.py"]
