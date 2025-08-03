# **Менеджер символических ссылок (Symlink Manager)**

Кросс-платформенный инструмент для работы с символическими ссылками в **Windows, Linux и macOS**. Поддерживает все типы ссылок, включая WSL-ссылки и junction points в Windows.

## 🔥 **Возможности**

- **Создание** символических ссылок (файлы/папки)
- **Поиск** всех ссылок в директории (рекурсивно)
- **Удаление** (одной ссылки или всех в папке)
- Поддержка **WSL-ссылок** и **junction points**
- Проверка прав администратора (Windows)
- **Тихий режим** для автоматизации

## 📦 **Установка**

1. Требуется **Python 3.7+**
2. Скачайте скрипт:
   ```bash
   curl -O http://raw.githubusercontent.com/kolelan/symlink_manager/refs/heads/main/symlink_manager.py
   ```
3. (Опционально) Сделайте исполняемым:
   ```bash
   chmod +x symlink_manager.py
   ```

## 🛠 **Использование**

### **1. Создание ссылки**
```bash
python symlink_manager.py create <исходный_путь> <имя_ссылки> [--silent]
```
**Пример:**
```bash
# Windows
python symlink_manager.py create "C:\Data" "C:\Links\DataLink"

# WSL
python3 symlink_manager.py create ~/Documents/project ~/project_link

# Linux/macOS
python symlink_manager.py create /path/to/file my_link
```

### **2. Поиск ссылок**
```bash
python symlink_manager.py list [--directory <папка>] [--no-recursive]
```
**Пример:**
```bash
python symlink_manager.py list --directory ~/projects
```

### **3. Удаление ссылок**
```bash
# Удалить одну ссылку
python symlink_manager.py delete <путь> [--recursive] [--silent]

# Рекурсивное удаление всех ссылок в папке
python symlink_manager.py delete <папка> [--recursive] [--silent]
```
**Пример:**
```bash
# Удалить одну ссылку
python symlink_manager.py delete ~/broken_link

# Удалить все ссылки в проекте
python symlink_manager.py delete ~/OldProject --recursive
```

## 🔧 Особенности

✅ **Кросс-платформенность**  
Работает в Windows (требует админ-прав), Linux, macOS и WSL

✅ **Поддержка WSL**  
Корректно определяет и удаляет ссылки, созданные в WSL

✅ **Гибкие параметры**  
- Рекурсивный поиск/удаление  
- Тихий режим (--silent)  
- Работа с относительными/абсолютными путями

## ⚠️ Ограничения

- В Windows требуется запуск от имени администратора
- Некоторые WSL-ссылки могут не определяться в особых случаях

## 📜 Лицензия

MIT License. Используйте свободно.