with open('health.json') as file:
    total = sum(1 for line in file.readlines() if 'instances' in line)