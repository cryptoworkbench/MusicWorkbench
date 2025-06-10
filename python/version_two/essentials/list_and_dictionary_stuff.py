def _multiply_list(list_to_multiply: list, multiplier: int) -> list:
    if not list_to_multiply:
        raise ValueError("the list provided for multiplication cannot be empty!")
    if multiplier <= 0:
        raise ValueError("argument 'multiplier has to be a positive number!")
    ret_val = []
    for _ in range(multiplier):
        ret_val.extend(list_to_multiply)
    return ret_val

class methodized_dictionary(dict):
    def list_of_elements(self):
        for key, value in self.items():
            print(f"{key}: {value}")
