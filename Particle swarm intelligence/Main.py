from Parameters import *
from StanderdPSO import StanderdPSO
from math import cos, pi, sqrt, sin, exp
from function_display import display_func, swarm_particle_figure_surface, swarm_particle_figure_contour, animation, \
	compare_between_deffirent_c1, compare_between_deffirent_c2
from Particle import Particle
import plotly.graph_objects as go
import numpy as np
from random import uniform

bounds1 = [(-100, 100), (-100, 100)]


def BOHACHEVSKY_FUNCTIONS(x, y):
	return x ** 2 + 2 * y ** 2 - 0.3 * cos(3 * pi * x) - 0.4 * cos(4 * pi * y) + 0.7


bounds2 = [(-5.12, 5.12), (-5.12, 5.12)]


def DROP_WAVE_FUNCTION(x, y):
	return -1 * (1 + cos(12 * sqrt(x ** 2 + y ** 2))) / (0.5 * (x ** 2 + y ** 2) + 2)


bounds3 = [(-512, 512), (-512, 512)]


def EGGHOLDER_FUNCTION(x, y):
	return (-1 * (y + 47) * sin(sqrt(np.linalg.norm(y + (x / 2) + 47)))) - (x * sin(sqrt(np.linalg.norm(x - (y + 47)))))


bounds4 = [(-10, 10), (-10, 10)]


