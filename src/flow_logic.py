import mitmproxy
import minecraft_api


def skin(username, flow, uuid_cache):
    uuid = minecraft_api.get_uuid(username, uuid_cache)

    textures = minecraft_api.get_profile_textures(uuid)

    skin = minecraft_api.get_skin(textures)

    flow.response = mitmproxy.http.Response.make(200, skin, {"Content-Type": "image/png"})


def cape(username, flow, uuid_cache):
    uuid = minecraft_api.get_uuid(username, uuid_cache)

    textures = minecraft_api.get_profile_textures(uuid)

    cape = minecraft_api.get_cape(textures)

    if cape:
        flow.response = mitmproxy.http.Response.make(200, cape, {"Content-Type": "image/png"})
    else:
        flow.response = mitmproxy.http.Response.make(404)
