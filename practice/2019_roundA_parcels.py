def distance(p1, p2):
	(r1, c1), (r2, c2) = p1, p2
	return abs(r1-r2) + abs(c1-c2)

def del_time(p, arr):
	min_dist = distance(p,arr[0])
	for q in range(1,len(arr)):
		dist = distance(p,arr[q])
		if dist < min_dist:
			min_dist = dist
	return min_dist

def solve():
	t = int(input())
	for i in range(1, t+1):
		r,c = [int(s) for s in input().split(' ')]
		matrix = []
		offices = []
		for x in range(0,r):
			row = []
			for y, s in enumerate(list(input())):
				row.append(int(s))
				if s == '1':
					offices.append((x,y))
			matrix.append(row)

		office_count = len(offices)
		if office_count > 0:
			max_distance = 0
			max_p = [(0, 0)]
			for x in range(0,r):
				for y in range(0,c):
					if matrix[x][y] == 0:
						p = (x,y)
						d = del_time(p,offices)
						if d > max_distance:
							max_distance = d
							max_p = [p]
						elif d == max_distance:
							max_p.append(p)
						else:
							pass
		else:
			max_p = (r//2, c//2)
		
		# print("cur_max = {}".format(max_distance))
		global_max_distance = 0
		total = r*c
		if office_count != total:
			if type(max_p) != list:
				max_p = [max_p]
			for m in max_p:
				offices.append(m)
				matrix[m[0]][m[1]] = 1
				max_distance = 0
				for x in range(0,r):
					for y in range(0,c):
						if matrix[x][y] == 0:
							p = (x,y)
							d = del_time(p,offices)
							if d > max_distance:
								max_distance = d
				if max_distance > global_max_distance:
					global_max_distance = max_distance
				
		print("Case #{}: {}".format(i,global_max_distance))

if __name__ == "__main__":
	solve()
