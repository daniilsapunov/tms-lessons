time = int(input())
days = time // (3600 * 24)
time = time - days * 3600 * 24
hours = time // 3600
time = time - hours *3600
minutes = time // 60
time = time -minutes * 60
seconds = time  % 60

print(days,':',hours,':', minutes,':', seconds )