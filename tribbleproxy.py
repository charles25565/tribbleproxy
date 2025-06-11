from mitmproxy import http
from json import load
with open("tribbleproxy.properties") as properties:
  USERNAME = load(properties)["username"]
  SKIN = load(properties)["skin"]
  CAPE = load(properties)["cape"]
def response(flow: http.HTTPFlow) -> None:
  global USERNAME, SKIN, CAPE
  if flow.request.host == "s3.amazonaws.com" && flow.request.path == f"/MinecraftSkins/{USERNAME}.png":
    with open(SKIN, "rb") as skin:
      flow.response.content = skin.read()
      flow.response.status_code = 200
  if flow.request.host == "s3.amazonaws.com" && flow.request.path == f"/MinecraftCloaks/{USERNAME}.png":
    with open(CAPE, "rb") as cape:
      flow.response.content = cape.read()
      flow.response.status_code = 200
