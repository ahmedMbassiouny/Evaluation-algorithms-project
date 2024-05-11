from Particle import Particle
from typing import Callable
import copy


class StanderdPSO:
	def __init__(self, objective_function: Callable[[float, float], float],
				 bounds: list[tuple[float, float], tuple[float, float]], particle_size: int,  # NOQA
				 iterations: int, type_of_problem: int, theta: float, c1: float, c2: float):  # NOQA
		self.fitness_global_best_particle_position: float = float(
			"INF") if type_of_problem == Particle.MINIMIZATION else -float("INF")
		self.global_best_particle_position: list[float, float] = []
		self.swarm_particles: list[Particle] = []
		self.bounds = bounds
		self.iterations = iterations
		self.particle_size = particle_size
		self.type_of_problem = type_of_problem
		self.objective_function = objective_function
		self.Globals: list[float] = []
		self.particles: list[list[Particle]] = [[None]] * self.iterations  # NOQA
		self.theta = theta
		self.c1 = c1
		self.c2 = c2

	def generate_swarm(self):
		for i in range(self.particle_size):
			self.swarm_particles.append(Particle(self.bounds, self.type_of_problem))
		return self.swarm_particles

	def compute(self) -> tuple[list[float, float], float, list[float], list[list[Particle]]]:
		for iteration in range(self.iterations):
			self.particles[iteration] = copy.deepcopy(self.swarm_particles)
			for particle in range(self.particle_size):
				self.swarm_particles[particle].evaluate_position(self.objective_function)

				if self.type_of_problem == Particle.MINIMIZATION:

					if self.swarm_particles[
						particle].fitness_particle_position < self.fitness_global_best_particle_position:
						self.global_best_particle_position = list(self.swarm_particles[particle].particle_position)
						self.fitness_global_best_particle_position = float(
							self.swarm_particles[particle].fitness_particle_position)

				if self.type_of_problem == Particle.MAXIMIZATION:

					if self.swarm_particles[
						particle].fitness_particle_position > self.fitness_global_best_particle_position:
						self.global_best_particle_position = list(self.swarm_particles[particle].particle_position)
						self.fitness_global_best_particle_position = float(
							self.swarm_particles[particle].fitness_particle_position)
			for k in range(self.particle_size):
				self.swarm_particles[k].update_velocity(self.global_best_particle_position, self.theta, self.c1,
														self.c2)
				self.swarm_particles[k].update_position(self.bounds)

			self.Globals.append(self.fitness_global_best_particle_position)

		return self.global_best_particle_position, self.fitness_global_best_particle_position, self.Globals, self.particles
