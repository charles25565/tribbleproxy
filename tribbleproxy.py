import mitmproxy
import urllib.request
import json
import base64

_uuid_cache = {}

def _get_uuid(username):
  if username in _uuid_cache:
    return _uuid_cache[username]
  with urllib.request.urlopen(f"https://api.minecraftservices.com/minecraft/profile/lookup/name/{username}") as response:
    uuid = json.loads(response.read())["id"]
    _uuid_cache[username] = uuid
    return uuid

def _get_profile_textures(uuid):
  with urllib.request.urlopen(f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid}") as response:
    textures = json.loads(base64.b64decode(json.loads(response.read())["properties"][0]["value"]))
    return textures["textures"]

def _get_skin(textures):
  with urllib.request.urlopen(textures["SKIN"]["url"]) as response:
    return response.read()

def _get_cape(textures):
  try:
    with urllib.request.urlopen(textures["CAPE"]["url"]) as response:
      return response.read()
      
  except KeyError:
    return None

def request(flow: mitmproxy.http.HTTPFlow):
  if flow.request.path.startswith("/cloak/get.jsp"):
    username = flow.request.path.split("?user=")[-1]
  else:
    username = flow.request.path.split("/")[-1].split(".png")[0]

  if flow.request.pretty_host == "s3.amazonaws.com" or flow.request.pretty_host == "skins.minecraft.net":
    if flow.request.path == "/MinecraftResources/":
      flow.response = mitmproxy.http.Response.make(404)
      
    elif flow.request.path == f"/MinecraftSkins/{username}.png":
      uuid = _get_uuid(username)
      textures = _get_profile_textures(uuid)
      skin = _get_skin(textures)
      flow.response = mitmproxy.http.Response.make(200, skin, {"Content-Type": "image/png"})
      
    elif flow.request.path == f"/MinecraftCloaks/{username}.png":
      uuid = _get_uuid(username)
      textures = _get_profile_textures(uuid)
      cape = _get_cape(textures)
      if cape:
        flow.response = mitmproxy.http.Response.make(200, cape, {"Content-Type": "image/png"})
      else:
        flow.response = mitmproxy.http.Response.make(404)
        
  elif flow.request.pretty_host == "www.minecraft.net":
    if flow.request.path.startswith("/game/joinserver.jsp") or flow.request.path.startswith("/game/checkserver.jsp"):
      flow.request.host = "session.minecraft.net"
    elif flow.request.path == f"/skin/{username}.png":
      uuid = _get_uuid(username)
      textures = _get_profile_textures(uuid)
      skin = _get_skin(textures)
      flow.response = mitmproxy.http.Response.make(200, skin, {"Content-Type": "image/png"})
    elif flow.request.path.startswith("/cloak/get.jsp"):
      uuid = _get_uuid(username)
      textures = _get_profile_textures(uuid)
      cape = _get_cape(textures)
      if cape:
        flow.response = mitmproxy.http.Response.make(200, cape, {"Content-Type": "image/png"})
      else:
        flow.response = mitmproxy.http.Response.make(404)
      
  elif flow.request.pretty_host == "snoop.minecraft.net":
    flow.request.host = "snoop-minecraft-net.invalid"
    
  elif flow.request.pretty_host == "assets.minecraft.net":
    if flow.request.path == "/1_6_has_been_released.flag":
      flow.response = mitmproxy.http.Response.make(404)

  elif flow.request.pretty_host == "session.minecraft.net":
    pass
  
  else:
    flow.kill()
