from random import Random
from time import time
from math import cos
from math import pi
from inspyred import ec
from inspyred.ec import terminators
import numpy as np
import os

def generate_(random, args):
    size = args.get('num_inputs', 12)
    return [random.randint(0, 15000) for i in range(size)]

def evaluate_(candidates, args):
    fitness = []
    for cs in candidates:
        fit = perform_fitness(cs[0], cs[1], cs[2], cs[3], cs[4],
                              cs[5], cs[6], cs[7], cs[8], cs[9],
                              cs[10], cs[11])
        fitness.append(fit)
    return fitness

def perform_fitness(C1Dianteira, C1Central, C1Traseira, C2Dianteira, C2Central, C2Traseira,
                    C3Dianteira, C3Central, C3Traseira, C4Dianteira, C4Central, C4Traseira):

    C1Dianteira = np.round(C1Dianteira)
    C1Central = np.round(C1Central)
    C1Traseira = np.round(C1Traseira)
    C2Dianteira = np.round(C2Dianteira)
    C2Central = np.round(C2Central)
    C2Traseira = np.round(C2Traseira)
    C3Dianteira = np.round(C3Dianteira)
    C3Central = np.round(C3Central)
    C3Traseira = np.round(C3Traseira)
    C4Dianteira = np.round(C4Dianteira)
    C4Central = np.round(C4Central)
    C4Traseira = np.round(C4Traseira)

    carga1 = C1Dianteira + C1Central + C1Traseira
    carga2 = C2Dianteira + C2Central + C2Traseira
    carga3 = C3Dianteira + C3Central + C3Traseira
    carga4 = C4Dianteira + C4Central + C4Traseira

    #Lucro
    fit = float((carga1 * 0.31 + carga2 * 0.38 + carga3 * 0.35 + carga4 * 0.285) / 12350)
    # Total Suportado Avião
    h1 = np.maximum(0, float((C1Dianteira + C1Central + C1Traseira + C2Dianteira + C2Central + C2Traseira
    + C3Dianteira + C3Central + C3Traseira + C4Dianteira + C4Central + C4Traseira) - 34000)) / 3090.90
    # Total Suportado Dianteira
    h2 = np.maximum(0, float((C1Dianteira + C2Dianteira + C3Dianteira + C4Dianteira) - 10000)) / 909
    # Total Suportado Central
    h3 = np.maximum(0, float((C1Central + C2Central + C3Central + C4Central) - 16000)) / 1452
    # Total Suportado Traseira
    h4 = np.maximum(0, float((C1Traseira + C2Traseira + C3Traseira + C4Traseira) - 8000)) / 727
    # Carga 1
    h5 = np.maximum(0, float((C1Dianteira + C1Central + C1Traseira) - 18000)) / 1636
    # Carga 2
    h6 = np.maximum(0, float((C2Dianteira + C2Central + C2Traseira) - 15000)) / 1363
    # Carga 3
    h7 = np.maximum(0, float((C3Dianteira + C3Central + C3Traseira) - 23000)) / 2090
    # Carga 4
    h8 = np.maximum(0, float((C4Dianteira + C4Central + C4Traseira) - 12000)) / 1090
    # Capacidade de Volumétrica Dianteira
    h9 = np.maximum(0, float(C1Dianteira * 0.48 + C2Dianteira * 0.65 + C3Dianteira * 0.58 + C4Dianteira * 0.39)-6800) / 618
    # Capacidade de Volumétrica Central
    h10 = np.maximum(0, float(C1Central * 0.48 + C2Central * 0.65 + C3Central * 0.58 + C4Central * 0.39)-8700) / 790  
    # Capacidade de Volumétrica Traseira                 
    h11 = np.maximum(0, float(C1Traseira*0.48 + C2Traseira*0.65
                    + C3Traseira*0.58 + C4Traseira*0.39)-5300) / 481

    fit = fit - (h1 + h2 + h3 + h4 + h5 + h6 + h7 + h8 + h9 + h10 + h11)
    return fit
  
