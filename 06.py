from collections import defaultdict
import sys 

data = [ (194, 200), (299, 244), (269, 329), (292, 55), (211, 63), (123, 311), (212, 90), (292, 169), (359, 177), (354, 95), (101, 47), (95, 79), (95, 287), (294, 126), (81, 267), (330, 78), (202, 165), (225, 178), (266, 272), (351, 326), (180, 62), (102, 178), (151, 101), (343, 145), (205, 312), (74, 193), (221, 56), (89, 89), (242, 172), (59, 138), (83, 179), (223, 88), (297, 234), (147, 351), (226, 320), (358, 338), (321, 172), (54, 122), (263, 165), (126, 341), (64, 132), (264, 306), (72, 202), (98, 49), (238, 67), (310, 303), (277, 281), (222, 318), (357, 169), (123, 225)]

# bounding box for determining all relevant points
minx = min([x for x,y in data])
miny = min([y for x,y in data])
maxx = max([x for x,y in data])
maxy = max([y for x,y in data])

def manhatten_distance(x,y):
	return abs(x[0] - y[0]) + abs(x[1] - y[1])

def part_1():
	point_to_coordinates = defaultdict(list)
	for x in range(minx, maxx+1):
		for y in range(miny, maxy+1):
			min_distance, tied = sys.maxsize, False
			for point_id, coordinate in enumerate(data):
				distance = manhatten_distance(coordinate, (x,y))
				if distance == min_distance:
					tied = True
				if distance < min_distance:
					min_distance = distance
					p = point_id 
					tied = False
			if not tied:
				point_to_coordinates[p].append((x,y))

	largest_area, the_point = -1, None
	for point in point_to_coordinates:
		# ignore any point that reside on the bbox' edges, they are infinite
		if not any((1 for x,y in point_to_coordinates[point] if x == minx or x == maxx or y == miny or y == maxy)):
			point_size = len(point_to_coordinates[point])
			if point_size > largest_area:
				largest_area = point_size
	print(largest_area)


def part_2():
	print(sum((1 for x in range(minx, maxx+1) for y in range(miny, maxy+1) if sum([manhatten_distance((x,y), coordinate) for coordinate in data]) < 10000)))

part_1()
part_2()