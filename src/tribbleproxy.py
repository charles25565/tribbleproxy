import mitmproxy
import other_helpers
import flow_logic

# Mojang's servers have extremely heavy ratelimits for UUID requests
_uuid_cache = {}


def request(flow):
    username = other_helpers.get_username(flow)

    if flow.request.pretty_host in ("s3.amazonaws.com", "skins.minecraft.net"):
        if flow.request.path == "/MinecraftResources/":
            flow.response = mitmproxy.http.Response.make(404)

        elif flow.request.path == f"/MinecraftSkins/{username}.png":
            flow_logic.skin(username, flow, _uuid_cache)

        elif flow.request.path == f"/MinecraftCloaks/{username}.png":
            flow_logic.cape(username, flow, _uuid_cache)

    elif flow.request.pretty_host == "www.minecraft.net":
        if flow.request.path.startswith("/game/joinserver.jsp") or flow.request.path.startswith("/game/checkserver.jsp"):
            flow.request.host = "session.minecraft.net"

        elif flow.request.path == f"/skin/{username}.png":
            flow_logic.skin(username, flow, _uuid_cache)

        elif flow.request.path.startswith("/cloak/get.jsp"):
            flow_logic.cape(username, flow, _uuid_cache)

    elif flow.request.pretty_host == "snoop.minecraft.net":
        flow.kill()  # Disable telemetry

    elif flow.request.pretty_host == "assets.minecraft.net":
        if flow.request.path == "/1_6_has_been_released.flag":
            flow.response = mitmproxy.http.Response.make(404)

    elif flow.request.pretty_host == "session.minecraft.net":
        pass

    else:
        flow.kill()  # Prevents the proxy from being used for general traffic
