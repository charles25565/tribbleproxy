# tribbleproxy

Tribbleproxy is a simple proxy that simulates the endpoints for skins and capes for old versions of Minecraft.

In theory it would work for any Minecraft version that uses the MinecraftSkins/MinecraftCloaks AWS S3 bucket.

## Example Configuration

Save this as `tribbleproxy.properties`.

```json
{
  "username": "charles25565",
  "skin": "skin.png",
  "cape": "cape.png"
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
