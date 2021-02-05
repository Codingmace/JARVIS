from datetime import datetime, timedelta
for a in range(0,10):
    d = datetime.today() - timedelta(days=a)
    print(d.strftime("%Y-%m-%d"))
