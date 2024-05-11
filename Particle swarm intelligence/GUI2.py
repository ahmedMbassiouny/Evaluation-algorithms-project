import customtkinter
from PIL import Image
from function_display import display_func, swarm_particle_figure_surface, swarm_particle_figure_contour, animation, \
	compare_between_deffirent_c1, compare_between_deffirent_c2
from Main import *
from StanderdPSO import StanderdPSO
import copy

app = customtkinter.CTk()

global pso_standerd

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

# center the ctk window
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

w = 800
h = app.winfo_screenheight() - 130

a = (screen_width / 2) - (w / 2)
b = (screen_height / 2) - (h / 2)

app.geometry("%dx%d+%d+%d" % (w, h, a, b))

app.title("PSO Algorithm")
customtkinter.set_default_color_theme("dark-blue")

frame1 = customtkinter.CTkFrame(app)
frame1.grid(row=0, column=0, sticky="ewns")
frame1.grid_rowconfigure((0, 1, 2), weight=1)  # NOQA
frame1.grid_columnconfigure(0, weight=1)
frame1.configure(fg_color=("gray85", "gray16"))


def get_choice(choice):
	option_menu_var.set(value=choice)


# creating main frame
main_frame = customtkinter.CTkFrame(frame1)
main_frame.grid(row=0, column=0, sticky="ewns")
main_frame.grid_rowconfigure((0, 1, 2), weight=1)  # NOQA
main_frame.grid_columnconfigure((0, 1), weight=1)  # NOQA
main_frame.configure(fg_color="transparent")

toplevelwindow = None


def showTopLevelResult():
	toplevelwindow_result = customtkinter.CTkToplevel()

	screen_width2 = app.winfo_screenwidth()
	screen_height2 = app.winfo_screenheight()

	width1 = 380
	height1 = 100

	c = (screen_width2 / 2) - (width1 / 2)
	d = (screen_height2 / 2) - (height1 / 2)

	toplevelwindow_result.geometry("%dx%d+%d+%d" % (width1, height1, c, d))

	toplevelwindow_result.attributes('-topmost', 'true')

	toplabel_result1 = customtkinter.CTkLabel(toplevelwindow_result,
											  text=f"The best position found for {label_var4.get()} iterations is ({round(global_best_position[0], 3)},{round(global_best_position[1], 3)})")  # NOQA
	toplabel_result1.grid(row=0, column=0, padx=10, pady=10)

	toplabel_result2 = customtkinter.CTkLabel(toplevelwindow_result,
											  text=f"The best fitness found for {label_var4.get()} iterations is {round(fitness_global_best_position, 3)}")  # NOQA
	toplabel_result2.grid(row=1, column=0, padx=10, pady=10)


