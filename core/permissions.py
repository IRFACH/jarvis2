PERMISSIONS = {
    "open_app": True,
    "gps": False,
    "camera": False,
    "send_message": False
}

def has_permission(action):
    return PERMISSIONS.get(action, False)

def grant_permission(action):
    PERMISSIONS[action] = True
