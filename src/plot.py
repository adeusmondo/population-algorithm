from src.algorithm import BinaryBackpack

import pathlib
import statistics

import matplotlib.pyplot as plt
import numpy as np

class BinaryBackpackPlot(BinaryBackpack):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def plot_population_convergence(self):
        fig = plt.figure(figsize =(15, 10))
        ax = plt.axes()

        plt.title("Convergência da população")
        plt.xlabel("Geração")
        plt.ylabel("Fitness")

        ax.plot(self._best_fitness, label="Melhor")
        ax.plot(self._avg_fitness, label="Média")
        ax.plot(self._worst_fitness, label="Pior")
        ax.grid(False)
        plt.savefig(f"output/plot_population_convergence_{self._dt_section}.jpg", bbox_inches='tight', dpi=150)
        plt.close() 
        
    def plot_box_plot(self):
        fitness = [
            self._best_fitness,
            self._avg_fitness,
            self._worst_fitness
        ]
        font_1 = {'family':'serif', 'color':'#993556'}
        font_2 = {'family':'serif', 'color':'#5C1BCC'}
        font_3 = {'family':'serif', 'color':'000', 'size':12}
        
        fig = plt.figure(figsize =(15, 10))
        ax = plt.axes()

        tl = ax.set_title("Box Plot")
        tl = ax.set_ylabel("Fitness")
        tl = ax.set_xlabel("Gerações")

        for i in range(0, len(fitness)):
            plt.text(i + 1, min(fitness[i]), '{0:.2f}'.format(min(fitness[i])), fontdict=font_1)
            plt.text(i + 1, statistics.mean(fitness[i]), '{0:.2f}'.format(statistics.mean(fitness[i])), fontdict=font_2)
            plt.text(i + 1, max(fitness[i]), '{0:.2f}'.format(max(fitness[i])), fontdict=font_1)
        
        bp = ax.boxplot(x=fitness, labels=["Melhor", "Média", "Pior"])
        ax.grid(False)
        plt.savefig(f"output/plot_box_plot_{self._dt_section}.jpg", bbox_inches='tight', dpi=150)
        plt.close() 

    def plot_error_bar(self):
        arrys = [
            ("best_fitness", self._best_fitness),
            ("avg_fitness", self._avg_fitness),
            ("worst_fitness", self._worst_fitness),
        ]
        for name, data in arrys:
            x = np.array(data)
            y = np.power(x, 2) # Effectively y = x**2
            error = 0.1 + 0.2 * x
            plt.errorbar(x, y, error, linestyle='None', marker='^')

            plt.savefig(f"output/plot_{name}_error_bar_{self._dt_section}.jpg", bbox_inches='tight', dpi=150)
            plt.close() 

    def execute(self, **kwargs):
        super().execute(**kwargs)
        self.plot_population_convergence()
        self.plot_box_plot()
        self.plot_error_bar()