from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
import re


class BuyScreen(BoxLayout, FocusBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.package = [['Number', 'B', 'S', '4A', '3A', '3ABC'],
                        ['Number', '4A', '4B', '4C', '4D', '4E'],
                        ['Box', 'B', 'S', '', '', ''],
                        ['iBox', 'B', 'S', '', '', ''],
                        ['PK', 'B', 'S', '', '', ''],
                        ['PB', 'B', 'S', '', '', ''],
                        ['HT', 'B', 'S', '', '', ''],
                        ['Number', '3A', '3B', '3C', '3D', '3E'],
                        ['Number', '2A', '2B', '2C', '2D', '2E']]

        self.package_status = 0         # Initial package is choose (first package)
        self.update_package(self.package[self.package_status])  # initialize the package
        self.textbox_instance = None    # initial object is None (object haven't created)
        self.bind_textbox()     # To bind the textbox input for the package

        #print(self.ids['display_screen'].width)
        #print(self.ids['display_screen'].height)

        self.keyboard_mode = 'managed'

        layout = GridLayout(cols=2, spacing='1dp', size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(100):
            #btn = Button(text=str(i), size_hint_y=None, height='35dp')
            layout.add_widget(self.add_button(i))
        root = ScrollView(size_hint=(1, 1))
        root.add_widget(layout)
        self.ids['display_screen'].add_widget(root)



    @staticmethod
    def on_double_tab(item):
        print(item)

    @staticmethod
    def add_textbox(textbox_id):
        textbox = TextInput(id=textbox_id,
                            height='40dp',
                            pos_hint='top',
                            size_hint_x=0.9,
                            multiline=False)
        return textbox

    @staticmethod
    def add_button(index):
        button_index = 'btn_'+ str(index)
        button = Button(id=button_index, size_hint_y=None, height='35dp',text=button_index)
        return button

    def display_screen(self):
        print(self.ids['display_screen'])

    def bind_textbox(self):
        for object_created in self.ids: # To get all the object(widget) created in the root
            print(f"{'Object: ': <7}"
                  f"{f'{object_created}': <18}"
                  f"{'Object location: ': <17}"
                  f"{f'{self.ids[object_created]}': >60}")

            # print('Object: ', object_created, '\t->Object location: ', self.ids[object_created])
            str_ids_dict = str(self.ids[object_created])  # convert the ids dict item into string for re.search
            found_textbox = re.search('TextInput', str_ids_dict)
            print(found_textbox)
            if found_textbox is not None:
                # print(re.search('TextInput', str_ids_dict))
                self.ids[object_created].bind(focus=self._on_focus)  # bind all found TextBox to _on_focus function

    # To get which current text box is focus and the current text input
    def _on_focus(self, instance, value, *largs):
        self.textbox_instance = instance
        self.hide_keyboard()
        self._keyboards = {}

        print('Current Instance: ', instance)
        #print('Current focused textbox', self.textbox_instance.text)

        print(self.keyboard_mode)   # auto
        print(self.keyboard)        # None
        print(self._keyboard)       # None
        print(self._keyboards)      # Keyboard and point to the textbox instance
        print(self._requested_keyboard)  # False
        print()

        # print('TextBox Text: ', type(instance.text))
        # print('TextBox object: ', instance)
        # print('TextBox Focus status: ', value)
        # print(type(largs))

    def delete_inp(self):  # DEL button pressed
        if self.textbox_instance is not None:  # textbox_instance haven't get any object when program start
            self.textbox_instance.text = self.textbox_instance.text[:-1]

    def clear_input(self):  # CLR button pressed
        # clear all input
        self.ids.number.text = ''
        self.ids.game_type_1.text = ''
        self.ids.game_type_2.text = ''
        self.ids.game_type_3.text = ''
        self.ids.game_type_4.text = ''
        self.ids.game_type_5.text = ''

    def update_package(self, package):
        print('update', package)
        add_space = ' '
        self.ids.number.hint_text = add_space + package[0]
        self.ids.game_type_1.hint_text = package[1]
        self.ids.game_type_2.hint_text = package[2]
        self.ids.game_type_3.hint_text = package[3]
        self.ids.game_type_4.hint_text = package[4]
        self.ids.game_type_5.hint_text = package[5]

        self.clear_input()
        # pass

    def previous_package(self):

        if self.package_status == 0:
            return
        else:
            print('previous package')
            self.package_status = self.package_status - 1
            self.update_package(self.package[self.package_status])

    def next_package(self):

        if self.package_status == len(self.package) - 1:
            return
        else:
            print('next package')
            self.package_status = self.package_status + 1
            self.update_package(self.package[self.package_status])


class BuyApp(App):
    def build(self):
        return BuyScreen()


if __name__ == '__main__':
    BuyApp().run()


    # def on_touch_down(self, touch): this function will overwrite other touch down unable to touch down
    # print(touch)


######################### Testing Keyboard #########################

        #print('keyboard mode now: ', self.keyboard_mode)
        #self.keyboard_mode = 'managed'
        #self.hide_keyboard()
        #self._keyboard_released()
        #print('keyboard mode after: ', self.keyboard_mode)

######################### Testing Keyboard #########################

'''
 print('keyboard before hide', self._keyboards)

        for keyboards in self._keyboards:
            self.keyboard = keyboards
            print('keyboard value: ', self._keyboards[keyboards])

        print('keyboard...: ', self.keyboard)
        #print(self.hide_keyboard)
        self.hide_keyboard()
        #self._unbind_keyboard()

        # for keyboard in self._keyboards:
        # print(self._keyboards[keyboard])
        # print(instance)
        print('keyboard after hide', self._keyboards)

        # pass

'''