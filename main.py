n = int(input())
while n!=0:
    name = str(input())
    n-=1
    if "Кот" in name or "кот" in name:

        print("МЯУ")
    else:
        print("НЕТ")