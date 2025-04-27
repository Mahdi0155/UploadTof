import json
import os

CHANNELS_FILE = "database/channels.json"

def load_channels():
    if not os.path.exists(CHANNELS_FILE):
        return []
    with open(CHANNELS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_channels(channels):
    with open(CHANNELS_FILE, "w", encoding="utf-8") as f:
        json.dump(channels, f, ensure_ascii=False, indent=4)

def add_channel(channel_id):
    channels = load_channels()
    if channel_id not in channels:
        channels.append(channel_id)
        save_channels(channels)
        return True
    return False

def remove_channel(channel_id):
    channels = load_channels()
    if channel_id in channels:
        channels.remove(channel_id)
        save_channels(channels)
        return True
    return False
