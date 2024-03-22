T = int(input())
station_dict = {}
for _ in range(T):
    train_name = input()
    station_dict[train_name] = {}
    N = int(input())
    for _ in range(N):
        comaprtment, passengers = input().split(",")
        station_dict[train_name][comaprtment] = int(passengers)
