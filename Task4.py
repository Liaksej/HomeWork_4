stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

for key, value in stats.items():
    if value == max(stats.values()):
        print(key)

x = max(stats, key=stats.get)
print(x)
