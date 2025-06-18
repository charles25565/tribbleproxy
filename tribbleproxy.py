import mitmproxy
import urllib.request

def request(flow: mitmproxy.http.HTTPFlow) -> None:
  USERNAME = flow.request.path.split("/")[-1].split(".png")[0]
  if flow.request.pretty_host == "s3.amazonaws.com" or flow.request.pretty_host == "skins.minecraft.net":
    if flow.request.path == "/MinecraftResources/":
      flow.response = mitmproxy.http.Response.make(404)
    elif flow.request.path == f"/MinecraftSkins/{USERNAME}.png":
      with urllib.request.urlopen(f"https://mineskin.eu/skin/{USERNAME}") as skin:
        flow.response = mitmproxy.http.Response.make(200, skin.read(), {"Content-Type": "image/png"})
    elif flow.request.path == f"/MinecraftCloaks/{USERNAME}.png":
      # TODO: Capes
      flow.response = mitmproxy.http.Response.make(404)
  elif flow.request.pretty_host == "www.minecraft.net":
    if flow.request.path.startswith("/game/joinserver.jsp"):
      flow.request.host = "session.minecraft.net"
  elif flow.request.pretty_host == "snoop.minecraft.net":
    flow.request.host = "snoop-minecraft-net.invalid"
  elif flow.request.pretty_host == "assets.minecraft.net":
    if flow.request.path == "/1_6_has_been_released.flag":
      flow.response = mitmproxy.http.Response.make(404)
  else:
    flow.kill()
