import time

from kivy.app import App
from kivy.lang import Builder
import show_function
from Telas_calculadora import *
from show_function import *
from botoes import *
from old_operation import Old_Operation
import os
from time import sleep

import sympy as sp
import math


GUI = Builder.load_file("files/main.kv")

class MyApp(App):
    old_operations_list = []
    Equation_mode_state = False

    def build(self):
         return GUI

    def write(self, string, *args):
        calculo_page_ids = self.root.ids["calculo_page"]
        tela_text = calculo_page_ids.ids["calculator_screen"].text
        if string == "(":
             if self.is_parenteses(tela_text) == True:
                 calculo_page_ids.ids["calculator_screen"].text += ")"
             else:
                 calculo_page_ids.ids["calculator_screen"].text += "("
        else:
            calculo_page_ids.ids["calculator_screen"].text += string
        self.copy_screen_text()




    def change_text(self, text):
       id_main = self.root.ids["calculo_page"]
       id_tela = id_main.ids["calculator_screen"]
       id_tela.text = text

    def copy_screen_text(self):
        calculo_page = self.root.ids["calculo_page"]
        calculator_screen = calculo_page.ids["calculator_screen"]
        other_keyboard_page = self.root.ids["other_keyboard"]
        other_screen_id = other_keyboard_page.ids["other_screen"]
        other_screen_id.text = calculator_screen.text



    def delete(self):
       calculo_page_ids = self.root.ids["calculo_page"]
       calculo_page_ids.ids["calculator_screen"].text = ""

    def is_parenteses(self, tela_text):
        if not tela_text:
            return False
        elif "(" in tela_text and tela_text[-1].isnumeric() == True:
            if ")" in tela_text:
                return False
            else:
                return True


    def make_operation(self, operation):
        try:
            new_operation = self.manage_operation(operation)
            sum = eval(new_operation)
            self.delete()
            self.write(f"{sum}")
            self.old_operations_list.append([operation, f"{sum}"])
            self.fill_operations(self.old_operations_list)
            self.old_operations_list = []
        except:
            self.change_text("ERROR")
            time.sleep(2)
            self.delete()
            pass



    def fill_operations(self, old_operations_list):
        operations_page_id = self.root.ids["operations_page"]
        old_operations_id = operations_page_id.ids["old_operations"]
        for operation in old_operations_list:
            old_operations_id.add_widget(Old_Operation(operation[0], operation[1]))


    def change_screen(self, id_screen):
        manager = self.root.ids["screen_manager"]
        manager.current = id_screen

    def manage_operation(self, operation):
        operation = operation.replace("x", "*")
        operation = operation.replace(",", ".")
        operation = operation.replace("^", "**")
        operation = self.manage_operation_more(operation)
        managed_operation = operation
        return managed_operation

    def manage_operation_more(self, string):
        for index, number in enumerate(string):
            if string[index].isnumeric() and string[index + 1] == "(":
                string = string.replace(f'{number}(', f'{number}*(')
                print(string)
                return string
            else:
                return string

    def compute_sqrt(self, string):
        print(list(enumerate(string)))

    def Equation_mode(self):
        calculo_page = self.root.ids['calculo_page']
        equation_button = calculo_page.ids['Equation_button']
        if self.Equation_mode_state == False:
            self.Equation_mode_state = True
            equation_button.color = (15 / 255, 242 / 255, 179 / 255)
        else:
            self.Equation_mode_state = False
            equation_button.color = (1, 1, 1, 1)




    def take_coeffs(self, equation):

        new_equation = self.trasnlate_equation(equation)

        # Defina as variáveis simbólicas
        x = sp.symbols('x')

        # Extrai automaticamente os coeficientes
        a, b, c = sp.Poly(new_equation, x).all_coeffs()
        return a, b, c

    def trasnlate_equation(self, equation):
        for number_index, number in enumerate(equation):
            if number == "x" and equation[number_index - 1].isnumeric() == True:
                equation = equation.replace(number, f'*{number}')
            elif number == "x" and equation[number_index - 1].isnumeric() == False:
                equation = equation.replace(number, f'1*{number}')

        return equation

    def solve_equation(self, equation):
        try:
            coff_a, coff_b, coff_c = self.take_coeffs(equation)
            delta = self.calculet_delta(coff_a, coff_b, coff_c)
            raiz_1, raiz_2 = self.sqrt_of_delta(coff_a, coff_b, delta)
            print(raiz_1, raiz_2)
            x, y = show_function.plot_function(coff_a, coff_b, coff_c, raiz_1, raiz_2)
            show_function.print_function(x, y, raiz_1, raiz_2)
            self.image_update()
        except:
            self.change_text("ERROR")
            pass
        else:
            self.change_screen("graph_page")





    def calculet_delta(self, coff_a, coff_b, coff_c):
        delta = coff_b ** 2 - (4 * coff_a * coff_c)
        return delta


    def sqrt_of_delta(self, coff_a, coff_b, delta):
        raiz_delta = math.sqrt(delta)
        if raiz_delta.is_integer():
            raiz_delta = int(raiz_delta)
            raiz_1 = (-coff_b + raiz_delta) / (2 * coff_a)
            raiz_2 = (-coff_b - raiz_delta) / (2 * coff_a)
            return raiz_1, raiz_2
        else:
            print("raiz de delta nao e exata")
            return 0, 0

    def erase(self, id_screen):
        try:
            screen = self.root.ids[id_screen]
            if id_screen == "calculo_page":
                calculator_screen = screen.ids["calculator_screen"]
            else:
                calculator_screen = screen.ids["other_screen"]
            screen_text = list(calculator_screen.text)
            screen_text[-1] = ""
            calculator_screen.text = "".join(screen_text)
        except:
            pass
        
    def image_update(self):
        graph_page = self.root.ids["graph_page"]
        graph_page.ids["graph_image"].reload()










MyApp().run()