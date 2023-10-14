from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PySide6.QtGui import QPixmap, QImage
import requests
from display_window import DisplayWindow  

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.pokemon_data = {}
        self.initUI()
        self.api_url = "https://pokeapi.co/api/v2/pokemon/"

    def initUI(self):
        self.setFixedSize(850, 500)
        self.setWindowTitle("Pokédex")

        bg_image = QImage("../assets/landing.jpg")
        bg_pixmap = QPixmap.fromImage(bg_image)
        bg_label = QLabel(self)
        bg_label.setPixmap(bg_pixmap)
        bg_label.setGeometry(0, 0, 850, 500)

        layout = QVBoxLayout()

        label1 = QLabel("Enter the Pokémon name:", self)
        layout.addWidget(label1)

        self.textbox = QLineEdit(self)
        layout.addWidget(self.textbox)

        search_button = QPushButton("Search", self)
        search_button.clicked.connect(self.search_pokemon)
        layout.addWidget(search_button)

        capture_button = QPushButton("Capture", self)
        capture_button.clicked.connect(self.capture_pokemon)
        layout.addWidget(capture_button)

        display_button = QPushButton("Display", self)
        display_button.clicked.connect(self.open_display_window)
        layout.addWidget(display_button)

        self.result_label = QLabel(self)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def search_pokemon(self):
        pokemon_name = self.textbox.text()
        if pokemon_name:
            try:
                response = requests.get(self.api_url + pokemon_name.lower())
                response.raise_for_status()
                pokemon_data = response.json()

                name = pokemon_data['name']
                abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
                types = [type['type']['name'] for type in pokemon_data['types']]
                stats = [stat['base_stat'] for stat in pokemon_data['stats']]

                image_url = pokemon_data['sprites']['other']['official-artwork']['front_default']
                pixmap = QPixmap()
                pixmap.loadFromData(requests.get(image_url).content)

                info_text = f"Name: {name}\n"
                info_text += f"Abilities: {', '.join(abilities)}\n"
                info_text += f"Types: {', '.join(types)}\n"
                info_text += "Stats:\n"
                for stat, value in zip(["HP", "Attack", "Defense", "Special Attack", "Special Defense", "Speed"], stats):
                    info_text += f"{stat}: {value}\n"

                self.result_label.setText(info_text)
                self.pokemon_data[pokemon_name] = {'name': name, 'abilities': abilities, 'types': types, 'stats': stats, 'image': pixmap}

            except requests.exceptions.HTTPError as e:
                QMessageBox.critical(self, "Error", f"Error fetching data: {e}")
        else:
            QMessageBox.warning(self, "Invalid Input", "Please enter a Pokémon name.")

    def capture_pokemon(self):
        pokemon_name = self.textbox.text()
        if pokemon_name:
            if pokemon_name in self.pokemon_data:
                QMessageBox.information(self, "Already Captured", "This Pokémon is already captured.")
            else:
                QMessageBox.information(self, "Capture Success", f"You have captured {pokemon_name}!")
                self.search_pokemon()
        else:
            QMessageBox.warning(self, "Invalid Input", "Please enter a Pokémon name.")

    def open_display_window(self):
        if self.pokemon_data:
            display_window = DisplayWindow(self.pokemon_data)
            display_window.exec_()
        else:
            QMessageBox.warning(self, "No Captured Pokémon", "You haven't captured any Pokémon yet.")

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec_())