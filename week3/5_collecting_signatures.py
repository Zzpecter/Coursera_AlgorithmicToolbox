# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021

def optimal_points(segments, touched):
    # go through the first range, see how many intersections you get at each point, choose the max.
    # create a bool list for storing the touched segments

    max_touched = 0
    for i in range(segments[0]):
        num_touched = 0
        for segment in segments[1:]:
            if i in range(segment):
                num_touched += 1
        max_touched = num_touched if num_touched > max_touched else max_touched

if __name__ == '__main__':
    num_segments = int(input())
    segments = []

    for s in range(num_segments):
        line = input().split()
        segments.append(tuple(int(line[0]), int(line[1])))

    touched = [False] * len(segments)

    points = optimal_points(segments, touched)