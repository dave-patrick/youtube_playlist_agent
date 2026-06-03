import sqlite3

conn = sqlite3.connect('/home/ubuntu/youtube_playlist_agent/db.sqlite')
conn.row_factory = sqlite3.Row
rules = conn.execute("SELECT * FROM user_rules WHERE user_id = 1 AND (target_category LIKE '%Tana%' OR channel_name LIKE '%Tana%')").fetchall()
conn.close()

print(f"Total Tana rules: {len(rules)}")
for r in rules:
    print(f"  {r['channel_name']} -> {r['target_category']}")
