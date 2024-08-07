def calculate_structure_sum(data_structure):
    total_sum = 0
    def recursive_sum(element):
        nonlocal total_sum
        if isinstance(element, (int, float)):
            total_sum += element
        elif isinstance(element, str):
            total_sum += len(element)
        elif isinstance(element, list):
            for i in element:
                recursive_sum(i)
        elif isinstance(element, set):
            for i in element:
                recursive_sum(i)
        elif isinstance(element, dict):
            for key, value in element.items():
                recursive_sum(key)
                recursive_sum(value)
        elif isinstance(element, tuple):
            for i in element:
                recursive_sum(i)
    for i in data_structure:
        recursive_sum(i)

    return total_sum

data_structure = [ [1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)
