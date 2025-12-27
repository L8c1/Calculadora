from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button



class ChoiceBanner(FloatLayout):
    def __init__(self):
        super().__init__()

    def explanation_answer(self, id_button, *args):
        my_app = App.get_running_app()
        if id_button == "button_yes":
            my_app.Explanation = True
        else:
            my_app.Explanation = False





    question = Label(text="Vocé gostaria de uma explicação detalhada da operação?", size_hint=(0.50, 0.15),  pos_hint={"right": 0.75, "top": 0.25})

    buttons_grid = GridLayout()
    button_yes = Button(text="Sim", on_release=explanation_answer("buttons_yes"))
    button_no = Button(text="No", on_release=explanation_answer("button_no"))
    buttons_grid.add_widget(button_yes)
    buttons_grid.add_widget(button_no)


