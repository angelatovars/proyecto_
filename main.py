from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import requests

# Carga el archivo de estilos
Builder.load_file('styles.kv')

class BaseScreen(Screen):
    pass

class WelcomeScreen(BaseScreen):
    def switch_to_login(self):
        self.manager.current = 'login'

class LoginScreen(BaseScreen):
    def validar_login(self):
        email = self.ids.username.text
        password = self.ids.password.text
        error_label = self.ids.error_message
        error_label.text = ""

        try:
            # Hacer la solicitud POST a la API Flask para verificar el login
            response = requests.post('http://127.0.0.1:5000/login', json={
                'email': email,
                'password': password
            })
            
            if response.status_code == 200:
                # Inicio de sesión exitoso, cambia a la pantalla del dashboard
                self.manager.current = 'dashboard'
            else:
                error_label.text = "Correo electrónico o contraseña no válidos"
                print("Error de inicio de sesión:", response.json())
        except requests.exceptions.RequestException as e:
            error_label.text = "Error al conectar con la API"
            print(f"Error al conectar con la API: {e}")

    def switch_to_register(self):
        self.manager.current = 'register'

class RegisterScreen(BaseScreen):
    def register(self):
        full_name = self.ids.full_name.text
        email = self.ids.email.text
        password = self.ids.password.text
        confirm_password = self.ids.confirm_password.text

        if password == confirm_password:
            try:
                # Hacer la solicitud POST a la API para registrar el usuario
                response = requests.post('http://127.0.0.1:5000/usuarios', json={
                    'nombre_completo': full_name,
                    'email': email,
                    'password': password
                })
                
                if response.status_code == 201:
                    self.manager.current = 'registration_success'
                    # Limpia los campos
                    self.ids.full_name.text = ''
                    self.ids.email.text = ''
                    self.ids.password.text = ''
                    self.ids.confirm_password.text = ''
                else:
                    print("Error al registrar usuario:", response.json())
            except requests.exceptions.RequestException as e:
                print(f"Error al conectar con la API: {e}")
        else:
            print("Las contraseñas no coinciden")

    def switch_to_login(self):
        self.manager.current = 'login'

class RegistrationSuccessScreen(BaseScreen):
    def switch_to_login(self):
        self.manager.current = 'login'

class DashboardScreen(BaseScreen):  
    def logout(self):
        self.manager.current = 'welcome'

class MenteAprendeApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(RegistrationSuccessScreen(name='registration_success'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        return sm

if __name__ == '__main__':
    MenteAprendeApp().run()
