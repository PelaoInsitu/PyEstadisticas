#----------FRECUENCIAS----------


def get_unique_values(sorted_list):
    unique_values = list(set(sorted_list))
    return unique_values


def get_absolute_frequency(unique_values_list, list, n):
    dictionary = {}
    total = 0

    for value in unique_values_list:
        dictionary[value] = {"absolute_frequency": list.count(value)}
        total += list.count(value)
        print(f"Valor: {value}  -   {list.count(value)} veces")

    print(f"Total: {total}")
    if not total == n:
        raise ValueError("Error de cálculo al obtener frecuencia absoluta. El total no coincide")

    return dictionary


def get_relative_frequency(absolute_frecuency_dictionary, n):
    dictionary = {}
    total = 0

    for key in absolute_frecuency_dictionary:
        relative_frecuency = ((absolute_frecuency_dictionary[key]["absolute_frequency"]) / n)
        dictionary[key] = {"relative_frequency": relative_frecuency}
        total += relative_frecuency
        print(f"Valor: {key}  -   {relative_frecuency}")

    print(f"Total: {round(total, 2)}")

    return dictionary