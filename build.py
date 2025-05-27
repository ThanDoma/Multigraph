import os
import subprocess
import sys
import platform

def main():
    print("Начало сборки приложения в один исполняемый файл...")
    
    # Проверяем наличие PyInstaller
    try:
        import PyInstaller
        print("PyInstaller уже установлен")
    except ImportError:
        print("Установка PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # Проверяем наличие необходимых зависимостей
    print("Проверка и установка зависимостей...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    # Определяем имя исполняемого файла в зависимости от ОС
    exe_name = "BalanceCalculator"
    if platform.system() == "Windows":
        exe_name += ".exe"
    
    # Создаем папку для сборки, если её нет
    if not os.path.exists("dist"):
        os.makedirs("dist")
    
    # Параметры для PyInstaller
    pyinstaller_args = [
        "pyinstaller",
        "--onefile",  # Создать один исполняемый файл
        "--windowed",  # Не показывать консоль при запуске
        "--name", exe_name,  # Имя исполняемого файла
        "--icon=windows/icon.ico" if os.path.exists("windows/icon.ico") else "",  # Иконка, если есть
    ]
    
    # Добавляем параметр --add-data с правильным разделителем в зависимости от ОС
    if platform.system() == "Windows":
        pyinstaller_args.extend(["--add-data", "windows;windows"])
    else:
        pyinstaller_args.extend(["--add-data", "windows:windows"])
    
    # Добавляем главный файл приложения
    pyinstaller_args.append("main.py")
    
    # Удаляем пустые аргументы
    pyinstaller_args = [arg for arg in pyinstaller_args if arg]
    
    print("Запуск PyInstaller со следующими аргументами:")
    print(" ".join(pyinstaller_args))
    
    # Запускаем PyInstaller
    subprocess.check_call(pyinstaller_args)
    
    print("\nСборка завершена!")
    print(f"Исполняемый файл находится в: dist/{exe_name}")

if __name__ == "__main__":
    main() 