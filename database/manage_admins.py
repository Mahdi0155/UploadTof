import os
import json
from config import OWNER_ID, ADMIN_FILE

def _load_admins():
    if not os.path.exists(ADMIN_FILE):
        return []
    with open(ADMIN_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def _save_admins(admins):
    with open(ADMIN_FILE, "w") as f:
        json.dump(admins, f)

def is_owner(user_id):
    return str(user_id) == str(OWNER_ID)

def add_admin(admin_id):
    admins = _load_admins()
    if admin_id not in admins:
        admins.append(admin_id)
        _save_admins(admins)
        return True
    return False
