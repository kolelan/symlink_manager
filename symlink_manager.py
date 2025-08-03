import os
import sys
import platform
import argparse
from typing import List

def is_symlink(path: str) -> bool:
    """Определяет, является ли путь симлинком или junction point (Windows)"""
    if platform.system() == "Windows":
        try:
            # Проверяем атрибуты файла
            if not os.path.exists(path):
                return False
            if os.path.isdir(path):
                # Для папок проверяем, является ли она junction или symlink
                import ctypes
                FILE_ATTRIBUTE_REPARSE_POINT = 0x400
                attrs = ctypes.windll.kernel32.GetFileAttributesW(path)
                return attrs & FILE_ATTRIBUTE_REPARSE_POINT != 0
            else:
                return os.path.islink(path)
        except Exception:
            return False
    else:
        return os.path.islink(path)

def find_symlinks(directory: str = ".", recursive: bool = True) -> List[str]:
    """Находит все символические ссылки в указанной папке"""
    symlinks = []
    try:
        if recursive:
            for root, _, files in os.walk(directory):
                for name in files + _:
                    path = os.path.join(root, name)
                    if is_symlink(path):
                        symlinks.append(path)
        else:
            for item in os.listdir(directory):
                path = os.path.join(directory, item)
                if is_symlink(path):
                    symlinks.append(path)
    except Exception as e:
        print(f"Ошибка при сканировании: {e}", file=sys.stderr)
    return symlinks

def main():
    parser = argparse.ArgumentParser(description="Менеджер символических ссылок")
    parser.add_argument("command", choices=["list"], help="Команда")
    parser.add_argument("--directory", default=".", help="Директория для поиска")
    parser.add_argument("--no-recursive", action="store_true", help="Не искать рекурсивно")

    args = parser.parse_args()

    if args.command == "list":
        symlinks = find_symlinks(args.directory, not args.no_recursive)
        if symlinks:
            print("Найдены символические ссылки:")
            for link in symlinks:
                target = os.readlink(link) if hasattr(os, "readlink") else "???"
                print(f"{link} → {target}")
        else:
            print("Ссылок не найдено.")

if __name__ == "__main__":
    main()