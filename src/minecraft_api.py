# Copyright 2025 Charles

import urllib.request
import urllib.parse
import json
import base64


def get_uuid(username, uuid_cache):
    username = urllib.parse.quote(username)

    # Yes, a TTL could work but that is not a complete solution, simply making the solution apply slightly faster
    if username in uuid_cache:
        return uuid_cache[username]

    try:
        with urllib.request.urlopen(f"https://api.minecraftservices.com/minecraft/profile/lookup/name/{username}") as response:
            uuid = json.loads(response.read())["id"]
            if len(uuid_cache) >= 128:  # Prevent a DoS
                uuid_cache.clear()
            uuid_cache[username] = uuid
            return uuid
    except KeyError:
        return "c06f89064c8a49119c29ea1dbd1aab82"  # MHF_Steve


def get_profile_textures(uuid):
    with urllib.request.urlopen(f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid}") as response:
        textures = json.loads(base64.b64decode(json.loads(response.read())["properties"][0]["value"]))
        return textures["textures"]


def get_skin(textures):
    with urllib.request.urlopen(textures["SKIN"]["url"]) as response:
        return response.read()


def get_cape(textures):
    try:
        with urllib.request.urlopen(textures["CAPE"]["url"]) as response:
            return response.read()

    except KeyError:
        return None
