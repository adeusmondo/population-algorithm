from config import ReaderConfig
import random

class BinaryBackpack(ReaderConfig):
    def __init__(
            self, 
            penality = 25, 
            population_size = 4, 
            total_amount_valuations = 30, 
            percentage_performing_mutation = 3,
            dt_section = "one",
            dataset = None
        ):
        super().__init__()
        if dataset:
            self.dataset = dataset
        else:
            self.dataset = self.load(dt_section=dt_section)
            
        self.penality = penality
        self.population_size = population_size
        self.total_amount_valuations = total_amount_valuations
        self.percentage_performing_mutation = percentage_performing_mutation
        self._dt_section = dt_section
        self.reset_params()
        
    def reset_params(self):
        self._solution_size = len(self.dataset.profits_objects)
        self._current_amount_valuations = 0
        self._population = []
        self._next_population = []
        self._fitness = [0] * self.population_size
        self._fitness_next_population = [0] * (self.population_size + 1)
        self._index_best_solution = 0
        self._index_worst_solution = 0

        for i in range(self.population_size):
            self._population.append([0] * self._solution_size)
            self._next_population.append([0] * self._solution_size)

        self._next_population.append([0] * self._solution_size)

    def objective_function(self, solution):
        _fitness = 0
        _weight = 0

        for i in range(len(solution)):
            _fitness += (
                solution[i] * self.dataset.profits_objects[i]
            )
            _weight += (
                solution[i] * self.dataset.weights_objects[i]
            )

        if (_weight > self.dataset.capacity):
            _fitness -= self.penality

        return _fitness

    def generate_initial_solution(self):
        for i in range(self.population_size):
            for j in range(self._solution_size):
                self._population[i][j] = random.randint(0, 1)

    def evaluate_solution(self, i):
        self._fitness[i] = self.objective_function(self._population[i])

    def evaluate_population(self):
        for i in range(self.population_size):
            self.evaluate_solution(i)
        
    def identify_better_solution(self):
        _index_best_solution = 0
        for i in range(self.population_size):
            if self._fitness[_index_best_solution] < self._fitness[i]:
               _index_best_solution = i
        
        return _index_best_solution

    def crossover(self, i) -> None:
        new_l = []
        new_q = []
        l = self._population[i]
        q = self._population[-2]

        print("Ponto de Corte")
        k = random.randint(0, self._solution_size)
        
        for i in range(self._solution_size):
            if i <= k:
                new_l.append(l[i])
                new_q.append(q[i])
            else:
                new_l.append(q[i])
                new_q.append(l[i])
                
        self._population[i] = new_l
        self._population[-2] = new_q

    def elitism(self) -> None:
        _index_best_solution = self.identify_better_solution()
        self._next_population[self.population_size] = self._population[_index_best_solution]
        self._fitness_next_population[self.population_size] = self._fitness[_index_best_solution]

    def mutation(self, i):
        for j in range(self._solution_size):
            if random.randint(0, 100) <= self.percentage_performing_mutation:
                if self._population[i][j] == 0:
                    self._next_population[i][j] = 1
                else:
                    self._next_population[i][j] = 0
            else:
                self._next_population[i][j] = self._population[i][j]

    def identify_worst_solution_next_population(self):
        _index_worst_solution = 0
        for i in range(self.population_size + 1):
            if self._fitness_next_population[_index_worst_solution] > self._fitness_next_population[i]:
                _index_worst_solution = i

        return _index_worst_solution

    def identify_worst_solution_current_population(self):
        _index_worst_solution = 0
        for i in range(self.population_size):
            if self._fitness[_index_worst_solution] > self._fitness[i]:
                _index_worst_solution = i
        
        return _index_worst_solution

    def generate_next_population(self):
        _worse = self.identify_worst_solution_next_population()
        del self._next_population[_worse]
        del self._fitness_next_population[_worse]

        _population = self._next_population
        _fitness = self._fitness_next_population

        self._next_population.append(self._next_population[0])
        self._fitness_next_population.append(self._fitness_next_population[0])

    def stop_criterion_reached(self, current_amount_valuations):
        return current_amount_valuations >= self.total_amount_valuations

    def report_convergence_generation(self):
        self._best_fitness_generation.append(self._fitness[self.identify_better_solution()])
        self._worst_fitness_generation.append(self._fitness[self.identify_worst_solution_current_population()])

        _avg = 0
        for i in self._fitness:
            _avg += i

        self._avg_fitness_generation.append(_avg/len(self._fitness))

    def execute(self, repeat = 1):
        self._best_fitness = []
        self._avg_fitness = []
        self._worst_fitness = []

        self._best_fitness_generation = []
        self._avg_fitness_generation = []
        self._worst_fitness_generation = []
        _repeat_counter = 0

        while not _repeat_counter >= repeat:
            self.generate_initial_solution()
            self.evaluate_population()

            self._current_amount_valuations = self.population_size
            self.report_convergence_generation()

            _counter = 0
            while not self.stop_criterion_reached(self._current_amount_valuations):
                self.elitism()
                for i in range(self.population_size):
                    self.crossover(i)
                    self.mutation(i)
                    self._fitness_next_population[i] = self.objective_function(self._next_population[i])
                    self._current_amount_valuations += 1
                
                self.generate_next_population()
                self.report_convergence_generation()
                _counter += 1
            
            _best_solution = self.identify_better_solution()
            _worst_soluiton = self.identify_worst_solution_current_population()
            _avg_solution = (self._fitness[_best_solution] + self._fitness[_worst_soluiton]) / 2

            self._best_fitness.append(self._fitness[_best_solution])
            self._avg_fitness.append(_avg_solution)
            self._worst_fitness.append(self._fitness[_worst_soluiton])

            _repeat_counter += 1

        