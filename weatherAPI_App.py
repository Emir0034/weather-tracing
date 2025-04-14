import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

deneme1 = 10
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        #self.setGeometry(750, 400, 400, 400)
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
                            QLabel, QPushButton{
                                font-family: calibri;    
                           }
                           QLabel#city_label{
                                font-size: 40px;
                                font-style: italic
                           }
                           QLineEdit#city_input{
                                font-size: 40px;
                           }
                           QPushButton#get_weather_button{
                                font-size: 30px;
                                font-weight: bold
                           }
                           QLabel#temperature_label{
                                font-size: 75px;
                           }
                           QLabel#emoji_label{
                                font-size: 100px;
                                font-family: Segoe UI emoji;
                           }
                           QLabel#description_label{
                                font-size: 50px;
                           }
                           """)
        
        self.get_weather_button.clicked.connect(self.get_weather)
    
    
    def get_weather(self):
        api_key = "1f9ef3df13d2712ff341b816d1faad82"
        city_name = self.city_input.text()

        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial"
            response = requests.get(url)
            response.raise_for_status()
            print(response)
            weather_data = response.json()
            if weather_data["cod"] == 200:
                weather_temperature_c = (weather_data["main"]["temp"])
                self.temperature_label.setText(f"{weather_temperature_c:.1f} °C")
                weather_info = weather_data["weather"][0]["description"]
                self.description_label.setText(weather_info)
                weather_id = weather_data["weather"][0]["id"]
                self.emoji_label.setText(self.get_weather_emoji(weather_id))
                print(weather_info)
        except requests.exceptions.HTTPError as error:
            #print(f"Error: {error}")
            print(f"Error code: {response.status_code}")
        except requests.exceptions.RequestException as req_err:
            print(f"Request error: {req_err}")


    def display_error(self):
        pass

    def display_weather(self):
        pass

    @staticmethod
    def get_weather_emoji(weather_id):
        """
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "⛅"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"  
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "🌬️"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""
            """
        pass


def get_weather_info(location):
    base_url = "https://api.openweathermap.org/data/3.0/onecall?"
    #API_key = "1f9ef3df13d2712ff341b816d1faad82"
    #url = f"https://api.openweathermap.org/data/3.0/onecall?appid={API_key}"
    #response = requests.get(url)
    #print(response)

def main():
    get_weather_info("deneme")

if __name__ == "__main__":
    #main()
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())