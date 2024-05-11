import numpy as np
from ObjectiveFunctions import *
from WorkerBee import WorkerBee
from EmployeeBee import EmployeeBee
from OnlookerBee import onlookerBee
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class ABC(object):
    
    def __init__(self, obj_function, colonySize=100, n_iter=300, limit=100):
        self.colony_size = colonySize
        self.n_iter = n_iter
        self.limit = limit
        self.obj_function = obj_function
        self.optimal_solution = EmployeeBee(obj_function)

    
    def initialize_employees(self):
        self.employee_bees = []
        for itr in range(self.colony_size // 2):
            self.employee_bees.append(EmployeeBee(self.obj_function))
        self.compute_all_probability()

         
        
    
    def employee_bees_phase(self):
       for bee in self.employee_bees:
        bee.generate_solution(self.employee_bees)



    def compute_all_probability(self):
     for employeeee in self.employee_bees:
       employeeee.prob = employeeee.compute_prob()



    def initialize_onlookers(self):
        self.onlookeer_bees = []
        for itr in range(self.colony_size // 2):
            self.onlookeer_bees.append(onlookerBee(self.obj_function))
          

    def onlooker_bees_phase(self):
          for bee in self.onlookeer_bees:
            bee.exploit_food_sources(self.employee_bees)
        

    def check_scout_phase(self):
        self.update_optimal_solution()
        max_trial_employee = max(self.employee_bees, key=lambda x: x.trial)
        if  max_trial_employee.trial >= self.limit:
             self.employee_bees.remove(max_trial_employee)
             new_employee = EmployeeBee(self.obj_function)
             new_employee.prob = new_employee.compute_prob()
             self.employee_bees.append( new_employee)
        self.update_optimal_solution()


    def update_optimal_solution(self):
        self.optimal_solution = max(self.employee_bees, key=lambda x: x.fitness)

    

  


# bukin_1 = rastrigin_function(2, -5.12, 5.12 )

# #ploting the function 
# # Generate 2D input array
# x = np.linspace(-5.12, 5.12, 50)
# y = np.linspace(-5.12, 5.12, 50)
# X, Y = np.meshgrid(x, y)

# # Calculate the objective values
# Z = np.apply_along_axis(bukin_1.objective_value, axis=1, arr=np.column_stack((X.ravel(), Y.ravel())))
# Z = Z.reshape(X.shape)

# # Create a 3D plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# global surface
# surface = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')


# # Set labels and title
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Objective Value')
# ax.set_title('Rastrigin Function in 3D')

# evolution = ABC(bukin_1)
# evolution.initialize_employees()
# evolution.initialize_onlookers()


# employee_points, = ax.plot([], [], [], 'ro', markersize=10)

# def update(frame, evolution):
#     ax.clear()  # Clear the existing plot
    
#     # Plot the surface
#     ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')

#     # Plot the employee points
#     for obj in evolution.employee_bees:
#         ax.scatter(obj.position[0], obj.position[1], obj.objectivevalue, color='red', s=50)
    
#     # Update the data for employee_points
#     employee_points.set_data([obj.position[0] for obj in evolution.employee_bees], [obj.position[1] for obj in evolution.employee_bees])
#     employee_points.set_3d_properties([obj.objectivevalue for obj in evolution.employee_bees])

#     evolution.employee_bees_phase()
#     evolution.onlooker_bees_phase()
#     evolution.check_scout_phase()
#     evolution.update_optimal_solution()

#     print(f"Iteration: {frame}, Optimal Solution: {evolution.optimal_solution.position}, Objective Value: {evolution.optimal_solution.objectivevalue}")

# ani = FuncAnimation(fig, update, fargs=(evolution,), frames=evolution.n_iter, interval=100)
# plt.show()















# for obj in evolution.employee_bees:
#     ax.scatter(obj.position[0], obj.position[1], obj.objectivevalue, color='red', s=50)

# for itr in range(evolution.n_iter):
    
#     evolution.employee_bees_phase()
#     evolution.onlooker_bees_phase()
#     evolution.check_scout_phase()
#     evolution.update_optimal_solution()


#     print("iter: {} = cost: {}"
#                   .format(itr, "%04.03e" % evolution.optimal_solution.fitness))
#     print(evolution.optimal_solution.position)
#     print(f"trials : {evolution.optimal_solution.trial}")
# max_object = max(evolution.employee_bees, key=lambda x: x.fitness)
# print(f"the posistion is {max_object.position} and the objective value is is {max_object.objectivevalue} and the ftiness is {max_object.fitness} and calculate fitness {max_object.calculate_fitness(max_object.objectivevalue)}")


