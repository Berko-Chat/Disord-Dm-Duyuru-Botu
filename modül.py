import os

def change_cmd_color(color_code):
    os.system(f'cmd /c "color {color_code}"')

def install_modules():
    os.system('cmd /c "pip install discord.py"')

if __name__ == "__main__":
    change_cmd_color('0A')  # '0A' yeşil metin siyah arka plan için
    install_modules()
    input("Yükleme tamamlandı. Pencereyi kapatmak için Enter tuşuna basın...")
