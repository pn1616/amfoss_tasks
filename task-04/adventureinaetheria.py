n = int(input())
travel_times = list(map(int, input().split()))

min_time = min(travel_times)
count_min_time = travel_times.count(min_time)

if count_min_time > 1:
    print("Still Aetheria")
else:
    towntogo = travel_times.index(min_time) + 1
    print(towntogo)
