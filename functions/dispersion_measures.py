from functions.central_tendency_measures import get_median
import numpy as np
import math
#----------MEDIDAS DE DISPERSIÓN----------


#Rango (amplitud)
def get_range(sorted_list):

    #Valor mínimo
    min_value = sorted_list[0]
    #Valor máximo
    max_value = sorted_list[-1]

    range = max_value - min_value

    return range


#Rango intercuartil
def get_interquartile_range(sorted_list):

    # Calcular el cuartil 1 (Q1)
    q1 = np.percentile(sorted_list, 25)
    #print(f'Cuartil 1: {q1}')

    # Calcular el cuartil 3 (Q3)
    q3 = np.percentile(sorted_list, 75)
    #print(f'Cuartil 3: {q3}')

    rango_inter = q3 - q1

    return rango_inter


#Varianza poblacional
def get_population_variance(sorted_list, n, arithmetic_mean):
    result = 0
    for i in sorted_list:
        result += (i - arithmetic_mean)**2
    result /=n

    return result


#Varianza muestral
def get_sample_variance(sorted_list, n, arithmetic_mean):
    result = 0
    for i in sorted_list:
        result += (i - arithmetic_mean)**2
    result /= (n - 1)

    return result


#Desviación estándar
def get_standard_deviation(variance):
    desviation =  math.sqrt(variance)
    return desviation


#Coeficiente de variación
def get_coefficient_of_variation(arithmetic_mean, standard_deviation):
    variation_coefficient = (standard_deviation / arithmetic_mean) * 100

    return variation_coefficient