def optimization():
	toplevelwindow = customtkinter.CTkToplevel()

	screen_width1 = app.winfo_screenwidth()
	screen_height1 = app.winfo_screenheight()

	width = 350
	height = 100

	c = (screen_width1 / 2) - (width / 2)
	d = (screen_height1 / 2) - (height / 2)

	toplevelwindow.geometry("%dx%d+%d+%d" % (width, height, c, d))

	toplevelwindow.attributes('-topmost', 'true')

	toplabel = customtkinter.CTkLabel(toplevelwindow, text="Optimizing function.....", font=font3)
	toplabel.grid(row=0, column=0, padx=(80, 0), pady=10, sticky="ew")

	progressbar = customtkinter.CTkProgressBar(toplevelwindow, determinate_speed=0.5, height=15)
	progressbar.set(0)
	progressbar.grid(row=1, column=0, padx=(80, 0), pady=10, sticky="ew")
	progressbar.start()

	global swarm_particles  # NOQA
	global pso_standerd
	global particles  # NOQA
	global Globals  # NOQA
	global global_best_position
	global fitness_global_best_position
	button1_2.configure(state="normal")
	button1_3.configure(state="normal")
	button1_4.configure(state="normal")
	button2_1.configure(state="normal")
	button2_2.configure(state="normal")
	button2_3.configure(state="normal")
	if option_menu_var.get() == "BOHACHEVSKY_FUNCTIONS":
		pso_standerd = StanderdPSO(BOHACHEVSKY_FUNCTIONS, bounds1, label_var5.get(), label_var4.get(), 0,
								   label_var1.get(), label_var2.get(),  # NOQA
								   label_var3.get())  # NOQA
		swarm_particles = copy.deepcopy(pso_standerd.generate_swarm())

		global_best_position, fitness_global_best_position, Globals, particles = pso_standerd.compute()

		toplevelwindow.after(2780, toplevelwindow.destroy)

		toplevelwindow.after(2700, showTopLevelResult)

	if option_menu_var.get() == "DROP_WAVE_FUNCTION":
		pso_standerd = StanderdPSO(DROP_WAVE_FUNCTION, bounds2, label_var5.get(), label_var4.get(), 0, label_var1.get(),
								   label_var2.get(),  # NOQA
								   label_var3.get())  # NOQA

		swarm_particles = copy.deepcopy(pso_standerd.generate_swarm())

		global_best_position, fitness_global_best_position, Globals, particles = pso_standerd.compute()

		toplevelwindow.after(2780, toplevelwindow.destroy)

		toplevelwindow.after(2700, showTopLevelResult)
	if option_menu_var.get() == "EGGHOLDER_FUNCTION":
		pso_standerd = StanderdPSO(EGGHOLDER_FUNCTION, bounds3, label_var5.get(), label_var4.get(), 0, label_var1.get(),
								   label_var2.get(),  # NOQA
								   label_var3.get())  # NOQA

		swarm_particles = copy.deepcopy(pso_standerd.generate_swarm())

		global_best_position, fitness_global_best_position, Globals, particles = pso_standerd.compute()

		toplevelwindow.after(2780, toplevelwindow.destroy)

		toplevelwindow.after(2700, showTopLevelResult)
	if option_menu_var.get() == "BOOTH_FUNCTION":
		pso_standerd = StanderdPSO(BOOTH_FUNCTION, bounds4, label_var5.get(), label_var4.get(), 0, label_var1.get(),
								   label_var2.get(),  # NOQA
								   label_var3.get())  # NOQA

		swarm_particles = copy.deepcopy(pso_standerd.generate_swarm())

		global_best_position, fitness_global_best_position, Globals, particles = pso_standerd.compute()

		toplevelwindow.after(2780, toplevelwindow.destroy)

		toplevelwindow.after(2700, showTopLevelResult)


# Optimization button frame
button_frame = customtkinter.CTkFrame(main_frame)
button_frame.grid(row=1, column=1, pady=(200, 0))
button_frame.configure(fg_color="transparent")
button_frame.grid_rowconfigure((0, 1), weight=1)  # NOQA
button_frame.grid_columnconfigure((0, 1), weight=1)  # NOQA

font2 = customtkinter.CTkFont(family="Aptos", size=16, weight="bold")  # NOQA
button_op = customtkinter.CTkButton(button_frame, command=optimization, text="Optimize", font=font2, width=150,
									height=40)  # NOQA
button_op.grid(row=1, column=0, padx=10, pady=10)

# adding Tab frame
tab_frame = customtkinter.CTkTabview(frame1)
tab_frame.grid(row=1, column=0, padx=10, pady=30, sticky="we")
tab_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)  # NOQA

font3 = customtkinter.CTkFont(family="Aptos", size=16, weight="bold")  # NOQA

tab_frame.add("Optimization Result")
tab_frame.add("Analysis")

font1 = customtkinter.CTkFont(family="Aptos Display", size=25, weight="bold")  # NOQA
main_label = customtkinter.CTkLabel(main_frame, text="Particle Swarm Optimization", font=font1, width=100, height=70)
main_label.grid(row=0, column=0, padx=20, pady=20)

