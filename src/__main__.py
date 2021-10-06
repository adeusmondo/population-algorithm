import sys

from src.plot import BinaryBackpackPlot
from src.dataset import Dataset

if __name__ == "__main__":
    print("Running experiment...")
    if sys.argv[1] == '--debug':
        dataset = Dataset(
            description="", 
            capacity=7, 
            weights_objects=[6, 3, 5, 1, 1, 2, 3, 5, 6, 8, 4, 3, 3, 2, 1], 
            profits_objects=[5, 3, 2, 1, 4, 6, 3, 5, 1, 1, 2, 3, 5, 6, 8], 
            optimal_selection_weights=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )
        BinaryBackpackPlot(dataset=dataset).execute()
    elif sys.argv[1] == '-dt':
        reset_gen = False
        if len(sys.argv) >= 5:
            reset_gen = True if sys.argv[4] == "--reset-gen" else False

        BinaryBackpackPlot(dt_section=sys.argv[2]).execute(repeat=sys.argv[3], reset_gen=reset_gen)