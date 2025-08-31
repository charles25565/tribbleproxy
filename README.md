# Tribbleproxy

Tribbleproxy is a simple proxy that simulates various endpoints used in Minecraft: Java Edition between 2009 and 2013.

## Features

- :white_check_mark: Late Alpha through Beta 1.7.3 multiplayer authentication
- :white_check_mark: Skins
- :white_check_mark: Capes
- :white_check_mark: 1.6 update notification (spoofs as if it isn't out)
- :x: Snooper
- :x: Resources
- :x: Non Minecraft traffic

## Compatible versions

- Classic 0.0.18a onwards
- Indev
- Infdev
- Alpha
- Beta
- Releases until and including 1.5.2

## Example Command

```sh
podman run -p 8080:8080 \
  --rm \
  -ti quay.io/charles2/tribbleproxy:latest
```

## Example Usage

Add the following JVM arguments:

```
-Dhttp.proxyHost=localhost -Dhttp.proxyPort=8080
```
