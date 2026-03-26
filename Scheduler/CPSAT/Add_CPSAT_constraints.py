from ortools.sat.python import cp_model

class Contraint_adder:
    def __init__(interval_variables: dict[dict[str, list[any]]],
                 model: cp_model):