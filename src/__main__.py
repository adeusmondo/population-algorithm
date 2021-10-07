import sys

from src.plot import BinaryBackpackPlot
from src.dataset import Dataset

if __name__ == "__main__":
    print("Running experiment...")
    if sys.argv[1] == '--debug':
        dataset = Dataset(
            description="", 
            capacity=7, 
            weights_objects=[6,3,5,1,1,2,3,5,6,8,4, 3, 3, 2, 1], 
            profits_objects=[5, 3, 2, 1, 4,6,3,5,1,1,2,3,5,6,8], 
            optimal_selection_weights=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )
        BinaryBackpackPlot(dataset=dataset).execute()
    elif sys.argv[1] == '-dt':
        dt_section = 'one'
        if len(sys.argv) >= 3:
            dt_section = sys.argv[2]

        repeat = 1
        if len(sys.argv) >= 4:
            repeat = int(sys.argv[3])       

        BinaryBackpackPlot(dt_section=dt_section).execute(repeat=repeat)