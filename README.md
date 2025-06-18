# Tribbleproxy

Tribbleproxy is a simple proxy that simulates various endpoints used by much of Golden & Silver Age Minecraft.

## Features

- :white_check_mark: <b1.8 authentication
- :white_check_mark: Skins
- :white_check_mark: Capes
- :x: Snooper (intentionally blocked)
- :x: 1.6 update notification (intentionally disabled)

## Example Configuration

Save this as `tribbleproxy.properties`.

```json
{
  "charles25565": {
    "skin": "skin.png",
    "cape": "cape.png"
  }
}
```

## Example Command

```bash
podman run -p 8080:8080 \
  -v ./tribbleproxy.py:/tribbleproxy.py \
  -v ./tribbleproxy.properties:/tribbleproxy.properties \
  -v ./skin.png:/skin.png \
  -v ./cape.png:/cape.png \
  -ti docker.io/mitmproxy/mitmproxy \
  mitmdump -s /tribbleproxy.py
```

## Example Usage

Add the following JVM arguments:

```
-http.proxyHost=localhost -http.proxyPort=8080
```
