import numpy as np
from ObjectiveFunctions import *
from WorkerBee import WorkerBee
from EmployeeBee import EmployeeBee

class onlookerBee(WorkerBee):

    last_food_source = 0


    """
    function :  onlook on the best fodd sources explored by Employeed bee
    arguments:  best_food_sources ==> positions of employeed bees(solutions)
    """
    
    def exploit_food_sources(self, best_food_sources):
        # print("#########ONLOOKER PHASE######")

        for i in range(len(best_food_sources)):
            r = np.random.uniform(0, 1)
            # print(f" r = {r}")
            # print(f" probabilty of the current {best_food_sources[(i + onlookerBee.last_food_source) % len(best_food_sources)].compute_prob()}")
            if r < best_food_sources[(i + onlookerBee.last_food_source) % len(best_food_sources)].compute_prob():

                self.position = best_food_sources[i].position.copy()
                # print(f"current position{self.position}")
                self.objectivevalue = self.evaluate(self.position)
                # print(f"current objective value{self.objectivevalue}")
                self.fitness = self.calculate_fitness(self.objectivevalue)
                # print(f"current current fitness{ self.fitness}")
                self.trial = best_food_sources[i].trial


                partner = np.random.choice(best_food_sources)
                
                while ((partner.position == self.position).any()):
                    partner = np.random.choice(best_food_sources)
                # print(f"partner position: {partner.position}")
        
                component = np.random.choice(self.position) 
                # print(f" the component is {component}")         #decsition variable in current position to be modified
                index = np.where(self.position == component)[0][0]   #index of descition variable in partner position to be modified
                # print(f"index: {index}")
        
                phi = np.random.uniform(-1, 1)
                # print(f"phi {phi}")
        
                new_position = self.position.copy()
                new_position[index] = new_position[index] + phi*(component - partner.position[index]) 
                
                # print(f"new solution{new_position}")
        
                new_position =  best_food_sources[i].check_limits(new_position)
                # print(f"new position after checking the limits{new_position}")
                new_objective_value = best_food_sources[i].evaluate(new_position)
                # print(f" new objective value {new_objective_value}")
        
                new_fitness =  best_food_sources[i].calculate_fitness(new_objective_value)
                # print(f"new fitness: {new_fitness}")
        
                best_food_sources[i].update_worker(new_position, new_fitness)
                best_food_sources[i].objectivevalue = best_food_sources[i].evaluate(best_food_sources[i].position)
                best_food_sources[i].prob = best_food_sources[i].compute_prob()
                # print(f" after update")
                # print(f"position {best_food_sources[i].position} and objective value f{best_food_sources[i].objectivevalue} and fitness f{best_food_sources[i].fitness} , and probabilty {best_food_sources[i].prob}")

                onlookerBee.last_food_source += 1
                # print("----------------------------------------------------------------------")
                break

            else:
                onlookerBee.last_food_source += 1





# f = Sphere_function(2, -5.12, 5.12 )
# emp1 = EmployeeBee(f)
# print(f"max_fitness {emp1.max_fitness}")
# emp2 = EmployeeBee(f)
# print(f"max_fitness {emp1.max_fitness}")

# emp3 = EmployeeBee(f)
# print(f"max_fitness {emp1.max_fitness}")

# emp4 = EmployeeBee(f)
# print(f"max_fitness {emp1.max_fitness}")

# emp1.prob = emp1.compute_prob()
# emp2.prob  =emp2.compute_prob()
# emp3.prob =emp3.compute_prob()
# emp4.prob =emp4.compute_prob()
# emp_list = [emp1, emp2 , emp3, emp4 ]
# on1 = onlookerBee(f)
# on2 = onlookerBee(f)
# on3 = onlookerBee(f)
# on4 = onlookerBee(f)
# onlookerss = [on1, on2, on3, on4]

# for employeee in emp_list:
# print(f"the posistion is {employeee.position} and the objective value is is {employeee.objectivevalue} and the ftiness is {employeee.fitness} and calculate fitness {employeee.calculate_fitness(employeee.objectivevalue)}")
# print("----------------------------------")
# for onlook in onlookerss :
#    onlook.exploit_food_sources(emp_list)
# print("----------------------------------")
# for employeee in emp_list:
#  print(f"the posistion is {employeee.position} and the objective value is is {employeee.objectivevalue} and the ftiness is {employeee.fitness} and calculate fitness {employeee.calculate_fitness(employeee.objectivevalue)}")
# for employeee in emp_list:
#    print(f"the posistion is {employeee.position} and the objective value is is {employeee.objectivevalue} and the ftiness is {employeee.fitness} and calculate fitness {employeee.calculate_fitness(employeee.objectivevalue)} and probabilty {employeee.prob}" )
#    print("--------------------------------------------------------------")
#    employeee.generate_solution(emp_list)
#    print(f"the posistion is {employeee.position} and the objective value is is {employeee.objectivevalue} and the ftiness is {employeee.fitness} and calculate fitness {employeee.calculate_fitness(employeee.objectivevalue)} and probabilty {employeee.prob} ")

#    print(employeee.objectivevalue)


