# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021


def compute_min_refills(total_distance, car_autonomy, gas_stations, stops):
    next_stop = None
    route_progress = 0
    for gas_station in gas_stations:
        if gas_station > car_autonomy:
            break
        next_stop = gas_station
        route_progress += 1

    if next_stop is not None:
        gas_stations = gas_stations[route_progress:]
        gas_stations = [(gs - next_stop) for gs in gas_stations]
        stops += 1
        if gas_stations:
            return compute_min_refills(total_distance - next_stop, car_autonomy, gas_stations, stops)
    else:
        return -1
    return stops

if __name__ == '__main__':
    total_distance = int(input())
    car_autonomy = int(input())
    number_gas_stations = int(input())
    gas_stations = []

    line = input().split()
    for gs in line:
        gas_stations.append(int(gs))

    print(compute_min_refills(total_distance, car_autonomy, gas_stations, 0))
    # print(compute_min_refills(10, 3, [1, 2, 5, 9], 0))
