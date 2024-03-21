from statistics import multimode

#----------MEDIDAS DE TENDENCIA CENTRAL (Media aritmética, Moda y Mediana)----------


#Obtener media aritmética
def get_arithmetic_mean(list):
    result = 0
    for i in list:
        result += i
    result /= len(list)
    return result


#Obtener moda/s
def get_mode(list):
    mode = multimode(list)
    return mode



#Obtener mediana
def get_median(sorted_list, n):

    if n % 2 == 1:
        #Lista con cantidad impar
        median = sorted_list[n // 2]
    
    else:
        #Lista con cantidad par
        value_sup = (n // 2)
        value_inf = (n // 2) - 1

        median = (sorted_list[value_inf] + sorted_list[value_sup]) / 2
    
    return median