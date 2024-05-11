from Parameters import number_of_variables
from random import uniform, random
from typing import Callable


class Particle:
	MINIMIZATION = 0
	MAXIMIZATION = 1

	def __init__(self, bounds: list[tuple[float, float], tuple[float, float]], type_of_problem):
		self.type_of_problem = type_of_problem
		self.particle_position: list[float, float] = []  # A Particle Position
		self.particle_velocity: list[float, float] = []  # A Particle Velocity
		self.local_best_particle_position: list[float, float] = []  # A Local best position for A particle
		self.fitness_local_best_particle_position: float = float(
			"INF") if self.type_of_problem == self.MINIMIZATION else -float(
			"INF")  # Fitness of Best Local Particle position for a particle
		self.fitness_particle_position: float = float("INF") if self.type_of_problem == self.MINIMIZATION else -float(
			"INF")  # Fitness for A particle current position

		# initialize a random particle position and velocity
		for i in range(number_of_variables):
			self.particle_position.append(uniform(bounds[i][0], bounds[i][1]))
			self.particle_velocity.append(uniform(bounds[i][0], bounds[i][1]))

	# Function to evaluate the position of the current particle
	def evaluate_position(self, objective_function: Callable[[float, float], float]) -> None:
		#  Calculate The Fitness for a particle in current position
		self.fitness_particle_position = objective_function(self.particle_position[0], self.particle_position[1])

		if self.type_of_problem == self.MINIMIZATION:

			if self.fitness_particle_position < self.fitness_local_best_particle_position:
				self.local_best_particle_position = self.particle_position
				self.fitness_local_best_particle_position = self.fitness_particle_position

		if self.type_of_problem == self.MAXIMIZATION:

			if self.fitness_particle_position > self.fitness_local_best_particle_position:
				self.local_best_particle_position = self.particle_position
				self.fitness_local_best_particle_position = self.fitness_particle_position

	def update_position(self, bounds):
		# update position for A particle
		for i in range(number_of_variables):
			self.particle_position[i] = self.particle_position[i] + self.particle_velocity[i]

			# check if the new position of the particle is exceeded upper bounds
			if self.particle_position[i] > bounds[i][1]:
				self.particle_position[i] = bounds[i][1]

			# check if the new position of the particle is bellow lower bounds
			if self.particle_position[i] < bounds[i][0]:
				self.particle_position[i] = bounds[i][0]

	def update_velocity(self, global_best_particle_position: list[float, float], theta: float, c1: float, c2: float):
		# Update velocity of a particle
		for i in range(number_of_variables):
			r1 = random()  # return a random value in range [0,1)
			r2 = random()  # return a random value in range [0,1)

			cognitive_velocity: float = c1 * r1 * (self.local_best_particle_position[i] - self.particle_position[i])
			social_velocity: float = c2 * r2 * (global_best_particle_position[i] - self.particle_position[i])
			self.particle_velocity[i] = theta * self.particle_velocity[i] + cognitive_velocity + social_velocity