functions = ["BOHACHEVSKY_FUNCTIONS", "DROP_WAVE_FUNCTION", "EGGHOLDER_FUNCTION", "BOOTH_FUNCTION"]  # NOQA
option_menu_var = customtkinter.StringVar(value=functions[0])
option_menu = customtkinter.CTkOptionMenu(main_frame, values=functions, variable=option_menu_var, command=get_choice)
option_menu.grid(row=1, column=1, padx=30, pady=(30, 150))


def change_mode():
	if switch_var.get() == "on":
		customtkinter.set_appearance_mode("dark")
	if switch_var.get() == "off":
		customtkinter.set_appearance_mode("light")


switch_frame = customtkinter.CTkFrame(main_frame)
switch_frame.grid(row=0, column=1)
switch_frame.grid_columnconfigure((0, 1, 2), weight=1)  # NOQA
switch_frame.grid_rowconfigure(0, weight=1)
switch_frame.configure(fg_color="transparent")

switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(switch_frame, text="", command=change_mode,
								 variable=switch_var, onvalue="on", offvalue="off", width=10)  # NOQA
switch.grid(row=0, column=1)

sun_image_path = "Images/sun.png"
moon_image_path = "Images/moon.png"

sun_image = Image.open(sun_image_path)
moon_image = Image.open(moon_image_path)

sun_icon = customtkinter.CTkImage(light_image=sun_image, dark_image=sun_image, size=(35, 35))
moon_icon = customtkinter.CTkImage(light_image=moon_image, dark_image=moon_image, size=(25, 25))

sun = customtkinter.CTkLabel(switch_frame, text="", image=sun_icon)
sun.grid(row=0, column=0, pady=20, padx=10)
moon = customtkinter.CTkLabel(switch_frame, text="", image=moon_icon)
moon.grid(row=0, column=2, pady=20, padx=10)


def slider_event1(value):
	label_var1.set(round(value, 1))


def slider_event2(value):
	label_var2.set(round(value, 1))


def slider_event3(value):
	label_var3.set(round(value, 1))


def slider_event4(value):
	label_var4.set(round(value, 1))


def slider_event5(value):
	label_var5.set(round(value, 1))


slider_frame = customtkinter.CTkFrame(main_frame)
slider_frame.grid(row=1, column=0, padx=20, pady=20)
slider_frame.grid_columnconfigure((0, 1, 2), weight=1)  # NOQA
slider_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)  # NOQA
slider_frame.configure(fg_color=("gray90", "gray13"))

slider1 = customtkinter.CTkSlider(slider_frame, from_=0, to=1, number_of_steps=11, command=slider_event1)
slider1.grid(row=0, column=1, padx=10, pady=10)

label_w = customtkinter.CTkLabel(slider_frame, text="w")
label_w.grid(row=0, column=0, padx=5, pady=10)
label_var1 = customtkinter.DoubleVar(value=0.4)
label1 = customtkinter.CTkLabel(slider_frame, text="", textvariable=label_var1)
label1.grid(row=0, column=3, padx=10, pady=10)

slider2 = customtkinter.CTkSlider(slider_frame, from_=0, to=4, number_of_steps=10, command=slider_event2)
slider2.grid(row=1, column=1, padx=10, pady=10)

label_c1 = customtkinter.CTkLabel(slider_frame, text="c1")
label_c1.grid(row=1, column=0, padx=5, pady=10)
label_var2 = customtkinter.DoubleVar(value=2)
label2 = customtkinter.CTkLabel(slider_frame, text="", textvariable=label_var2)
label2.grid(row=1, column=3, padx=10, pady=10)

slider3 = customtkinter.CTkSlider(slider_frame, from_=0, to=4, number_of_steps=10, command=slider_event3)
slider3.grid(row=2, column=1, padx=10, pady=10)

