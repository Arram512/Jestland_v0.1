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


Window.size = (320, 600)



class HayrMerApp(MDApp):


    prkeq = """

            Կոդը ռան անելուց առաջ համոզվեք, որ աղոթել եք

                ************

            Հայր մեր որ յերկինս ես,
            սուրբ եղիցի անուն Քո։
            Եկեսցէ արքայութիւն Քո։
            Եղիցին կամք Քո
            որպէս յերկինս եւ յերկրի։
            Զհաց մեր հանապազորդ
            տուր մեզ այսօր։
            Եւ թող մեզ զպարտիս մեր,
            որպէս եւ մեք թողումք մերոց պարտապանաց։
            Եւ մի տանիր զմեզ ի փորձութիւն
            այլ փրկեա զմեզ ի չարէ։
            Զի քո է արքայութիւն
            եւ զօրութիւն եւ փառք յաւիտեանս
            Ամէն
            """

    def build(self):
        return Button(text = prkeq, on_release)
