from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super(DashboardScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        # Crear botones para el menú
        profile_btn = Button(text='Perfil', size_hint=(1, 0.2), background_color=(0.3, 0.5, 0.7, 1))
        settings_btn = Button(text='Configuraciones', size_hint=(1, 0.2), background_color=(0.3, 0.5, 0.7, 1))
        progress_btn = Button(text='Progreso', size_hint=(1, 0.2), background_color=(0.3, 0.5, 0.7, 1))
        logout_btn = Button(text='Cerrar sesión', size_hint=(1, 0.2), background_color=(0.3, 0.5, 0.7, 1))

        # Añadir botones al layout
        layout.add_widget(profile_btn)
        layout.add_widget(settings_btn)
        layout.add_widget(progress_btn)
        layout.add_widget(logout_btn)

        self.add_widget(layout)

        # Conectar botones a funciones
        profile_btn.bind(on_press=self.go_to_profile)
        settings_btn.bind(on_press=self.go_to_settings)
        progress_btn.bind(on_press=self.go_to_progress)
        logout_btn.bind(on_press=self.logout)

    def go_to_profile(self, instance):
        print("Ir a Perfil")
        # Aquí se puede añadir la lógica para cambiar a la pantalla del perfil

    def go_to_settings(self, instance):
        print("Ir a Configuraciones")
        # Aquí se puede añadir la lógica para cambiar a la pantalla de configuraciones

    def go_to_progress(self, instance):
        print("Ir a Progreso")
        # Aquí se puede añadir la lógica para cambiar a la pantalla de progreso

    def logout(self, instance):
        print("Cerrar sesión")
        self.manager.current = 'welcome'

class MenteAprendeApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(DashboardScreen(name='dashboard'))
        return sm

if __name__ == '__main__':
    MenteAprendeApp().run()
