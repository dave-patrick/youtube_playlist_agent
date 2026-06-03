import json
import collections
import sqlite3

# 1. Read db
conn = sqlite3.connect('/home/ubuntu/youtube_playlist_agent/db.sqlite')
conn.row_factory = sqlite3.Row
rules = conn.execute('SELECT * FROM user_rules').fetchall()
conn.close()

print(f"Total DB user rules: {len(rules)}")
for r in rules[:30]:
    print(f"  {r['channel_name']} -> {r['target_category']}")

# 2. Read maintenance actions
with open('/home/ubuntu/youtube_playlist_agent/maintenance_actions_1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"\nTotal actions: {len(data)}")

# Let's inspect duplicate items where it wants to keep in Star Wars
star_wars_dups = [x for x in data if x.get('type') in ['DUPLICATE', 'DUPLICATE_NO_TARGET'] and x.get('keep') == 'Star Wars']
print(f"\nStar Wars Duplicates to Keep ({len(star_wars_dups)}):")
for idx, d in enumerate(star_wars_dups[:10]):
    print(f"  [{idx+1}] {d['title']} (Channel: {d.get('channel')})")
    print(f"      Remove from: {d.get('remove')}")

# Let's inspect misplaced items going to Star Wars
star_wars_misplaced = [x for x in data if x.get('type') == 'MISPLACED' and x.get('to') == 'Star Wars']
print(f"\nStar Wars Misplaced going to Star Wars ({len(star_wars_misplaced)}):")
for idx, m in enumerate(star_wars_misplaced[:10]):
    print(f"  [{idx+1}] {m['title']} (Channel: {m.get('channel')})")
    print(f"      From: {m.get('from')}")
