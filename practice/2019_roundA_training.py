def solve():
	t = int(input())
	for i in range(1, t+1):
		n,p = [int(s) for s in input().split(' ')]
		students = []
		students.extend([int(s) for s in input().split(' ')])
		students.sort(reverse=True)

		# Calculate
		remain = p - 1
		j = 0
		k = j + p - 1
		arr_sum = sum(students[j+1:k+1])
		min_hours = (students[j] * remain) - arr_sum
		j += 1
		k += 1

		while k < n:
			arr_sum -= students[j]
			arr_sum += students[k]
			hours = (students[j] * remain) - arr_sum
			if hours < min_hours:
				min_hours = hours
			if min_hours == 0:
				break
			j += 1
			k += 1

		print("Case #{}: {}".format(i, min_hours))

if __name__ == "__main__":
	solve()
