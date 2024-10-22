import json
import os
import django

# تنظیمات Django را آماده می‌کنیم
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SportClub.settings')
django.setup()

from players.models import Players

# مسیر به فایل JSON
json_file_path = '/home/sajjad/PycharmProjects/SportClub/players.json'

# بارگذاری داده‌های JSON
with open(json_file_path, 'r') as file:
    players_data = json.load(file)

# ایجاد اشیاء Player از داده‌ها
for player in players_data:
    Players.objects.create(
        name=player['name'],
        family=player['family'],
        age=player['age'],
        position=player['position'],
        img=player['img'],
        created=player['created'],
    )

print("بازیکنان با موفقیت وارد شدند!")
