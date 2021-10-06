from dataclasses import dataclass
from typing import List


@dataclass
class Dataset:
    description: str
    capacity: int
    weights_objects: List[int]
    profits_objects: List[int]
    optimal_selection_weights: List[int]

    def __post_init__(self):
        self.validate_length()
        self.validate_optimal_selection_weights_items()

    @property
    def about(self):
        return f"Hi! I am {self.description}"

    @property
    def number_items(self):
        return len(self.weights_objects)

    def validate_length(self):
        if (len(self.weights_objects) != len(self.profits_objects)) or (len(self.weights_objects) != len(self.optimal_selection_weights)):
            raise ValueError(f"""The length of attr lists is inconsistent\n
Weights len: {len(self.weights_objects)}\n
Profits len: {len(self.profits_objects)}\n
Optimal Selection len: {len(self.optimal_selection_weights)}""")

    def validate_optimal_selection_weights_items(self):
        for i in self.optimal_selection_weights:
            if i not in [1, 0]:
                raise ValueError("The optimal selection weights numbers need be 0's or 1's")
