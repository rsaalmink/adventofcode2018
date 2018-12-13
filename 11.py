import sys
import time

class Memoize:
	def __init__(self, fn):
		self.fn = fn
		self.memoize = {}

	def __call__(self, *args):
		if args not in self.memoize:
			self.memoize[args] = self.fn(*args)
		return self.memoize[args]

# no need to keep recalculating
@Memoize
def level(x, y):
	return ((((x+10)*y + my_serial)*(x+10)) // 100) % 10 - 5

grid_cache = {}
def power_level_grid(x,y,size):
	# optimization: if we know the value from x,y with a grid of size-1*size-1, we can add the last row/column to that to get the power level of size*size.
	if (x, y, size-1) in grid_cache:
		power = grid_cache[(x, y, size-1)]
		for i in range(size-1):
			power += level(x+size-1,y+i)
			power += level(x+i,y+size-1)
		power += level(x+size-1, y+size-1)
		grid_cache[(x, y, size)] = power
		return power
	else:
		grid_cache[(x, y, size)] = sum([level(x+k, y+l,) for k in range(size) for l in range(size)])
	return grid_cache[(x, y, size)] 

# Ok, my optimization is quite limited, should have used summed area table..

my_serial = 3214
field_size = 300

# # part 1
# min_size, max_size = 3, 3
# part 2
min_size, max_size = 1, 300

start_time = time.time()
best, best_size, indices = -sys.maxsize, -sys.maxsize, (-1,-1)
for size in range(min_size, max_size+1):
	for i in range(1,field_size-size+1):
		for j in range(1,field_size-size+1):
			power = power_level_grid(i,j,size)
			if power > best:
				best, best_size, indices = power, size, (i,j)
				print("New best:", best, best_size, indices)
	print(str(int(time.time() - start_time))+'s: ', size, i, i*i, i*i*size*size)
print(best, best_size, indices)