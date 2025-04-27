import json
from config import OWNER_ID

ADMINS_FILE = "database/admins.json"

def load_admins():
    try:
        with open(ADMINS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_admins(admins):
    with open(ADMINS_FILE, "w") as file:
        json.dump(admins, file)

def add_admin(admin_id: int) -> bool:
    admins = load_admins()
    if admin_id not in admins:
        admins.append(admin_id)
        save_admins(admins)
        return True
    return False

def is_owner(user_id: int) -> bool:
    return user_id == OWNER_ID
