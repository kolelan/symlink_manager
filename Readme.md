# Symbolic Link Manager (symlink_manager.py)

A cross-platform utility for creating, finding, and deleting symbolic links with Windows, Linux, macOS, and WSL support.

## 📝 Requirements

- Python 3.6+
- Administrator privileges (Windows only)

## ⚙️ Installation

No installation needed. Just download the script:

```bash
wget https://raw.githubusercontent.com/kolelan/symlink_manager/refs/heads/main/symlink_manager.py
```

## 🛠 Usage

### Create a symbolic link
```bash
python symlink_manager.py create <source> <link_name> [--silent]
```
Example:
```bash
python symlink_manager.py create /path/to/file my_link
```

### Find symbolic links
```bash
python symlink_manager.py list [--directory <path>] [--no-recursive]
```
Example:
```bash
python symlink_manager.py list --directory ~/projects
```

### Delete symbolic links
```bash
python symlink_manager.py delete <path> [--recursive] [--silent]
```
Examples:
```bash
# Delete single link
python symlink_manager.py delete ~/my_link

# Recursively delete all links in directory
python symlink_manager.py delete ~/project_folder --recursive
```

## 🔧 Features

✅ **Cross-platform**  
Works on Windows (admin required), Linux, macOS and WSL

✅ **WSL Support**  
Correctly identifies and removes links created in WSL

✅ **Flexible Options**  
- Recursive operations  
- Silent mode (--silent)  
- Relative/absolute path support

## ⚠️ Limitations

- Requires admin privileges on Windows
- Some edge-case WSL links might not be detected

## 📜 License

MIT License. Free to use and modify.