def BOOTH_FUNCTION(x, y):
	return (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2


bounds5 = [(-32.768, 32.768), (-32.768, 32.768)]


def ACKLEY_FUNCTION(x, y):
	arr_np = np.array([x, y])
	n = len(arr_np)
	a = 20
	b = 0.2
	c = 2 * np.pi
	term1 = -a * np.exp(-b * np.sqrt(np.sum(arr_np ** 2) / n))
	term2 = -np.exp(np.sum(np.cos(c * arr_np)) / n)
	return term1 + term2 + a + np.e


bounds6 = [(-5.12, 5.12), (-5.12, 5.12)]


def RASTRIGIN_FUNCTION(x, y):
	return (10 * 2) + (x ** 2 - 10 * cos(2 * pi * x)) + (y ** 2 - 10 * cos(2 * pi * y))


bounds7 = [(-5.12, 5.12), (-5.12, 5.12)]


def SPHERE_FUNCTION(x, y):
	return x ** 2 + y ** 2


seeds = [x for x in range(42, 72)]

"""
if __name__ == '__main__':
	display_func(ACKLEY_FUNCTION, bounds5[0][0], bounds5[0][1], "ACKLEY_FUNCTION")

	seeds = [x for x in range(42, 72)]

	global_bests1 = []
	fitness_global_bests1 = []
	Globals_over_runs1 = []
	for i in seeds:
		np.random.seed(i)

		Pso_algorithm = StanderdPSO(ACKLEY_FUNCTION, bounds5, particle_size, iterations, Particle.MINIMIZATION,
									theta,
									c1, c2)

		swarm_particle: list[Particle] = Pso_algorithm.generate_swarm()

		# test(swarm_particle,BOHACHEVSKY_FUNCTIONS)

		# swarm_particle_figure_surface(EGGHOLDER_FUNCTION, bounds3[0][0], bounds3[0][1], swarm_particle)
		# swarm_particle_figure_contour(EGGHOLDER_FUNCTION, bounds3[0][0], bounds3[0][1], swarm_particle)

		global_best_position, fitness_global_best_position, Globals, particles = Pso_algorithm.compute()

		global_bests1.append(global_best_position)
		fitness_global_bests1.append(fitness_global_best_position)
		Globals_over_runs1.append(Globals)

	global_bests2 = []
	fitness_global_bests2 = []
	Globals_over_runs2 = []
	for i in seeds:
		np.random.seed(i)

		Pso_algorithm = StanderdPSO(RASTRIGIN_FUNCTION, bounds6, particle_size, iterations, Particle.MINIMIZATION,
									theta,
									c1, c2)

		swarm_particle: list[Particle] = Pso_algorithm.generate_swarm()

		# test(swarm_particle,BOHACHEVSKY_FUNCTIONS)

		# swarm_particle_figure_surface(EGGHOLDER_FUNCTION, bounds3[0][0], bounds3[0][1], swarm_particle)
		# swarm_particle_figure_contour(EGGHOLDER_FUNCTION, bounds3[0][0], bounds3[0][1], swarm_particle)

		global_best_position, fitness_global_best_position, Globals, particles = Pso_algorithm.compute()

		global_bests2.append(global_best_position)
		fitness_global_bests2.append(fitness_global_best_position)
		Globals_over_runs2.append(Globals)

	global_bests3 = []
	fitness_global_bests3 = []
	Globals_over_runs3 = []
	for i in seeds:
		np.random.seed(i)

		Pso_algorithm = StanderdPSO(SPHERE_FUNCTION, bounds7, particle_size, iterations, Particle.MINIMIZATION,
									theta,
									c1, c2)

		swarm_particle: list[Particle] = Pso_algorithm.generate_swarm()

		# test(swarm_particle,BOHACHEVSKY_FUNCTIONS)

		# swarm_particle_figure_surface(EGGHOLDER_FUNCTION, bounds3[0][0], bounds3[0][1], swarm_particle)
		# swarm_particle_figure_contour(EGGHOLDER_FUNCTION, bounds3[0][0], bounds3[0][1], swarm_particle)

		global_best_position, fitness_global_best_position, Globals, particles = Pso_algorithm.compute()

		global_bests3.append(global_best_position)
		fitness_global_bests3.append(fitness_global_best_position)
		Globals_over_runs3.append(Globals)

	# animation(EGGHOLDER_FUNCTION, particles, bounds3[0][0], bounds3[0][1])

	# print(
	# f"The best position founded for {iterations} iterations are ({round(global_best_position[0], 3)}, {round(global_best_position[1], 3)})")
	# print(f"The best fitness found is {round(fitness_global_best_position, 3)}")

	# fig = go.Figure(
	# data=go.Scatter(x=list(range(1, iterations + 1)), y=Globals, mode="lines+markers"))
	# fig.update_layout(title='Convergence Plot', xaxis_title='Iteration', yaxis_title='Best Fitness')
	# fig.show()

	array_avrage_position1 = np.array(global_bests1)
	xs1 = []
	ys1 = []
	for position in array_avrage_position1:
		xs1.append(position[0])
		ys1.append(position[1])

	avarge_x1 = np.mean(xs1)
	avarge_y1 = np.mean(ys1)

	avarage_position1 = (avarge_x1, avarge_y1)

	avarage_fitness1 = np.array(fitness_global_bests1).mean()

	sum1 = [0] * iterations
	result_of_avarages1 = [0] * iterations
	for run in Globals_over_runs1:
		for i in range(len(run)):
			sum1[i] += run[i]
	j = 0
	for j in range(iterations):
		result_of_avarages1[j] = sum1[j] / len(seeds)

	print(
		f"the mean best point for ACKLEY_FUNCTION is ({avarage_position1})")
	print(f"the avarage of best fittness for ACKLEY_FUNCTION is {avarage_fitness1}")

	array_avrage_position2 = np.array(global_bests2)
	xs2 = []
	ys2 = []
	for position in array_avrage_position2:
		xs2.append(position[0])
		ys2.append(position[1])

	avarge_x2 = np.mean(xs2)
	avarge_y2 = np.mean(ys2)

	avarage_position2 = (avarge_x2, avarge_y2)

	avarage_fitness2 = np.array(fitness_global_bests2).mean()

	sum2 = [0] * iterations
	result_of_avarages2 = [0] * iterations
	for run in Globals_over_runs2:
		for i in range(len(run)):
			sum2[i] += run[i]
	j = 0
	for j in range(iterations):
		result_of_avarages2[j] = sum2[j] / len(seeds)

	print(
		f"the mean best point for RASTRIGIN_FUNCTION is ({avarage_position2})")
	print(f"the avarage of best fittness for RASTRIGIN_FUNCTION is {avarage_fitness2}")

	array_avrage_position3 = np.array(global_bests3)
	xs3 = []
	ys3 = []
	for position in array_avrage_position3:
		xs3.append(position[0])
		ys3.append(position[1])

	avarge_x3 = np.mean(xs3)
	avarge_y3 = np.mean(ys3)

	avarage_position3 = (avarge_x3, avarge_y3)

	avarage_fitness3 = np.array(fitness_global_bests3).mean()

	sum3 = [0] * iterations
	result_of_avarages3 = [0] * iterations
	for run in Globals_over_runs3:
		for i in range(len(run)):
			sum3[i] += run[i]
	j = 0
	for j in range(iterations):
		result_of_avarages3[j] = sum3[j] / len(seeds)

	print(
		f"the mean best point for SPHERE_FUNCTION is (f{avarage_position3})")
	print(f"the avarage of best fittness for SPHERE_FUNCTION is {avarage_fitness3}")

	avarges = [result_of_avarages1, result_of_avarages2, result_of_avarages3]
	functions = ["ACKLEY_FUNCTION", "RASTRIGIN_FUNCTION", "SPHERE_FUNCTION"]

	fig = go.Figure()

	for i in range(len(avarges)):
		fig.add_trace(
			go.Scatter(x=list(range(1, iterations + 1)), y=avarges[i], mode="lines+markers", name=f"{functions[i]}"))

	fig.update_layout(title='avarage fitness of 3 functions', xaxis_title='Iteration', yaxis_title='Best Fitness')
	fig.show()

	# analysis
	# Comparing between c1 and c2

	"""
"""
avarges = []
Globals_0_run = []
for i in seeds:
	np.random.seed(i)
	Pso_algorithm_with_deffirent_c1_0 = StanderdPSO(ACKLEY_FUNCTION, bounds5, particle_size, iterations,
													Particle.MINIMIZATION, theta,  # NOQA
													c1=0, c2=2)  # NOQA

	_ = Pso_algorithm_with_deffirent_c1_0.generate_swarm()

	_, _, Globals0, _ = Pso_algorithm_with_deffirent_c1_0.compute()

	Globals_0_run.append(Globals0)
sum_elements_c1_0 = [sum(column) for column in zip(*Globals_0_run)]

avg_c1_0 = [0] * iterations
for j in range(iterations):
	avg_c1_0[j] = sum_elements_c1_0[j] / len(seeds)
avarges.append(avg_c1_0)

Globals_0_run = []
for i in seeds:
	np.random.seed(i)
	Pso_algorithm_with_deffirent_c1_0_4 = StanderdPSO(ACKLEY_FUNCTION, bounds5, particle_size, iterations,
													  Particle.MINIMIZATION, theta,  # NOQA
													  c1=0.4, c2=2)  # NOQA

	_ = Pso_algorithm_with_deffirent_c1_0_4.generate_swarm()

	_, _, Globals0, _ = Pso_algorithm_with_deffirent_c1_0_4.compute()

	Globals_0_run.append(Globals0)

sum_elements_c1_0_4 = [sum(column) for column in zip(*Globals_0_run)]

avg_c1_0_4 = [0] * iterations
for j in range(iterations):
	avg_c1_0_4[j] = sum_elements_c1_0_4[j] / len(seeds)

avarges.append(avg_c1_0_4)

Globals_0_run = []
for i in seeds:
	np.random.seed(i)
	Pso_algorithm_with_deffirent_c1_0_8 = StanderdPSO(ACKLEY_FUNCTION, bounds5, particle_size, iterations,
													  Particle.MINIMIZATION, theta,  # NOQA
													  c1=0.8, c2=2)  # NOQA

	_ = Pso_algorithm_with_deffirent_c1_0_8.generate_swarm()

	_, _, Globals0, _ = Pso_algorithm_with_deffirent_c1_0_8.compute()

	Globals_0_run.append(Globals0)

sum_elements_c1_0_8 = [sum(column) for column in zip(*Globals_0_run)]

avg_c1_0_8 = [0] * iterations
for j in range(iterations):
	avg_c1_0_8[j] = sum_elements_c1_0_8[j] / len(seeds)

avarges.append(avg_c1_0_8)

Globals_0_run = []
for i in seeds:
	np.random.seed(i)
	Pso_algorithm_with_deffirent_c1_1_2 = StanderdPSO(ACKLEY_FUNCTION, bounds5, particle_size, iterations,
													  Particle.MINIMIZATION, theta,  # NOQA
													  c1=1.2, c2=2)  # NOQA

	_ = Pso_algorithm_with_deffirent_c1_1_2.generate_swarm()

	_, _, Globals0, _ = Pso_algorithm_with_deffirent_c1_1_2.compute()

	Globals_0_run.append(Globals0)

sum_elements_c1_1_2 = [sum(column) for column in zip(*Globals_0_run)]

avg_c1_1_2 = [0] * iterations
for j in range(iterations):
	avg_c1_1_2[j] = sum_elements_c1_1_2[j] / len(seeds)

avarges.append(avg_c1_1_2)

Globals_0_run = []
for i in seeds:
	np.random.seed(i)
	Pso_algorithm_with_deffirent_c1_1_6 = StanderdPSO(ACKLEY_FUNCTION, bounds5, particle_size, iterations,
													  Particle.MINIMIZATION, theta,  # NOQA
													  c1=1.6, c2=2)  # NOQA

	_ = Pso_algorithm_with_deffirent_c1_1_6.generate_swarm()

	_, _, Globals0, _ = Pso_algorithm_with_deffirent_c1_1_6.compute()

	Globals_0_run.append(Globals0)

sum_elements_c1_1_6 = [sum(column) for column in zip(*Globals_0_run)]

avg_c1_1_6 = [0] * iterations
for j in range(iterations):
	avg_c1_1_6[j] = sum_elements_c1_1_6[j] / len(seeds)

avarges.append(avg_c1_1_6)

Globals_0_run = []
for i in seeds:
	np.random.seed(i)
	Pso_algorithm_with_deffirent_c1_2 = StanderdPSO(ACKLEY_FUNCTION, bounds5, particle_size, iterations,
													Particle.MINIMIZATION, theta,  # NOQA
													c1=2, c2=2)  # NOQA

	_ = Pso_algorithm_with_deffirent_c1_2.generate_swarm()

	_, _, Globals0, _ = Pso_algorithm_with_deffirent_c1_2.compute()

	Globals_0_run.append(Globals0)

sum_elements_c1_2 = [sum(column) for column in zip(*Globals_0_run)]

avg_c1_2 = [0] * iterations
for j in range(iterations):
	avg_c1_2[j] = sum_elements_c1_2[j] / len(seeds)

avarges.append(avg_c1_2)

compare_between_deffirent_c1(ACKLEY_FUNCTION, bounds5[0][0], bounds5[0][1], avarges, theta,
							 [0, 0.4, 0.8, 1.2, 1.6, 2], c2=2)

"""

"""
avarges2 = []
Globals_1_run = []
for i in seeds:
	np.random.seed(i)
	Pso_algorithm_with_deffirent_c2_0 = StanderdPSO(ACKLEY_FUNCTION, bounds5, particle_size, iterations,
													Particle.MINIMIZATION, theta,  # NOQA
													c1=2, c2=0)  # NOQA

	_ = Pso_algorithm_with_deffirent_c2_0.generate_swarm()

	_, _, Globals0, _ = Pso_algorithm_with_deffirent_c2_0.compute()

	Globals_1_run.append(Globals0)
sum_elements_c2_0 = [sum(column) for column in zip(*Globals_1_run)]

avg_c2_0 = [0] * iterations
for j in range(iterations):
	avg_c2_0[j] = sum_elements_c2_0[j] / len(seeds)
avarges2.append(avg_c2_0)

Globals_1_run = []
for i in seeds:
	np.random.seed(i)
	Pso_algorithm_with_deffirent_c2_0_4 = StanderdPSO(ACKLEY_FUNCTION, bounds5, particle_size, iterations,
													  Particle.MINIMIZATION, theta,  # NOQA
													  c1=2, c2=0.4)  # NOQA

	_ = Pso_algorithm_with_deffirent_c2_0_4.generate_swarm()

	_, _, Globals0, _ = Pso_algorithm_with_deffirent_c2_0_4.compute()

	Globals_1_run.append(Globals0)

sum_elements_c2_0_4 = [sum(column) for column in zip(*Globals_1_run)]

avg_c2_0_4 = [0] * iterations
for j in range(iterations):
	avg_c2_0_4[j] = sum_elements_c2_0_4[j] / len(seeds)
avarges2.append(avg_c2_0_4)

Globals_1_run = []
for i in seeds:
	np.random.seed(i)
	Pso_algorithm_with_deffirent_c2_0_8 = StanderdPSO(ACKLEY_FUNCTION, bounds5, particle_size, iterations,
													  Particle.MINIMIZATION, theta,  # NOQA
													  c1=2, c2=0.8)  # NOQA
	_ = Pso_algorithm_with_deffirent_c2_0_8.generate_swarm()

	_, _, Globals0, _ = Pso_algorithm_with_deffirent_c2_0_8.compute()

	Globals_1_run.append(Globals0)

sum_elements_c2_0_8 = [sum(column) for column in zip(*Globals_1_run)]

avg_c2_0_8 = [0] * iterations
for j in range(iterations):
	avg_c2_0_8[j] = sum_elements_c2_0_8[j] / len(seeds)

avarges2.append(avg_c2_0_8)

Globals_1_run = []
for i in seeds:
	np.random.seed(i)
	Pso_algorithm_with_deffirent_c2_1_2 = StanderdPSO(ACKLEY_FUNCTION, bounds5, particle_size, iterations,
													  Particle.MINIMIZATION, theta,  # NOQA
													  c1=2, c2=1.2)  # NOQA

	_ = Pso_algorithm_with_deffirent_c2_1_2.generate_swarm()

	_, _, Globals0, _ = Pso_algorithm_with_deffirent_c2_1_2.compute()

	Globals_1_run.append(Globals0)

sum_elements_c2_1_2 = [sum(column) for column in zip(*Globals_1_run)]

avg_c2_1_2 = [0] * iterations
for j in range(iterations):
	avg_c2_1_2[j] = sum_elements_c2_1_2[j] / len(seeds)

avarges2.append(avg_c2_1_2)

Globals_1_run = []
for i in seeds:
	np.random.seed(i)
	Pso_algorithm_with_deffirent_c2_1_6 = StanderdPSO(ACKLEY_FUNCTION, bounds5, particle_size, iterations,
													  Particle.MINIMIZATION, theta,  # NOQA
													  c1=2, c2=1.6)  # NOQA

	_ = Pso_algorithm_with_deffirent_c2_1_6.generate_swarm()

	_, _, Globals0, _ = Pso_algorithm_with_deffirent_c2_1_6.compute()

	Globals_1_run.append(Globals0)

sum_elements_c2_1_6 = [sum(column) for column in zip(*Globals_1_run)]

avg_c2_1_6 = [0] * iterations
for j in range(iterations):
	avg_c2_1_6[j] = sum_elements_c2_1_6[j] / len(seeds)

avarges2.append(avg_c2_1_6)

Globals_1_run = []
for i in seeds:
	np.random.seed(i)
	Pso_algorithm_with_deffirent_c2_2 = StanderdPSO(ACKLEY_FUNCTION, bounds5, particle_size, iterations,
													Particle.MINIMIZATION, theta,  # NOQA
													c1=2, c2=2)  # NOQA

	_ = Pso_algorithm_with_deffirent_c2_2.generate_swarm()

	_, _, Globals0, _ = Pso_algorithm_with_deffirent_c2_2.compute()

	Globals_1_run.append(Globals0)

sum_elements_c2_2 = [sum(column) for column in zip(*Globals_1_run)]

avg_c2_2 = [0] * iterations
for j in range(iterations):
	avg_c2_2[j] = sum_elements_c2_2[j] / len(seeds)

avarges2.append(avg_c2_2)

compare_between_deffirent_c2(ACKLEY_FUNCTION, bounds5[0][0], bounds5[0][1], avarges2, theta,
							 2, c2=[0, 0.4, 0.8, 1.2, 1.6, 2])











_ = Pso_algorithm_with_deffirent_c2_0.generate_swarm()

_, _, Globals0, _ = Pso_algorithm_with_deffirent_c2_0.compute()

_ = Pso_algorithm_with_deffirent_c2_0_4.generate_swarm()

_, _, Globals1, _ = Pso_algorithm_with_deffirent_c2_0_4.compute()

_ = Pso_algorithm_with_deffirent_c2_0_8.generate_swarm()

_, _, Globals2, _ = Pso_algorithm_with_deffirent_c2_0_8.compute()

_ = Pso_algorithm_with_deffirent_c2_1_2.generate_swarm()

_, _, Globals3, _ = Pso_algorithm_with_deffirent_c2_1_2.compute()

_ = Pso_algorithm_with_deffirent_c2_1_6.generate_swarm()

_, _, Globals4, _ = Pso_algorithm_with_deffirent_c2_1_6.compute()

_ = Pso_algorithm_with_deffirent_c2_2.generate_swarm()

_, _, Globals5, _ = Pso_algorithm_with_deffirent_c2_2.compute()

Globals = [Globals0, Globals1, Globals2, Globals3, Globals4, Globals5]

compare_between_deffirent_c2(BOHACHEVSKY_FUNCTIONS, bounds1[0][0], bounds1[0][1], Globals, theta,
							 2, c2=[0, 0.4, 0.8, 1.2, 1.6, 2])  # NOQA

"""
