# Tribbleproxy

Tribbleproxy is a simple proxy that simulates the endpoints for skins and capes for old versions of Minecraft. As a bonus, it also routes the `www.minecraft.net/game/joinserver.jsp` endpoint to the newer `session.minecraft.net` domain, and it also blocks snooper requests.

In theory it would work for any Minecraft version that uses `MinecraftSkins`/`MinecraftCloaks` URLs.

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