label_c2 = customtkinter.CTkLabel(slider_frame, text="c2")
label_c2.grid(row=2, column=0, padx=5, pady=10)
label_var3 = customtkinter.DoubleVar(value=2)
label3 = customtkinter.CTkLabel(slider_frame, text="", textvariable=label_var3)
label3.grid(row=2, column=3, padx=10, pady=10)

slider4 = customtkinter.CTkSlider(slider_frame, from_=1, to=1000, number_of_steps=999, command=slider_event4)
slider4.grid(row=3, column=1, padx=10, pady=10)

label_iterations = customtkinter.CTkLabel(slider_frame, text="iterations")
label_iterations.grid(row=3, column=0, padx=5, pady=10)
label_var4 = customtkinter.IntVar(value=500)
label4 = customtkinter.CTkLabel(slider_frame, text="", textvariable=label_var4)
label4.grid(row=3, column=3, padx=10, pady=10)

slider5 = customtkinter.CTkSlider(slider_frame, from_=1, to=300, number_of_steps=299, command=slider_event5)
slider5.grid(row=4, column=1, padx=10, pady=10)

label_particles = customtkinter.CTkLabel(slider_frame, text="no. particles")
label_particles.grid(row=4, column=0, padx=5, pady=10)
label_var5 = customtkinter.IntVar(value=100)
label5 = customtkinter.CTkLabel(slider_frame, text="", textvariable=label_var5)
label5.grid(row=4, column=3, padx=10, pady=10)


def showfunction():  # NOQA
	if option_menu_var.get() == "BOHACHEVSKY_FUNCTIONS":
		display_func(BOHACHEVSKY_FUNCTIONS, bounds1[0][0], bounds1[0][1], "BOHACHEVSKY_FUNCTIONS")
	if option_menu_var.get() == "DROP_WAVE_FUNCTION":
		display_func(DROP_WAVE_FUNCTION, bounds2[0][0], bounds2[0][1], "DROP_WAVE_FUNCTION")
	if option_menu_var.get() == "EGGHOLDER_FUNCTION":  # NOQA
		display_func(EGGHOLDER_FUNCTION, bounds3[0][0], bounds3[0][1], "EGGHOLDER_FUNCTION")  # NOQA
	if option_menu_var.get() == "BOOTH_FUNCTION":
		display_func(BOOTH_FUNCTION, bounds4[0][0], bounds4[0][1], "BOOTH_FUNCTION")


def showanimationsurface():
	if option_menu_var.get() == "BOHACHEVSKY_FUNCTIONS":
		swarm_particle_figure_surface(BOHACHEVSKY_FUNCTIONS, bounds1[0][0], bounds1[0][1], swarm_particles,
									  label_var5.get())  # NOQA
	if option_menu_var.get() == "DROP_WAVE_FUNCTION":
		swarm_particle_figure_surface(DROP_WAVE_FUNCTION, bounds2[0][0], bounds2[0][1], swarm_particles,
									  label_var5.get())  # NOQA
	if option_menu_var.get() == "EGGHOLDER_FUNCTION":  # NOQA
		swarm_particle_figure_surface(EGGHOLDER_FUNCTION, bounds3[0][0], bounds3[0][1], swarm_particles,
									  label_var5.get())  # NOQA
	if option_menu_var.get() == "BOOTH_FUNCTION":
		swarm_particle_figure_surface(BOOTH_FUNCTION, bounds4[0][0], bounds4[0][1], swarm_particles, label_var5.get())


def showanimationcontour():
	if option_menu_var.get() == "BOHACHEVSKY_FUNCTIONS":
		swarm_particle_figure_contour(BOHACHEVSKY_FUNCTIONS, bounds1[0][0], bounds1[0][1], swarm_particles,
									  label_var5.get())  # NOQA
	if option_menu_var.get() == "DROP_WAVE_FUNCTION":
		swarm_particle_figure_contour(DROP_WAVE_FUNCTION, bounds2[0][0], bounds2[0][1], swarm_particles,
									  label_var5.get())  # NOQA
	if option_menu_var.get() == "EGGHOLDER_FUNCTION":
		swarm_particle_figure_contour(EGGHOLDER_FUNCTION, bounds3[0][0], bounds3[0][1], swarm_particles,
									  label_var5.get())  # NOQA
	if option_menu_var.get() == "BOOTH_FUNCTION":
		swarm_particle_figure_contour(BOOTH_FUNCTION, bounds4[0][0], bounds4[0][1], swarm_particles, label_var5.get())


