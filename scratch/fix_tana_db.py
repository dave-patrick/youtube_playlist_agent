import sqlite3

conn = sqlite3.connect('/home/ubuntu/youtube_playlist_agent/db.sqlite')
cursor = conn.cursor()

# Update Tana channels to map to Tana category
cursor.execute("UPDATE user_rules SET target_category = 'Tana' WHERE user_id = 1 AND channel_name IN ('Tana', 'Tana Central')")
updated = cursor.rowcount
conn.commit()
conn.close()

print(f"Updated {updated} rules in the DB.")
