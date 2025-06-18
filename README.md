# Tribbleproxy

Tribbleproxy is a simple proxy that simulates various endpoints used by much of Golden & Silver Age Minecraft.

## Features

- :white_check_mark: <b1.8 authentication
- :white_check_mark: Skins
- :x: Capes
- :x: Snooper (intentionally blocked)
- :x: 1.6 update notification (intentionally disabled)
- :x: Non Minecraft traffic (intentionally blocked)

## Compatible versions

- Beta 1.2_02 - 1.8
- Release 1.0.0 - 1.5.2

## Example Command

```bash
podman run -p 8080:8080 \
  -v ./tribbleproxy.py:/tribbleproxy.py \
  -ti docker.io/mitmproxy/mitmproxy \
  mitmdump -s /tribbleproxy.py
```

## Example Usage

Add the following JVM arguments:

```
-Dhttp.proxyHost=localhost -Dhttp.proxyPort=8080
```
