"""
app-launcher.py

a mycroft skill that launches apps found on your computer.

By: Calacuda | MIT Licence | Epoch: 10/5/2020
"""


from adapt.intent import IntentBuilder 
from mycroft import MycroftSkill, intent_handler
import os.system as run


class Launcher(MycroftSkill):
    def __init__(self):
        super().__init__(self)

    def initialize(self):
         self.set_settings()

    def set_settings(self):
        #browser = self.settings.get('browser')
        #terminal = self.settings.get('terminal')
        apps = self.settings.get("Applications")
        
    def on_settings_changed(self):
        self.set_settings()

    @intent_handler('launch.Intent')
    def handle_launch__intent(self, app):
        speak(f"app is {app}")
        application = apps.get(app)
        speak(f"launching {application}")
        run(application)
        
    def stop(self):
        pass


def create_skill():
    return Launcher()
