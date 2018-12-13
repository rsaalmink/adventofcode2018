edges = [ ("B","K"), ("F","I"), ("T","U"), ("R","Z"), ("N","S"), ("X","Y"), ("I","Y"), ("K","L"), ("U","J"), ("G","L"), ("W","A"), ("H","Q"), ("M","L"), ("P","L"), ("L","A"), ("V","Y"), ("Q","Y"), ("Z","J"), ("O","D"), ("Y","A"), ("J","E"), ("A","E"), ("C","E"), ("D","E"), ("S","E"), ("B","R"), ("U","O"), ("X","I"), ("C","S"), ("O","S"), ("J","D"), ("O","E"), ("Z","O"), ("J","C"), ("P","Y"), ("X","S"), ("O","Y"), ("J","A"), ("H","C"), ("P","D"), ("Z","S"), ("T","Z"), ("Y","C"), ("X","H"), ("R","Y"), ("T","W"), ("L","O"), ("G","Z"), ("H","P"), ("I","U"), ("H","V"), ("N","Y"), ("Q","E"), ("H","D"), ("P","O"), ("T","I"), ("W","V"), ("K","M"), ("R","W"), ("B","T"), ("U","A"), ("N","H"), ("F","U"), ("Q","O"), ("Y","S"), ("V","O"), ("W","C"), ("Y","J"), ("T","V"), ("N","D"), ("U","Q"), ("A","C"), ("U","M"), ("Q","S"), ("P","V"), ("B","Z"), ("W","Q"), ("L","S"), ("I","P"), ("G","P"), ("L","C"), ("K","A"), ("D","S"), ("I","H"), ("R","M"), ("Q","D"), ("K","O"), ("I","C"), ("N","O"), ("R","X"), ("P","C"), ("B","Y"), ("G","E"), ("L","V"), ("W","Y"), ("C","D"), ("M","J"), ("F","N"), ("T","Q"), ("I","E"), ("A","D"), ("B","K"), ("F","I"), ("T","U"), ("R","Z"), ("N","S"), ("X","Y"), ("I","Y"), ("K","L"), ("U","J"), ("G","L"), ("W","A"), ("H","Q"), ("M","L"), ("P","L"), ("L","A"), ("V","Y"), ("Q","Y"), ("Z","J"), ("O","D"), ("Y","A"), ("J","E"), ("A","E"), ("C","E"), ("D","E"), ("S","E"), ("B","R"), ("U","O"), ("X","I"), ("C","S"), ("O","S"), ("J","D"), ("O","E"), ("Z","O"), ("J","C"), ("P","Y"), ("X","S"), ("O","Y"), ("J","A"), ("H","C"), ("P","D"), ("Z","S"), ("T","Z"), ("Y","C"), ("X","H"), ("R","Y"), ("T","W"), ("L","O"), ("G","Z"), ("H","P"), ("I","U"), ("H","V"), ("N","Y"), ("Q","E"), ("H","D"), ("P","O"), ("T","I"), ("W","V"), ("K","M"), ("R","W"), ("B","T"), ("U","A"), ("N","H"), ("F","U"), ("Q","O"), ("Y","S"), ("V","O"), ("W","C"), ("Y","J"), ("T","V"), ("N","D"), ("U","Q"), ("A","C"), ("U","M"), ("Q","S"), ("P","V"), ("B","Z"), ("W","Q"), ("L","S"), ("I","P"), ("G","P"), ("L","C"), ("K","A"), ("D","S"), ("I","H"), ("R","M"), ("Q","D"), ("K","O"), ("I","C"), ("N","O"), ("R","X"), ("P","C"), ("B","Y"), ("G","E"), ("L","V"), ("W","Y"), ("C","D"), ("M","J"), ("F","N"), ("T","Q"), ("I","E"), ("A","D")]


def next_step(vertices_to_visit, l):
	return [s for s in vertices_to_visit if all(y != s for (x, y) in l)]

def part_1():
	vertices_to_visit = set([s[0] for s in edges] + [s[1] for s in edges])

	result = ''
	while vertices_to_visit:
		# print(vertices_to_visit)
		vertices = list(next_step(vertices_to_visit, edges))
		vertices.sort()

		next_vertex = vertices[0]
		result += next_vertex
		vertices_to_visit.remove(next_vertex)
		edges = [(x, y) for (x, y) in edges if x != next_vertex]

	print(result)


def time_per_step(v):
	return ord(v) - 5


def part_2(edges):
	vertices_to_visit = set([s[0] for s in edges] + [s[1] for s in edges])

	seconds = 0
	num_elves = 5

	#for every elf, keep track of time left to spend and the vertex it is working on.
	elf_time_vertex = {}
	for i in range(num_elves):
		elf_time_vertex[i] = (0, None)

	while vertices_to_visit:
		next_vertices_to_proces = list(next_step(vertices_to_visit, edges))

		# if all elves are busy working, fast forward to next point in time of one elf hitting 1
		fastforward = max(1, min([elf_time_vertex[i][0] for i in elf_time_vertex])-2)
		for i in range(num_elves):
			# decrease worktime for all elves
			print(i, elf_time_vertex[i], end=' ')
			elf_time_vertex[i] = (max(elf_time_vertex[i][0] - fastforward, 0), elf_time_vertex[i][1])
			if elf_time_vertex[i][0] == 0:			
				if elf_time_vertex[i][1] is not None:
					# mark this vetex as done
					edges = [(x,y) for (x,y) in edges if x != elf_time_vertex[i][1]]
				if next_vertices_to_proces:
					# assign it to this elf
					next_vertex = next_vertices_to_proces.pop(0)
					elf_time_vertex[i] = (time_per_step(next_vertex), next_vertex)
					vertices_to_visit.remove(next_vertex)
		print()
		seconds += 1
	# add remainin worktime
	print(seconds + max([elf_time_vertex[i][0] for i in elf_time_vertex]))

part_2(edges)