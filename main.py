from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker
import random
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivymd.uix.behaviors import TouchBehavior
import time
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window

Window.clearcolor = (.1, .5, 1, 1)


value = 0
amount = 0

Builder.load_file('template.kv')


class MenuScreen(Screen):
    def checked(self, instance, value):
        print(value)

    def main(self):
        number = self.ids.name_input.text

        self.ids.list_label.text = number

        self.ids.name_input.text = ""

    def job2(self, instance, value):
        number = self.ids.name_input.text

        self.ids.list_label.text = number

        self.ids.name_input.text = ""

    def deletetodo(self):
        self.ids.list_label.text = ''

    def play_sound(self):
        sound = SoundLoader.load('study.mp3')
        if sound:
            sound.play()


class SettingsScreen(Screen):
    def register(self):
        f = open('data.txt', 'a')
        f.write(self.ids.user_input.text + '\n')
        f.close()


class AgendaScreen(Screen):
    def show_date_picker(self):
        pass

class Overhoren(Screen):
    def overhoren(self):
        global woordje
        global randomwoordje

        lines = open('data.txt').read().splitlines()
        randomwoordje = random.choice(lines)

        woordje = randomwoordje.split('=')

        self.ids.list_vraag.text = woordje[0]

    def antwoord(self):

        try:
            awnser = self.ids.antwoordinput.text

            if awnser == woordje[1]:
                self.ids.list_vraag.text = "Goed"

            else:
                self.ids.list_vraag.text = "Fout Het goede Antwoord is: " + woordje[1]
                false_words = open("WRONG.txt", 'a')
                false_words.write(randomwoordje + '\n')
                false_words.close()


            self.ids.antwoordinput.text = ""
        except:
            pass

class Overhoren1(Screen):
    def overhoren1(self):
        global woordje
        global randomwoordje

        lines = open('WRONG.txt').read().splitlines()
        randomwoordje = random.choice(lines)

        woordje = randomwoordje.split('=')

        self.ids.list_vraag.text = woordje[0]

    def antwoord1(self):

        try:
            awnser = self.ids.antwoordinput.text

            if awnser == woordje[1]:
                self.ids.list_vraag.text = "Goed"

            else:
                self.ids.list_vraag.text = "Fout Het goede Antwoord is: " + woordje[1]
                false_words = open("WRONG.txt", 'a')
                false_words.write(randomwoordje + '\n')
                false_words.close()


            self.ids.antwoordinput.text = ""
        except:
            pass

class calculator(Screen):
    def calculator(self):
        global value
        global amount

        numbers = self.ids.antwoordinput1.text + '-' + self.ids.antwoordinput2.text + '-' + self.ids.antwoordinput3.text + '-' + self.ids.antwoordinput4.text + '-' + self.ids.antwoordinput5.text + '-' + self.ids.antwoordinput6.text + '-' + self.ids.antwoordinput7.text + '-' + self.ids.antwoordinput8.text + '-' + self.ids.antwoordinput9.text + '-' + self.ids.antwoordinput10.text

        eerste_splid = numbers.split('-')
        for lines in eerste_splid:
            tweede_splid = lines.split(' ')
            try:
                cijfer1 = int(tweede_splid[0]) * int(tweede_splid[1])

                value += cijfer1
                amount += int(tweede_splid[1])

            except:
                pass

        gem = value / amount

        self.ids.gemmidelde.text = "Gemidelde: " + str(gem)
        value = 0
        amount = 0

class september(Screen, App):
    def addjobsep(self, instance):
        global ids

        id1 = instance.text
        ids = id1 + ' September'


class juli(Screen, App):
    def addjobjul(self, instance):
        global ids

        id1 = instance.text
        ids = id1 + ' Juli'
class oktober(Screen, App):
    def addjobokt(self, instance):
        global ids

        id1 = instance.text
        ids = id1 + ' Oktober'
class november(Screen, App):
    def addjobnov(self, instance):
        global ids

        id1 = instance.text
        ids = id1 + ' November'
class december(Screen, App):
    def addjobdec(self, instance):
        global ids

        id1 = instance.text
        ids = id1 + ' december'
class januari(Screen, App):
    def addjobjan(self, instance):
        global ids

        id1 = instance.text
        ids = id1 + ' Januari'
class februari(Screen, App):
    def addjobfeb(self, instance):
        global ids

        id1 = instance.text
        ids = id1 + ' februari'
class maart(Screen, App):
    def addjobma(self, instance):
        global ids

        id1 = instance.text
        ids = id1 + ' maart'
class april(Screen, App):
    def addjobap(self, instance):
        global ids

        id1 = instance.text
        ids = id1 + ' april'
class mei(Screen, App):
    def addjobmei(self, instance):
        global ids

        id1 = instance.text
        ids = id1 + ' mei'
class juni(Screen):
    def addjobjuni(self, instance):
        global ids

        id1 = instance.textR
        ids = id1 + ' juni'

class addjob(Screen):
    def addnewjob(self):
        job = self.ids.input.text
        print(job)

        f = open('jobstodo.txt', 'a')
        f.write('- ' + job + '\n')

class askjob(Screen):
    pass

class checkjob(Screen):
    def checkcurrentjobs(self):
        f = open('jobstodo.txt', 'r')
        lines = f.read()

        self.ids.list_label.text = str(lines)



class LearnAppApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(AgendaScreen(name='agenda'))
        sm.add_widget(Overhoren(name='overhoren'))
        sm.add_widget(Overhoren1(name='overhoren1'))
        sm.add_widget(calculator(name='calculator'))
        sm.add_widget(september(name='september'))
        sm.add_widget(juli(name="juli"))
        sm.add_widget(oktober(name='oktober'))
        sm.add_widget(november(name='november'))
        sm.add_widget(december(name='december'))
        sm.add_widget(januari(name='januari'))
        sm.add_widget(februari(name='februari'))
        sm.add_widget(maart(name='maart'))
        sm.add_widget(april(name='april'))
        sm.add_widget(mei(name='mei'))
        sm.add_widget(juni(name='juni'))
        sm.add_widget(addjob(name='addjob'))
        sm.add_widget(askjob(name='askjob'))
        sm.add_widget(checkjob(name='checkjob'))
        return sm


if __name__ == '__main__':
    LearnAppApp().run()