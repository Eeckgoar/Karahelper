import logging
logging.basicConfig(level=logging.INFO)


import time
import os
from pywinauto import Desktop, mouse
from subprocess import Popen




# Путь к исполняемому файлу Karafun Player
karafun_path = r"C:\Program Files (x86)\KaraFun Player 2\KarafunPlayer.exe"

# Путь для сохранения списка песен
save_path = r"Playlist.txt"

# Запуск Karafun Player (если он еще не запущен)
Popen(karafun_path)
player = Desktop(backend='uia').window(title_re="KaraFun Player")


# Подключение к главному окну Karafun Player
#main_window = app.window(title_re="KaraFun Player")

def save_playlist():
    # Проверяем, активно ли окно Karafun Player
    if player.is_active():
        # Дерево очередей
        player_tree = player.child_window(class_name = "TVirtualStringTree",  ctrl_index = 1)
        rect = player_tree.rectangle()
        mouse.right_click(coords=(rect.left +80, rect.top + 10))
        player.type_keys("{DOWN}{ENTER}")

        save_dialog = player.window(title="Save history to...")
        
        # Вводим путь для сохранения

        save_dialog.Edit.set_text(save_path)

        
        # Нажимаем кнопку "Save"
        save_dialog.Сохранить.click()
        print("Playlist saved successfully.")
    else:
        print("Karafun Player is not the active window. Skipping save.")

# Основной цикл
while True:
    save_playlist()
    time.sleep(60)  # Ожидание 10 минут (600 секунд)п