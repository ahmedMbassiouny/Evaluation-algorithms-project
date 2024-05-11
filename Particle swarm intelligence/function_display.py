import plotly.graph_objects as go
import numpy as np
from Parameters import *
from Particle import Particle
from plotly.subplots import make_subplots
import plotly as py
import pandas as pd


def display_func(function, lower: float, upper: float, function_name: str):
	x, y = np.linspace(lower, upper, 100), np.linspace(lower, upper, 100)
	z = np.zeros(shape=(x.shape[0], y.shape[0]))  # NOQA

	for i in range(x.shape[0]):
		for j in range(y.shape[0]):
			z[i, j] = function(x[i], y[j])

	fig = go.Figure(data=[go.Surface(z=z)])
	fig.update_layout(title=function_name, autosize=True)
	fig.update_traces(contours_z=dict(show=True, usecolormap=True,
									  highlightcolor="limegreen", project_z=True))  # NOQA

	fig.show()


def swarm_particle_figure_surface(function, lower: float, upper: float, swarm_particle: list[Particle],
								  particle_size) -> None:
	x, y = np.linspace(lower, upper, particle_size), np.linspace(lower, upper, particle_size)  # NOQA
	z = np.zeros(shape=(x.shape[0], y.shape[0]))  # NOQA

	for i in range(x.shape[0]):
		for j in range(y.shape[0]):
			z[i, j] = function(x[i], y[j])

	surface = go.Surface(x=x, y=y, z=z)

	layout = go.Layout(
		title_text=f"The Random intialization of {particle_size} particles in surface plot",  # NOQA
		title=dict(x=0.5, y=0.9),
		updatemenus=[
			{
				"type": "buttons",
				"buttons": [{
					"label": "Play",
					"method": "animate",
					"args": [
						None, {
							"frame": {
								"duration": 50,
								"redraw": True
							},
							"fromcurrent": True,
							"transition": {
								"duration": 300,
								"easing": "quadratic-in-out"
							}
						}
					],
				}],
				"x": 0.1,
				"y": 1,
				"yanchor": "top"
			},
			{
				"type": "buttons",
				"buttons": [{
					"label": "Pause",
					"method": "animate",
					"args": [
						[None], {
							"frame": {
								"duration": 0,
								"redraw": True
							},
							"mode": "immediate",
							"transition": {
								"duration": 0,
							}
						}
					]
				}],
				"x": 0.16,
				"y": 1,
				"yanchor": "top"
			},

		]
	)
	xx = [swarm_particle[n].particle_position[0] for n in range(particle_size)]
	yy = [swarm_particle[n].particle_position[1] for n in range(particle_size)]
	zz = [function(xx[m], yy[m]) for m in range(particle_size)]

	frames = [go.Frame(
		data=go.Scatter3d(
			x=xx[:i + 1],
			y=yy[:i + 1],
			z=zz[:i + 1],
			mode="markers",
			marker=dict(color="red", size=10)
		)) for i in range(particle_size)]

	fig = go.Figure(data=[surface, surface], layout=layout, frames=frames)

	fig.show()


def swarm_particle_figure_contour(function, lower: float, upper: float, swarm_particle: list[Particle],
								  particle_size) -> None:
	x, y = np.linspace(lower, upper, particle_size), np.linspace(lower, upper, particle_size)  # NOQA
	z = np.zeros(shape=(x.shape[0], y.shape[0]))  # NOQA

	for i in range(x.shape[0]):
		for j in range(y.shape[0]):
			z[i, j] = function(x[i], y[j])

	contour = go.Contour(z=z, x=x, y=y, line_smoothing=0.85)  # NOQA

	x_contour = []
	y_contour = []

	for particle in swarm_particle:
		x_contour.append(particle.particle_position[0])
		y_contour.append(particle.particle_position[1])

		scatter = go.Scatter(x=x_contour, y=y_contour
							 , mode="markers", marker=dict(size=10, color="red"))  # NOQA

	fig = go.Figure(data=[contour, scatter])  # NOQA
	fig.update_layout(title_text=f"The Random intialization of {particle_size} particles in Contour plot",  # NOQA
					  title=dict(x=0.5, y=0.9)  # NOQA
					  )  # NOQA
	fig.show()


def animation(function, particles: list[list[Particle]], upper, lower, iterations, particle_size):
	x, y = np.linspace(lower, upper, particle_size), np.linspace(lower, upper, particle_size)  # NOQA
	z = np.zeros(shape=(x.shape[0], y.shape[0]))

	for i in range(x.shape[0]):
		for j in range(y.shape[0]):
			z[i, j] = function(x[i], y[j])

	surface = go.Surface(x=x, y=y, z=z, contours_z=dict(show=True, usecolormap=True, project_z=True))

	xx = [[particles[n][k].particle_position[0] for k in range(particle_size)] for n in range(iterations)]
	yy = [[particles[n][k].particle_position[1] for k in range(particle_size)] for n in range(iterations)]
	zz = [[function(xx[m][p], yy[m][p]) for p in range(particle_size)] for m in range(iterations)]

	layout = go.Layout(
		scene=dict(
			xaxis=dict(range=[lower, upper], autorange=False, zeroline=False),
			yaxis=dict(range=[lower, upper], autorange=False, zeroline=False),
		),
		updatemenus=[
			{
				"type": "buttons",
				"buttons": [{
					"label": "Play",
					"method": "animate",
					"args": [
						None, {
							"frame": {
								"duration": 150,
								"redraw": True
							},
							"fromcurrent": True,
							"transition": {
								"duration": 50,
								"easing": "quadratic-in-out"
							}
						}
					],
				}],
				"x": 0.1,
				"y": 1,
				"yanchor": "top"
			},
			{
				"type": "buttons",
				"buttons": [{
					"label": "Pause",
					"method": "animate",
					"args": [
						[None], {
							"frame": {
								"duration": 0,
								"redraw": True
							},
							"mode": "immediate",
							"transition": {
								"duration": 0,
							}
						}
					]
				}],
				"x": 0.16,
				"y": 1,
				"yanchor": "top"
			},

		],
	)

	frames = [go.Frame(
		data=[go.Scatter3d(
			x=xx[i],
			y=yy[i],
			z=zz[i],
			mode="markers",
			marker=dict(color="red", size=10),
		)],
		layout=go.Layout(title_text=f"Iteration {i}", title=dict(x=0.5, y=0.9))  # NOQA
	) for i in range(iterations)]

	fig = go.Figure(data=[surface] * 2, layout=layout, frames=frames)
	fig.show()


def compare_between_deffirent_c1(function, upper, lower, Globals: list[list[float]], w: float, c1: list[float],  # NOQA
								 c2: float):  # NOQA

	fig = go.Figure()  # NOQA
	for i in range(len(Globals)):
		fig.add_trace(
			go.Scatter(x=list(range(1, iterations + 1)), y=Globals[i], mode="lines+markers", name=f"c1={c1[i]}"))

	fig.update_layout(title='Comparing between deffirent c1', xaxis_title='Iteration', yaxis_title='Best Fitness')

	fig.show()


def compare_between_deffirent_c2(function, upper, lower, Globals: list[list[list[float]]], w: float, c1: float,  # NOQA
								 c2: list[list[float]]):  # NOQA
	fig = go.Figure()  # NOQA
	for i in range(len(Globals)):
		fig.add_trace(
			go.Scatter(x=list(range(1, iterations + 1)), y=Globals[i], mode="lines+markers", name=f"c2={c2[i]}"))

	fig.update_layout(title='Comparing between deffirent c2', xaxis_title='Iteration', yaxis_title='Best Fitness')

	fig.show()
