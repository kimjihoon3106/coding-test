from datetime import datetime, timezone

time = datetime.now(timezone.utc)

print(time.strftime("%Y-%m-%d"))