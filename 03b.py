#!/usr/bin/env python3

with open('03.txt', 'rt') as f:
    input_data = f.readlines()
    input_data = [x.strip() for x in input_data]


from collections import defaultdict, Counter



oxy_data = [(x, x) for x in input_data]
co2_data = [(x, x) for x in input_data]

while len(oxy_data) > 1:
    cnt = Counter()
    for num, remainder in oxy_data:
        cnt[remainder[0]] += 1
    stats = cnt.most_common()
    if len(stats) > 1 and stats[0][1] == stats[1][1]:
        keep = '1'
    else:
        keep = stats[0][0]
    oxy_data = [(num, remainder[1:]) for (num, remainder) in oxy_data if remainder[0] == keep]

while len(co2_data) > 1:
    cnt = Counter()
    for num, remainder in co2_data:
        cnt[remainder[0]] += 1
    stats = cnt.most_common()
    if len(stats) > 1 and stats[0][1] == stats[1][1]:
        keep = '0'
    else:
        keep = stats[1][0]
    co2_data = [(num, remainder[1:]) for (num, remainder) in co2_data if remainder[0] == keep]

oxy = int(oxy_data[0][0], 2)
co2 = int(co2_data[0][0], 2)

mul = oxy*co2
print(f"oxy = {oxy}, co2 = {co2}, mul = {mul}")

