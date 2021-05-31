from typing import List

def calculate_span(price:list):
	sp = [1]
	st_queue = [0]

	for i in range(1,len(price)):

		while len(st_queue) > 0 and price[st_queue[-1]] <= price[i]:
			st_queue.pop()
		sp_price = 1 + i if len(st_queue) <= 0 else i - st_queue[-1]
		sp.append(sp_price)
		st_queue.append(i)
	return sp


if __name__ == '__main__':
	arr = [10, 4, 5, 90, 120, 80]
	sp = calculate_span(arr)
	print(sp)