def solution_evaluation(C1Dianteira, C1Central, C1Traseira, C2Dianteira, C2Central, C2Traseira,
                    C3Dianteira, C3Central, C3Traseira, C4Dianteira, C4Central, C4Traseira):

    C1Dianteira = np.round(C1Dianteira)
    C1Central = np.round(C1Central)
    C1Traseira = np.round(C1Traseira)
    C2Dianteira = np.round(C2Dianteira)
    C2Central = np.round(C2Central)
    C2Traseira = np.round(C2Traseira)
    C3Dianteira = np.round(C3Dianteira)
    C3Central = np.round(C3Central)
    C3Traseira = np.round(C3Traseira)
    C4Dianteira = np.round(C4Dianteira)
    C4Central = np.round(C4Central)
    C4Traseira = np.round(C4Traseira)

    print("########## RESUMO DO VOÔ##########")
    print("Lucro total R${}".format(float(0.31*(C1Dianteira + C1Central + C1Traseira) + 0.38*(C2Dianteira + C2Central + C2Traseira)
    + 0.35*(C3Dianteira + C3Central + C3Traseira) + 0.285*(C4Dianteira + C4Central + C4Traseira))))
    print("############################################################")
    print("Capacidade volumétrica (m3): {}"
    .format(float(C1Dianteira + C1Central + C1Traseira + C2Dianteira + C2Central + C2Traseira
    + C3Dianteira + C3Central + C3Traseira+ C4Dianteira + C4Central + C4Traseira))+" m3.")
    print("############################################################")
    print("Carga 1 {}".format(C1Dianteira + C1Central + C1Traseira)+"kg.")
    print("Carga 2 {}".format(C2Dianteira + C2Central + C2Traseira)+"kg.")
    print("Carga 3 {}".format(C3Dianteira + C3Central + C3Traseira)+"kg.")
    print("Carga 4 {}".format(C4Dianteira + C4Central + C4Traseira)+"kg.")
    print("############################################################")
    print("Peso Total Na Parte Dianteira do Avião {}".format(C1Dianteira + C2Dianteira + C3Dianteira + C4Dianteira)+"kg.")
    print("Peso Total Na Parte Central do Avião {}".format(C1Central + C2Central + C3Central + C4Central)+"kg.")
    print("Peso Total Na Parte Traseira do Avião {}".format(C1Traseira + C2Traseira + C3Traseira + C4Traseira)+"kg.")
    print("############################################################")


def main():
    rand = Random()
    rand.seed(int(time()))

    ea = ec.GA(rand)
    ea.selector = ec.selectors.tournament_selection
    ea.variator = [ec.variators.uniform_crossover,
                   ec.variators.gaussian_mutation]
    ea.replacer = ec.replacers.steady_state_replacement

    ea.terminator = terminators.generation_termination
    ea.observer = [ec.observers.stats_observer, ec.observers.file_observer]

    final_pop = ea.evolve(generator=generate_,
                          evaluator=evaluate_,
                          pop_size=100000,
                          maximize=True,
                          bounder=ec.Bounder(0, 15000),
                          max_generation=100000,
                          num_inputs=12,
                          crossover_rate=1.0,
                          num_crossover_points=1,
                          mutation_rate=0.25,
                          num_elites=3,
                          num_selected=12,
                          tournament_size=12,
                          statistics_file=open('aviao_stats.csv', 'w'),
                          individuals_file=open('aviao_individuals.csv', 'w'))

    final_pop.sort(reverse=True)

    perform_fitness(final_pop[0].candidate[0], final_pop[0].candidate[1], final_pop[0].candidate[2], final_pop[0].candidate[3],
                    final_pop[0].candidate[4], final_pop[0].candidate[5], final_pop[0].candidate[6], final_pop[0].candidate[7],
                    final_pop[0].candidate[8], final_pop[0].candidate[9], final_pop[0].candidate[10], final_pop[0].candidate[11])
    
    solution_evaluation(final_pop[0].candidate[0], final_pop[0].candidate[1], final_pop[0].candidate[2], final_pop[0].candidate[3],
                    final_pop[0].candidate[4], final_pop[0].candidate[5], final_pop[0].candidate[6], final_pop[0].candidate[7],
                    final_pop[0].candidate[8], final_pop[0].candidate[9], final_pop[0].candidate[10], final_pop[0].candidate[11])

main()