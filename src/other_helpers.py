import urllib.parse


def get_username(flow):
    try:
        if flow.request.path.startswith("/cloak/get.jsp"):
            username = flow.request.path.split("?user=")[-1]
        else:
            username = flow.request.path.split("/")[-1].split(".png")[0]
        username = urllib.parse.unquote(username)
    except IndexError:
        return "MHF_Steve"
    return username
