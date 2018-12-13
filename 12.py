# rules_test = [
# "...##",
# "..#..",
# ".#...",
# ".#.#.",
# ".#.##",
# ".##..",
# ".####",
# "#.#.#",
# "#.###",
# "##.#.",
# "##.##",
# "###..",
# "###.#",
# "####."
# ]


rules = [
"##.##", #
"..##.", #
"##...", #
"..#..", #
".###.", #
".#.#.", #
"#..##", #
".##.#", #
"#.###", #
".##..", #
"#.#.#", #
".#...", #
".#..#", #
"..#.#", #
"...#.", #
"####.", #
"###.." #
]

# part 1
# buffer = 25
# generations = 20
# next_state = list(buffer*"."+"#..#.#..##......###...###"+buffer*".")    # part 1


# part 2
buffer = 1000
generations = 1000
next_state = list(buffer*"."+"#......##...#.#.###.#.##..##.#.....##....#.#.##.##.#..#.##........####.###.###.##..#....#...###.##"+buffer*".")    # part_2

for generation in range(generations+1):
	state = next_state[:]
	print("".join(state))
	# next_state = state[:]
	first_pot = [i for i,pot in enumerate(state) if pot == '#'][0]
	for pot in range(len(state)):
		match ="".join(state[pot-2:pot+3])
		next_state[pot] = '#' if match in rules else '.'


	print(generation, sum([i-buffer for i,pot in enumerate(state) if pot == "#"]))

# found linear progression after a while. 
# 1000 = 76113
# 1001 = 76188
# 1002 = 76263

print((76188-76113)*(50000000000-1000)+76113)
