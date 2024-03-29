import matplotlib.pyplot as plt
from random_walk import RandomWalk

#keep making walks as long as program remains active
while True:
	#make random walk & plot points 
	rw = RandomWalk(50000)
	rw.fill_walk()

	#set size of plotting window
	plt.figure(figsize=(10,6))

	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
				cmap=plt.cm.Blues, edgecolor='none', s=1)
	
	#emphasize first & last points
	plt.scatter(0, 0, c='green', edgecolors='none', s=10)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
					edgecolors='none', s=10)

	plt.axis("off")

	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break
