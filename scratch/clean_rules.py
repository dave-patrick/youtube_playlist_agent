import sqlite3
import os

channels_to_remove = [
    "Adam Savage’s Tested",
    "Adobe Creative Cloud",
    "Adult Swim",
    "Adult Swim Europe",
    "Bad Lip Reading",
    "Corridor Digital",
    "Dropout",
    "Giant Freakin Robot",
    "How It Should Have Ended",
    "How To Drink",
    "IGN",
    "Industrial Light & Magic",
    "Inside the Magic",
    "Mitch Peacock • Designer Woodworker",
    "Mohawk Designs Off-Road",
    "Nerdist",
    "PostmodernJukebox",
    "Rob Landes",
    "RocketJump",
    "Rotten Tomatoes TV",
    "Rotten Tomatoes Trailers",
    "Saturday Night Live",
    "Screen Junkies",
    "Spencley Design Co.",
    "Syd Wilder",
    "Taylor Davis",
    "devinsupertramp",
    "eXquisite Gaming",
    "fxguide",
    "mouseinfo",
    "Kuma Films",
    "MagicofRahat"
]

# 1. Clean local and VM text file
def clean_text_file(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    new_lines = []
    removed_count = 0
    to_remove_lower = [c.lower() for c in channels_to_remove]
    
    for line in lines:
        if ":" in line:
            parts = line.split(":", 1)
            ch = parts[0].strip().lower()
            if ch in to_remove_lower:
                removed_count += 1
                continue
        new_lines.append(line)
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print(f"Cleaned {filepath}: Removed {removed_count} channel rules.")

# Clean local file
clean_text_file("yt_category_channel_map.txt")

# 2. Clean SQLite DB
db_path = "/home/ubuntu/youtube_playlist_agent/db.sqlite"
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    placeholders = ",".join("?" for _ in channels_to_remove)
    cursor.execute(f"DELETE FROM user_rules WHERE user_id = 1 AND channel_name IN ({placeholders})", channels_to_remove)
    deleted_db = cursor.rowcount
    conn.commit()
    conn.close()
    print(f"Deleted {deleted_db} rules from SQLite user_rules table for user 1.")
else:
    # If run locally, clean local db if exists
    if os.path.exists("db.sqlite"):
        conn = sqlite3.connect("db.sqlite")
        cursor = conn.cursor()
        placeholders = ",".join("?" for _ in channels_to_remove)
        cursor.execute(f"DELETE FROM user_rules WHERE channel_name IN ({placeholders})", channels_to_remove)
        deleted_db = cursor.rowcount
        conn.commit()
        conn.close()
        print(f"Deleted {deleted_db} rules from local SQLite.")
