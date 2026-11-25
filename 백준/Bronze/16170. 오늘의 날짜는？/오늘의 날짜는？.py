from datetime import datetime, timezone

# UTC 기준 현재 시각 가져오기
utc_now = datetime.now(timezone.utc)

print(utc_now.year)
print(utc_now.month)
print(utc_now.day)