import constants


def one_generation_iteration(total_population, population_with_advantage):
    general_population_left = (total_population - population_with_advantage) * (
            1 - constants.percentage_dies_before_reproduction / 100)*constants.number_of_children
    advantage_population_left = population_with_advantage * (1+constants.skill_advantage) * (
            1 - constants.percentage_dies_before_reproduction / 100)*constants.number_of_children
    return int(general_population_left + advantage_population_left), int(advantage_population_left)


def iterate():
    total_population = constants.starting_population
    population_with_advantage = constants.starting_population_with_advantage
    for i in range(constants.total_iteration):
        total_population, population_with_advantage = one_generation_iteration(total_population,
                                                                               population_with_advantage)
        if i % constants.number_of_iteration_for_result == 0:
            print("After iterations {0} total population {1} advantage population {2} ".format(i, total_population,
                  population_with_advantage))


if __name__ == "__main__":
    iterate()
