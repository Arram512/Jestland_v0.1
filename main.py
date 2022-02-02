from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import TwoLineAvatarIconListItem, IRightBody
from kivymd.uix.button import MDIconButton
from kivy.lang.builder import  Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.properties import StringProperty, ObjectProperty, ListProperty
from kivy.uix.screenmanager import ScreenManager

import time


Window.size = (320, 600)

class ContactsScreen(BoxLayout):
	pass


class AboutScreen(BoxLayout):
    pass

class ItemScreenDrawer(GridLayout):

    text = StringProperty()
    source = StringProperty()

class ContentNavigationDrawer(BoxLayout):
 
    pass

class CardsDrawer(GridLayout):


    instance = ObjectProperty()
    source = StringProperty()
    text = StringProperty()
    method = ObjectProperty()


class MainWindow(MDBoxLayout):
    
    pass


#////////////////////////////////////////////////////////////////////////////////////////////////////

class Database:
    dictionary = {
    'instagram': 'img/giphy.gif',
    'twitter' : 'img/twitter.gif',
    'test' : 'img/twitter.gif',
    }


class CallBacks(Database):

	###################################################################################

	def favorite_back_button(self, instance):
		print(self.favorite_more_screen)

		self.root.ids.favorite_more_screen.remove_widget(self.favorite_more_screen)
		self.root.ids.favorite_screen_manager.current = 'favorite_screen'

	#*********************************************************************************#
	def alphavite_back_button(self, instance):

		print(self.scr)
		self.root.ids.more_screen.remove_widget(self.scr)
		self.root.ids.first_screen_manager.current = 'list_screen'

	#####################################################################################

	def draw_the_favorite_screen(self, instance):


		text = instance.text
		source = self.dictionary[text]

		self.root.ids.favorite_screen_manager.current = 'favorite_more'

		self.favorite_more_screen = ItemScreenDrawer(text = text, source = source)

		back_button = Button(text = 'back')
		back_button.bind(on_release = lambda x: self.favorite_back_button(instance))

		self.favorite_more_screen.add_widget(back_button)

		self.root.ids.favorite_more_screen.add_widget(self.favorite_more_screen)

	def draw_the_item_screen(self, instance):

		text = instance.text
		source = self.dictionary[text]

		self.root.ids.first_screen_manager.current = 'item_screen'

		screen = ItemScreenDrawer(text = text, source = source)
		favorite_button = Button(text = 'favorite')
		favorite_button.bind(on_release = lambda x: self.favorite(instance))

		back_button = Button(text = 'back')
		back_button.bind(on_release = lambda x: self.alphavite_back_button(instance))

		screen.add_widget(favorite_button)
		
		screen.ids.favorite_back_button_layout.add_widget(back_button)

		self.root.ids.more_screen.add_widget(screen)

		self.scr = screen


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        

class MainApp(MDApp, CallBacks):

    previouse_screen = ""

    def favorite(self, instance):

        print(instance)
        return self.root.ids.favorites.add_widget(CardsDrawer(instance = self, source = instance.source, text = instance.text, method = self.draw_the_favorite_screen))


    def on_start(self):

        for item in self.dictionary:

            source = self.dictionary[item]

            self.card = CardsDrawer(instance = self, source = source, text= item, method = self.draw_the_item_screen)

            self.root.ids.images.add_widget(self.card)




    def build(self):
        self.title = 'LearnApp'
        self.theme_cls.primary_palette = "BlueGray"  # "Purple", "Red"
        self.icon = 'Mobile-icon.png'
        return MainWindow()


if __name__ == '__main__':
    MainApp().run()