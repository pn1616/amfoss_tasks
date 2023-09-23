from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QWidget, QTextEdit, QScrollArea
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class DisplayWindow(QDialog):
    def __init__(self, pokemon_data):
        super().__init__()
        self.pokemon_data = pokemon_data
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Display Pokémon")
        self.setGeometry(100, 100, 800, 600)
        
        main_layout = QVBoxLayout()
        
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.image_label)
        
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        main_layout.addWidget(self.text_edit)
        
        button_layout = QHBoxLayout()
        prev_button = QPushButton("Previous", self)
        next_button = QPushButton("Next", self)
        close_button = QPushButton("Close", self)
        button_layout.addWidget(prev_button)
        button_layout.addWidget(next_button)
        button_layout.addWidget(close_button)
        main_layout.addLayout(button_layout)
        
        self.setLayout(main_layout)

        self.current_pokemon_index = 0
        self.display_pokemon()
        
        prev_button.clicked.connect(self.show_previous_pokemon)
        next_button.clicked.connect(self.show_next_pokemon)
        close_button.clicked.connect(self.accept)
        
    def display_pokemon(self):
        if self.pokemon_data:
            pokemon_names = list(self.pokemon_data.keys())
            pokemon_name = pokemon_names[self.current_pokemon_index]
            pokemon_info = self.pokemon_data[pokemon_name]
            
            pixmap = pokemon_info['image']
            self.image_label.setPixmap(pixmap)
            
            info_text = f"Name: {pokemon_info['name']}\n"
            info_text += f"Abilities: {', '.join(pokemon_info['abilities'])}\n"
            info_text += f"Types: {', '.join(pokemon_info['types'])}\n"
            info_text += "Stats:\n"
            for stat, value in zip(["HP", "Attack", "Defense", "Special Attack", "Special Defense", "Speed"], pokemon_info['stats']):
                info_text += f"{stat}: {value}\n"
            
            self.text_edit.setPlainText(info_text)
            
    def show_previous_pokemon(self):
        if self.pokemon_data:
            self.current_pokemon_index = (self.current_pokemon_index - 1) % len(self.pokemon_data)
            self.display_pokemon()
            
    def show_next_pokemon(self):
        if self.pokemon_data:
            self.current_pokemon_index = (self.current_pokemon_index + 1) % len(self.pokemon_data)
            self.display_pokemon()