def showanimation():  # NOQA
	if option_menu_var.get() == "BOHACHEVSKY_FUNCTIONS":
		animation(BOHACHEVSKY_FUNCTIONS, particles, bounds1[0][0], bounds1[0][1], label_var4.get(), label_var5.get())
	if option_menu_var.get() == "DROP_WAVE_FUNCTION":
		animation(DROP_WAVE_FUNCTION, particles, bounds2[0][0], bounds2[0][1], label_var4.get(), label_var5.get())
	if option_menu_var.get() == "EGGHOLDER_FUNCTION":  # NOQA
		animation(EGGHOLDER_FUNCTION, particles, bounds3[0][0], bounds3[0][1], label_var4.get(), label_var5.get())
	if option_menu_var.get() == "BOOTH_FUNCTION":
		animation(BOOTH_FUNCTION, particles, bounds4[0][0], bounds4[0][1], label_var4.get(), label_var5.get())


def showdifferentc1():
	global avarges
	global Globals_0_run
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


def showdifferentc2():  # NOQA
	global avarges2
	global Globals_1_run
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



def showavarageconverge():  # NOQA
	seeds = [x for x in range(42, 72)]

	global_bests1 = []  # NOQA
	fitness_global_bests1 = []
	Globals_over_runs1 = []  # NOQA
	for i in seeds:
		np.random.seed(i)

		Pso_algorithm = StanderdPSO(ACKLEY_FUNCTION, bounds5, particle_size, iterations, Particle.MINIMIZATION,  # NOQA
									theta,
									c1, c2)

		_ = Pso_algorithm.generate_swarm()

		global_best_position, fitness_global_best_position, Globals1, _ = Pso_algorithm.compute()  # NOQA

		global_bests1.append(global_best_position)
		fitness_global_bests1.append(fitness_global_best_position)
		Globals_over_runs1.append(Globals1)

	global_bests2 = []  # NOQA
	fitness_global_bests2 = []
	Globals_over_runs2 = []  # NOQA
	for i in seeds:
		np.random.seed(i)

		Pso_algorithm = StanderdPSO(RASTRIGIN_FUNCTION, bounds6, particle_size, iterations, Particle.MINIMIZATION,
									# NOQA
									theta,
									c1, c2)

		_ = Pso_algorithm.generate_swarm()

		global_best_position, fitness_global_best_position, Globals1, _ = Pso_algorithm.compute()  # NOQA

		global_bests2.append(global_best_position)
		fitness_global_bests2.append(fitness_global_best_position)
		Globals_over_runs2.append(Globals1)

	global_bests3 = []  # NOQA
	fitness_global_bests3 = []
	Globals_over_runs3 = []  # NOQA
	for i in seeds:
		np.random.seed(i)

		Pso_algorithm = StanderdPSO(SPHERE_FUNCTION, bounds7, particle_size, iterations, Particle.MINIMIZATION,  # NOQA
									theta,
									c1, c2)

		_ = Pso_algorithm.generate_swarm()

		global_best_position, fitness_global_best_position, Globals1, _ = Pso_algorithm.compute()  # NOQA

		global_bests3.append(global_best_position)
		fitness_global_bests3.append(fitness_global_best_position)
		Globals_over_runs3.append(Globals1)

	# fig = go.Figure(
	# data=go.Scatter(x=list(range(1, iterations + 1)), y=Globals, mode="lines+markers"))
	# fig.update_layout(title='Convergence Plot', xaxis_title='Iteration', yaxis_title='Best Fitness')
	# fig.show()

	array_avrage_position1 = np.array(global_bests1)  # NOQA
	xs1 = []
	ys1 = []
	for position in array_avrage_position1:
		xs1.append(position[0])
		ys1.append(position[1])

	avarge_x1 = np.mean(xs1)  # NOQA
	avarge_y1 = np.mean(ys1)  # NOQA

	avarage_position1 = (avarge_x1, avarge_y1)  # NOQA

	avarage_fitness1 = np.array(fitness_global_bests1).mean()  # NOQA

	sum1 = [0] * iterations
	result_of_avarages1 = [0] * iterations  # NOQA
	for run in Globals_over_runs1:
		for i in range(len(run)):
			sum1[i] += run[i]

	for j in range(iterations):  # NOQA
		result_of_avarages1[j] = sum1[j] / len(seeds)  # NOQA

	# print(
	# f"the mean best point for ACKLEY_FUNCTION is ({avarage_position1})")
	# print(f"the avarage of best fittness for ACKLEY_FUNCTION is {avarage_fitness1}")

	array_avrage_position2 = np.array(global_bests2)  # NOQA
	xs2 = []
	ys2 = []
	for position in array_avrage_position2:
		xs2.append(position[0])
		ys2.append(position[1])

	avarge_x2 = np.mean(xs2)  # NOQA
	avarge_y2 = np.mean(ys2)  # NOQA

	avarage_position2 = (avarge_x2, avarge_y2)  # NOQA

	avarage_fitness2 = np.array(fitness_global_bests2).mean()  # NOQA

	sum2 = [0] * iterations
	result_of_avarages2 = [0] * iterations  # NOQA
	for run in Globals_over_runs2:
		for i in range(len(run)):
			sum2[i] += run[i]

	for j in range(iterations):
		result_of_avarages2[j] = sum2[j] / len(seeds)  # NOQA

	# print(
	# f"the mean best point for RASTRIGIN_FUNCTION is ({avarage_position2})")
	# print(f"the avarage of best fittness for RASTRIGIN_FUNCTION is {avarage_fitness2}")

	array_avrage_position3 = np.array(global_bests3)  # NOQA
	xs3 = []
	ys3 = []
	for position in array_avrage_position3:
		xs3.append(position[0])
		ys3.append(position[1])

	avarge_x3 = np.mean(xs3)  # NOQA
	avarge_y3 = np.mean(ys3)  # NOQA

	avarage_position3 = (avarge_x3, avarge_y3)  # NOQA

	avarage_fitness3 = np.array(fitness_global_bests3).mean()  # NOQA

	sum3 = [0] * iterations
	result_of_avarages3 = [0] * iterations  # NOQA
	for run in Globals_over_runs3:
		for i in range(len(run)):
			sum3[i] += run[i]

	for j in range(iterations):
		result_of_avarages3[j] = sum3[j] / len(seeds)  # NOQA

	# print(
	# f"the mean best point for SPHERE_FUNCTION is (f{avarage_position3})")
	# print(f"the avarage of best fittness for SPHERE_FUNCTION is {avarage_fitness3}")

	avarges = [result_of_avarages1, result_of_avarages2, result_of_avarages3]  # NOQA
	functions = ["ACKLEY_FUNCTION", "RASTRIGIN_FUNCTION", "SPHERE_FUNCTION"]  # NOQA

	fig = go.Figure()

	for i in range(len(avarges)):
		fig.add_trace(
			go.Scatter(x=list(range(1, iterations + 1)), y=avarges[i], mode="lines+markers", name=f"{functions[i]}"))

	fig.update_layout(title='avarage fitness of 3 functions', xaxis_title='Iteration',
					  yaxis_title='Best Fitness')  # NOQA
	fig.show()


