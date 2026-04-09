minutes = int(input())
hours = minutes // 60
mins = minutes % 60

if hours > 0:
    if hours == 1:
        print(f"{hours} hr {mins} minutes")
    else:
        print(f"{hours} hrs {mins} minutes")
else:
    print(f"{mins} minutes")