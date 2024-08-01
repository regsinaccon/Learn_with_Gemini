from toolkit import kit
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
import re



def markdown_to_markup(md_text):
    # Convert Markdown bold (**text**) to Kivy bold ([b]text[/b])
    md_text = re.sub(r'\*\*(.*?)\*\*', r'[b]\1[/b]', md_text)
    # Convert Markdown italics (*text*) to Kivy italics ([i]text[/i])
    md_text = re.sub(r'\*(.*?)\*', r'[i]\1[/i]', md_text)
    # Add more conversions as needed
    return md_text

searching_word_explanation = ''

class Home(Screen):
    def __init__(self, **kw):
        super(Home,self).__init__(**kw)
        
        # initial layout
        home_layout = BoxLayout(orientation='vertical')
        self.top_space = Label()
        # home_layout.add_widget(self.top_space)
        self.buttom_space = Label()
        # search bar 
        search_bar = BoxLayout(orientation='horizontal')
        self.search_input = TextInput(font_size = 32)
        self.search_button = Button(text = 'search',font_size = 40,size_hint=(0.7,1))
        self.search_button.bind(on_press = self.search_word_onGe)
        search_bar.add_widget(self.search_input)
        search_bar.add_widget(self.search_button)


        # put things together
        home_layout.add_widget(self.top_space)
        home_layout.add_widget(search_bar)
        home_layout.add_widget(self.buttom_space)

        self.add_widget(home_layout)

    def search_word_onGe(self,instance):
        global searching_word_explanation
        ask = kit()
        question = self.search_input.text
        
        searching_word_explanation = markdown_to_markup(ask.add_and_show_word(question))
        self.manager.current = 'Explanation'

class Search_screen(Screen):
    def __init__(self, **kw):
        
        super(Search_screen,self).__init__(**kw)
        # two main part
        global searching_word_explanation
        
        panel = BoxLayout(orientation='horizontal',height=100)
        explanation_area = BoxLayout(height=600)
        content = BoxLayout(orientation='vertical')

        # building panel
        explanation_area.add_widget(Label(text='',markup=True))
        panel.add_widget(Button(text="Search",size_hint=(0.5,0.5),on_press=self.go_search))
        
        content.add_widget(panel)
        content.add_widget(explanation_area)
        

        self.add_widget(content)
        
    def go_search(self,instance):
        self.manager.current = "Search_area"


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Home(name = "Search_area"))
        sm.add_widget(Search_screen(name = "Explanation"))
        return sm 
if __name__ == "__main__":
    MyApp().run()