def showconvergent():  # NOQA
	fig = go.Figure(data=go.Scatter(x=list(range(1, label_var4.get() + 1)), y=Globals, mode="lines+markers"))
	fig.update_layout(title='Convergence Plot', xaxis_title='Iteration', yaxis_title='Best Fitness')
	fig.show()


label1_1 = customtkinter.CTkLabel(tab_frame.tab("Optimization Result"), text="Show the function",
								  font=font3)  # NOQA
label1_1.grid(row=0, column=0, padx=10, pady=10)
button1_1 = customtkinter.CTkButton(tab_frame.tab("Optimization Result"), text="Show",
									command=showfunction)  # NOQA
button1_1.grid(row=0, column=2, padx=(200, 10), pady=10)

label1_2 = customtkinter.CTkLabel(tab_frame.tab("Optimization Result"),
								  text="Show initialization animation in surface plot",  # NOQA
								  font=font3)  # NOQA
label1_2.grid(row=1, column=0, padx=10, pady=10)
button1_2 = customtkinter.CTkButton(tab_frame.tab("Optimization Result"), text="Show", state="disabled",
									command=showanimationsurface)  # NOQA
button1_2.grid(row=1, column=2, padx=(200, 10), pady=10)

label1_3 = customtkinter.CTkLabel(tab_frame.tab("Optimization Result"),
								  text="Show intialization in Contour plot",  # NOQA
								  font=font3)  # NOQA
