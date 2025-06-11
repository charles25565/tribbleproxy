import mitmproxy
import json

with open("tribbleproxy.properties", "r") as properties:
    DATA = json.load(properties)

def serve_image(flow: mitmproxy.http.HTTPFlow, resource_type: str) -> None:
    USERNAME = flow.request.path.split("/")[-1].split(".png")[0]
    try:
        filename = DATA[USERNAME][resource_type]
        with open(filename, "rb") as f:
            flow.response = mitmproxy.http.Response.make(
                200, f.read(), {"Content-Type": "image/png"}
            )
    except KeyError:
        flow.response = mitmproxy.http.Response.make(404, b"User not found")
    except FileNotFoundError:
        flow.response = mitmproxy.http.Response.make(500, f"{resource_type} file not found".encode())

def request(flow: mitmproxy.http.HTTPFlow) -> None:
    USERNAME = flow.request.path.split("/")[-1].split(".png")[0]
    if flow.request.host == "s3.amazonaws.com":
        if flow.request.path == f"/MinecraftSkins/{USERNAME}.png":
            serve_image(flow, "skin")
        elif flow.request.path == f"/MinecraftCloaks/{USERNAME}.png":
            serve_image(flow, "cape")
