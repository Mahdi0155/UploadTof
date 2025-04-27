import os
import json
SUBS_FILE = "subscriptions.json"

def _load_subs():
    if not os.path.exists(SUBS_FILE):
        return []
    with open(SUBS_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def _save_subs(subs):
    with open(SUBS_FILE, "w") as f:
        json.dump(subs, f)

async def add_subscription_channel(channel_id):
    subs = _load_subs()
    if channel_id not in subs:
        subs.append(channel_id)
        _save_subs(subs)
        return True
    return False

async def remove_subscription_channel(channel_id):
    subs = _load_subs()
    if channel_id in subs:
        subs.remove(channel_id)
        _save_subs(subs)
        return True
    return False

async def get_subscription_channels():
    return _load_subs()
