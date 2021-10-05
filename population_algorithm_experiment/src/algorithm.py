from config import reader_config

class BinaryBackpack:
    def __init__(
            self, 
            penality = 20, 
            population_size = 4, 
            total_amount_valuations = 20, 
            percentage_performing_mutation = 3,
            dataset = "one",
        ):
        self.datasets = reader_config()

        self.backpack_size = len(self.dataset.get(dataset).get('weights_objects'))
        self.penality = penality

        self._fitness = 0
        self._
        self.population_size = population_size
        self.total_amount_valuations = total_amount_valuations
        self.percentage_performing_mutation = percentage_performing_mutation
        self._current_amount_valuations = 0


    def load(self):
        self.dataset = reader_config()

    def objective_function(self, solution):
        fitness = 0
        weight = 0

        for idx in range(len(solution)):
            fitness += (solution[idx] * self.dataset.get('profits_objects')[idx])
            weight += (solution[idx] * self.dataset.get('weights_objects')[idx])

        if (weight > self.backpack_size):
            fitness -= self.penality

        return fitness

    def execute():
