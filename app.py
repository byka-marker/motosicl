from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label





class Applica(App):

    def build(self):
        self.MainLayout = RelativeLayout()
        self.MainLayout.add_widget(Label(text="WTF"))
        return self.MainLayout


if __name__ == "__main__":
    Applica().run()