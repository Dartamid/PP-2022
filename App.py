from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition, SlideTransition
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera


Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '500 ')


class DataInput:
    count_variants = 0
    count_answer_options = 0
    count_question = 0
    order_answers = 0

    @staticmethod
    def print_all_data_input():
        print(f'Выбранное количество вариантов: {DataInput.count_variants}')
        print(f'Выбранное количество вриантов ответа: {DataInput.count_answer_options}')
        print(f'Выбранное количество вопросов: {DataInput.count_question}')
        print(f'Порядок ответов: {DataInput.order_answers}')


class TutorialPageOne(Screen):

    @staticmethod
    def switch_next_screen():
        TestApp.screen_manager.transition = SlideTransition(direction='left')
        TestApp.screen_manager.current = 'tutorial_page_2'

    @staticmethod
    def skip_tutorial():
        TestApp.screen_manager.transition = FadeTransition()
        TestApp.screen_manager.current = 'constructor_page_1'


class TutorialPageTwo(Screen):

    @staticmethod
    def switch_next_screen():
        TestApp.screen_manager.transition = SlideTransition(direction='left')
        TestApp.screen_manager.current = 'tutorial_page_3'

    @staticmethod
    def switch_screen_back():
        TestApp.screen_manager.transition = SlideTransition(direction='right')
        TestApp.screen_manager.current = 'tutorial_page_1'

    @staticmethod
    def skip_tutorial():
        TestApp.screen_manager.transition = FadeTransition()
        TestApp.screen_manager.current = 'constructor_page_1'


class TutorialPageThree(Screen):

    @staticmethod
    def switch_next_screen():
        TestApp.screen_manager.transition = SlideTransition(direction='left')
        TestApp.screen_manager.current = 'tutorial_page_4'

    @staticmethod
    def switch_screen_back():
        TestApp.screen_manager.transition = SlideTransition(direction='right')
        TestApp.screen_manager.current = 'tutorial_page_2'

    @staticmethod
    def skip_tutorial():
        TestApp.screen_manager.transition = FadeTransition()
        TestApp.screen_manager.current = 'constructor_page_1'


class TutorialPageFour(Screen):

    @staticmethod
    def switch_next_screen():
        TestApp.screen_manager.transition = SlideTransition(direction='left')
        TestApp.screen_manager.current = 'tutorial_page_5'

    @staticmethod
    def switch_screen_back():
        TestApp.screen_manager.transition = SlideTransition(direction='right')
        TestApp.screen_manager.current = 'tutorial_page_3'

    @staticmethod
    def skip_tutorial():
        TestApp.screen_manager.transition = FadeTransition()
        TestApp.screen_manager.current = 'constructor_page_1'


class TutorialPageFive(Screen):

    @staticmethod
    def switch_to_constructor():
        TestApp.screen_manager.transition = FadeTransition()
        TestApp.screen_manager.current = 'constructor_page_1'

    @staticmethod
    def switch_screen_back():
        TestApp.screen_manager.transition = SlideTransition(direction='right')
        TestApp.screen_manager.current = 'tutorial_page_4'


class ConstructorPageOne(Screen):

    def switch_next_screen(self):
        TestApp.screen_manager.transition = SlideTransition(direction='left')
        TestApp.screen_manager.current = 'constructor_page_2'
        DataInput.count_question = self.ids.count_question_input.text

    @staticmethod
    def switch_back_to_tutorial():
        TestApp.screen_manager.transition = FadeTransition()
        TestApp.screen_manager.current = 'tutorial_page_1'

    @staticmethod
    def on_click_checkbox_answers(instance, value):
        if instance:
            DataInput.count_answer_options = value

    @staticmethod
    def on_click_checkbox_variants(instance, value):
        if instance:
            DataInput.count_variants = value


class ConstructorPageTwo(Screen):

    @staticmethod
    def switch_screen_back():
        TestApp.screen_manager.transition = SlideTransition(direction='right')
        TestApp.screen_manager.current = 'constructor_page_1'

    def switch_to_check_data_page(self):
        TestApp.screen_manager.transition = FadeTransition()
        TestApp.screen_manager.current = 'check_data_page_1'
        DataInput.order_answers = self.ids.order_answers_input.text
        DataInput.print_all_data_input()


class CheckDataPage(Screen):
    pass


class CameraPage(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class TestApp(App):
    screen_manager = ScreenManager()

    def build(self):
        Builder.load_file('ScrManager.kv')
        self.screen_manager.add_widget(TutorialPageOne(name='tutorial_page_1'))
        self.screen_manager.add_widget(TutorialPageTwo(name='tutorial_page_2'))
        self.screen_manager.add_widget(TutorialPageThree(name='tutorial_page_3'))
        self.screen_manager.add_widget(TutorialPageFour(name='tutorial_page_4'))
        self.screen_manager.add_widget(TutorialPageFive(name='tutorial_page_5'))
        self.screen_manager.add_widget(ConstructorPageOne(name='constructor_page_1'))
        self.screen_manager.add_widget(ConstructorPageTwo(name='constructor_page_2'))
        # self.screen_manager.add_widget(CameraPage(name='camera_page'))
        self.screen_manager.add_widget(CheckDataPage(name='check_data_page_1'))
        return self.screen_manager


if __name__ == '__main__':
    TestApp().run()
