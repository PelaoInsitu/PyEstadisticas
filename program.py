from utilities import *
from functions.central_tendency_measures import *
from functions.dispersion_measures import *
from functions.frecuency import *
import sys

class Program:

    #Lista en bruto
    list = []
    #Lista ordenada
    sorted_list = []
    #Cantidad de datos
    quantity = 0
    #Opción de menú (poblacional o muestral)
    option = 0
    #Valores únicos (para frecuencia)
    unique_values = []


    @classmethod
    def start(cls):
        '''Método para arrancar el programa. Muestra el menú inicial para ingresar los datos'''

        simple_bar()
        title("Script para medidas estadísticas")
        simple_bar()
        print()
        

        while True:
            print('Escriba: \n"done" para continuar / "exit" para cancelar.')
            value = input("Ingrese un número a la lista: ")
            print()

            if value == "exit":
                sys.exit()

            if value == "done":
                while True:
                    simple_bar()
                    title("Opciones de cálculo")
                    simple_bar()
                    print("")
                    
                    print("1. Poblacional \n2. Muestral")
                    try:
                        cls.option = int(input("Seleccione un tipo de cálculo: "))
                        break
                    except ValueError:
                        print("Error: Por favor, ingrese un número entero.")
                    
                print()
                print()
                break

            if value.isalpha():
                print("Entrada incorrecta")
            else:
                cls.list.append(int(value))

    

    @classmethod
    def execute(cls):
        '''Este método se ejecuta cuando se termina de ingresar los datos. Llama a todas las funciones para realizar los cálculos'''

        if not cls.list == None:

            simple_bar()
            if cls.option == 1:
                title("Cálculo Poblacional")
            else:
                title("Cálculo Muestral")
            simple_bar()
            print()

            #Ordenar lista
            cls.sorted_list = sort_list(cls.list)
            #Cantidad de datos en la lista
            cls.quantity = len(cls.sorted_list)

            simple_bar()
            print(f"Lista:                  {cls.list}")
            print(f"Lista ordenada:         {cls.sorted_list}")
            print(f"Cantidad de datos:      {cls.quantity}")
            simple_bar()
            print("Medidas de tendencia central")
            print()


            #-----MEDIDAS DE TENDENCIA CENTRAL-----
            #Media aritmética
            arithmetic_mean = get_arithmetic_mean(cls.list)
            print(f"Media aritmética:       {arithmetic_mean}")

            #Moda
            mode = get_mode(cls.list)
            print(f"Moda:                   {mode}")

            #Mediana
            median = get_median(cls.sorted_list, cls.quantity)
            print(f"Mediana:                {median}")

            print()
            simple_bar()


            #-----MEDIDAS DE DISPERSIÓN-----
            #Rango
            range = get_range(cls.sorted_list)
            print(f'Rango:                  {range}')

            #Rango intercuartil
            interquartile_range = get_interquartile_range(cls.sorted_list)
            print(f'Rango intercuartil:     {interquartile_range}')


            if cls.option == 1:
                #Varianza poblacional (profe)
                variance = get_population_variance(cls.sorted_list, cls.quantity, arithmetic_mean)
                print(f'Varianza pobl:          {round(variance, 2)}')
            else:
                #Varianza muestral
                variance = get_sample_variance(cls.sorted_list, cls.quantity, arithmetic_mean)
                print(f'Varianza muestral:      {round(variance, 2)}')


            #Desviación estándar o típica
            standard_deviation = get_standard_deviation(variance)
            print(f"Desviación típica:      {round(standard_deviation, 2)}")

            #Coeficiente de variación
            coefficient_of_variation = get_coefficient_of_variation(arithmetic_mean, standard_deviation)
            print(f"Coef. variación:        {round(coefficient_of_variation, 2)}%")

            print()
            simple_bar()


            #-----FRECUENCIAS-----
            #Valores únicos
            cls.unique_values = get_unique_values(cls.sorted_list)
            print(f"Valores únicos: {cls.unique_values}")

            print()
            simple_bar()

            #Frecuencia absoluta
            print(f"Frecuencia Absoluta")
            absolute_frecuency_dictionary = get_absolute_frequency(cls.unique_values, cls.list, cls.quantity)

            print()
            simple_bar()

            #Frecuencia relativa
            print(f"Frecuencia relativa")
            relative_frecuency_dictionary = get_relative_frequency(absolute_frecuency_dictionary, cls.quantity)
        
        else:
            pass