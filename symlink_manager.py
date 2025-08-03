import os
import sys
import platform
import argparse
from typing import List, Optional

def is_symlink(path: str) -> bool:
    """Проверяет, является ли путь символической ссылкой."""
    return os.path.islink(path) if hasattr(os, 'islink') else False

def find_symlinks(directory: str = ".", recursive: bool = True) -> List[str]:
    """Находит все символические ссылки в указанной папке (рекурсивно)."""
    symlinks = []
    for root, _, files in os.walk(directory if recursive else directory + os.sep):
        for name in files + _:
            path = os.path.join(root, name)
            if is_symlink(path):
                symlinks.append(path)
    return symlinks

def delete_symlink(link_path: str, is_silent: bool = False) -> bool:
    """Удаляет символическую ссылку."""
    try:
        if not is_symlink(link_path):
            if not is_silent:
                print(f"⚠️ '{link_path}' не является символической ссылкой!")
            return False

        os.unlink(link_path)
        if not is_silent:
            print(f"🗑️ Удалено: {link_path}")
        return True

    except OSError as e:
        if not is_silent:
            print(f"❌ Ошибка: {e}")
        return False

def create_symlink(source: str, link_name: str, is_silent: bool = False) -> bool:
    """Создает символическую ссылку (Windows/Linux)."""
    try:
        if os.path.exists(link_name):
            if not is_silent:
                print(f"⚠️ Ссылка '{link_name}' уже существует!")
            return False

        if platform.system() == "Windows":
            target_is_dir = os.path.isdir(source)
            os.symlink(source, link_name, target_is_directory=target_is_dir)
        else:
            os.symlink(source, link_name)

        if not is_silent:
            print(f"🔗 Создано: {link_name} → {source}")
        return True

    except OSError as e:
        if not is_silent:
            print(f"❌ Ошибка: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Менеджер символических ссылок (Windows/Linux)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Создание ссылки
    parser_create = subparsers.add_parser("create", help="Создать символическую ссылку")
    parser_create.add_argument("source", help="Исходный файл/папка")
    parser_create.add_argument("link_name", help="Имя ссылки")
    parser_create.add_argument("--silent", action="store_true", help="Тихий режим")

    # Поиск ссылок
    parser_list = subparsers.add_parser("list", help="Найти все символические ссылки")
    parser_list.add_argument("--directory", default=".", help="Папка для поиска (по умолчанию: текущая)")
    parser_list.add_argument("--no-recursive", action="store_false", dest="recursive", help="Не искать рекурсивно")

    # Удаление ссылок
    parser_delete = subparsers.add_parser("delete", help="Удалить символическую ссылку")
    parser_delete.add_argument("path", help="Путь к ссылке или папке для рекурсивного удаления")
    parser_delete.add_argument("--recursive", action="store_true", help="Удалить все ссылки в папке рекурсивно")
    parser_delete.add_argument("--silent", action="store_true", help="Тихий режим")

    args = parser.parse_args()

    if args.command == "create":
        success = create_symlink(args.source, args.link_name, args.silent)
        sys.exit(0 if success else 1)

    elif args.command == "list":
        symlinks = find_symlinks(args.directory, args.recursive)
        if symlinks:
            print("Найдены символические ссылки:")
            for link in symlinks:
                print(f"→ {link}")
        else:
            print("Ссылок не найдено.")

    elif args.command == "delete":
        if os.path.isdir(args.path) and args.recursive:
            symlinks = find_symlinks(args.path, recursive=True)
            if not symlinks:
                if not args.silent:
                    print("⚠️ В указанной папке ссылок не найдено.")
                sys.exit(1)

            for link in symlinks:
                delete_symlink(link, args.silent)
        else:
            success = delete_symlink(args.path, args.silent)
            sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()