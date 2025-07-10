# Tribbleproxy

Tribbleproxy is a simple proxy that simulates various endpoints used by much of Golden & Silver Age Minecraft.

## Features

- :white_check_mark: <b1.8 authentication
- :white_check_mark: Skins
- :white_check_mark: Capes
- :x: Snooper
- :x: 1.6 update notification
- :x: Non Minecraft traffic
- :x: Resources

## Compatible versions

- Infdev
- Alpha
- Beta
- Release &#8804; 1.5.2

## Example Command

```bash
podman run -p 8080:8080 \
  --rm \
  -v ./tribbleproxy.py:/tribbleproxy.py \
  -ti docker.io/mitmproxy/mitmproxy \
  mitmdump -s /tribbleproxy.py
```

## Example Usage

Add the following JVM arguments:

```
-Dhttp.proxyHost=localhost -Dhttp.proxyPort=8080
```
