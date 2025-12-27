from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout




class Old_Operation(GridLayout):


    def __init__(self, operation, result):
        self.rows = 2
        super().__init__()

        main_operation = operation
        result_of_operation = result

        operation_GUI = FloatLayout()

        operation_pos = Label(text=f"operação: {main_operation}", size_hint=(0.25, 0.25), pos_hint={"right": 1, "top": 1})
        
        operation_GUI.add_widget(operation_pos)
        
        result_GUI = FloatLayout()

        result_pos = Label(text=f"resultado: {result_of_operation}", size_hint=(0.25, 0.25), pos_hint={"right": 1, "top": 1})

        result_GUI.add_widget(result_pos)

        self.add_widget(operation_GUI)
        self.add_widget(result_GUI)