label1_3.grid(row=2, column=0, padx=10, pady=10)
button1_3 = customtkinter.CTkButton(tab_frame.tab("Optimization Result"), text="Show", state="disabled",
									command=showanimationcontour)  # NOQA
button1_3.grid(row=2, column=2, padx=(200, 10), pady=10)

label1_4 = customtkinter.CTkLabel(tab_frame.tab("Optimization Result"),
								  text="Show animation of evaluation of particle",  # NOQA
								  font=font3)  # NOQA
label1_4.grid(row=3, column=0, padx=10, pady=10)
button1_4 = customtkinter.CTkButton(tab_frame.tab("Optimization Result"), text="Show", state="disabled",
									command=showanimation)  # NOQA
button1_4.grid(row=3, column=2, padx=(200, 10), pady=10)

label2_1 = customtkinter.CTkLabel(tab_frame.tab("Analysis"), text="Show the Result in different c1",
								  font=font3)  # NOQA
label2_1.grid(row=0, column=0, padx=10, pady=10)
button2_1 = customtkinter.CTkButton(tab_frame.tab("Analysis"), text="Show", state="disabled", command=showdifferentc1)
button2_1.grid(row=0, column=2, padx=(250, 10), pady=10)

label2_2 = customtkinter.CTkLabel(tab_frame.tab("Analysis"), text="Show the Result in different c2",
								  font=font3)  # NOQA
label2_2.grid(row=1, column=0, padx=10, pady=10)
button2_2 = customtkinter.CTkButton(tab_frame.tab("Analysis"), text="Show", state="disabled", command=showdifferentc2)
button2_2.grid(row=1, column=2, padx=(250, 10), pady=10)

label2_3 = customtkinter.CTkLabel(tab_frame.tab("Analysis"), text="Show convergent plot",
								  font=font3)  # NOQA
label2_3.grid(row=2, column=0, padx=10, pady=10)
button2_3 = customtkinter.CTkButton(tab_frame.tab("Analysis"), text="Show", state="disabled", command=showconvergent)
button2_3.grid(row=2, column=2, padx=(250, 10), pady=10)

label2_4 = customtkinter.CTkLabel(tab_frame.tab("Analysis"), text="Show avarage convergent plot over 30 runs",
								  font=font3)  # NOQA
label2_4.grid(row=3, column=0, padx=10, pady=10)
button2_4 = customtkinter.CTkButton(tab_frame.tab("Analysis"), text="Show",
									command=showavarageconverge)  # NOQA
button2_4.grid(row=3, column=2, padx=(250, 10), pady=10)

app.mainloop()
