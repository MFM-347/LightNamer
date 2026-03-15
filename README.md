# **LightNamer: CLI & Library for Auto Renaming** 🚀

![PyPI - Downloads](https://img.shields.io/pypi/dm/lightnamer)
![PyPI - Version](https://img.shields.io/pypi/v/lightnamer)
[![License MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/MFM-347/LightNamer/LICENSE)

LightNamer is a **Python library and CLI tool** designed to **automate file renaming** in a given directory. It sequentially renames files using a specified **base name**, appending a numeric index while preserving the original file extension.

## **📌 Features**

| Feature             | Availability | Description                                                                   |
| ------------------- | ------------ | ----------------------------------------------------------------------------- |
| **Batch Rename**    | ✔            | Rename multiple files at once with a custom prefix.                           |
| **Sorting Options** | ✔            | Rename files in alphabetical, newest, or oldest order.                        |
| **Simulation Mode** | ✔            | Preview renaming changes without modifying files. No actual changes are made. |
| **Library Support** | ✔            | Use LightNamer as a module in your Python scripts for automation.             |
| **Cross-Platform**  | ✔            | Works seamlessly on Windows, macOS, and Linux.                                |

## **🛠️ Prerequisites**

- **Python 3.x** installed
- Basic knowledge of **command-line usage**

### **📦 Required Python Packages**

LightNamer requires the following package(s):

- `pyfiglet` (for CLI banner text)

To install dependencies, run:

```sh
pip install -r requirements.txt  # Use pip3 on macOS
```

## **⚡ Installation**

### **🔹 Install via Pip**

To install LightNamer as a library:

```sh
pip install lightnamer
```

### **🔹 Install from Source**

To install and run the tool from the source code:

```sh
git clone https://github.com/MFM-347/LightNamer.git
cd LightNamer
pip install .
```

## **💻 CLI Usage**

### **📌 Run the CLI**

```sh
lightnamer <base_name> <directory> [-r <order>] [-s]
```

### **Example**

Rename files inside `C:\Users\YourName\Documents\Folder`, using "File" as the base name:

```sh
lightnamer "File" C:\Users\YourName\Documents\Folder
```

### **📂 Given Directory (`C:\Docs`)**

```
report.docx
notes.txt
summary.pdf
```

### **🏷️ Renaming Command**

```sh
lightnamer "Document" C:\Docs -r alphabet
```

### **📝 Output**

```
Document-1.docx
Document-2.pdf
Document-3.txt
```

## **⚙️ Command-Line Options**

| Option                | Description                                  |
| --------------------- | -------------------------------------------- |
| `<base_name>`         | Prefix for renamed files.                    |
| `<directory>`         | Path to folder containing the files.         |
| `-r, --order <order>` | Sorting order before renaming:               |
|                       | - `alphabet` → A-Z order                     |
|                       | - `new` → Newest to oldest                   |
|                       | - `old` → Oldest to newest (default)         |
| `-s, --simulate`      | Run a **simulation** without renaming files. |
| `--case-sensitive`    | Sorts filenames in case-sensitive mode.      |
| `--debug`             | Enables debug logging.                       |

## **📦 Using LightNamer as a Library**

### **🔹 Installed Library Usage**

If you have installed LightNamer via `pip`, you can use it in your Python scripts as follows:

```python
from lightnamer import renFn
from pathlib import Path

directory = Path("C:/Users/YourName/Documents/Folder")
renFn(base_name="Document", directory=directory, order="alphabet", simulate=False, case_sensitive=False)
```

### **🔹 Source Code Usage**

If running directly from the cloned source repository:

```python
from lightnamer import renFn
from pathlib import Path

directory = Path("C:/Users/YourName/Documents/Folder")
renFn(base_name="Document", directory=directory, order="alphabet", simulate=False, case_sensitive=False)
```

### **Sorting Files Only**

If you only need to **get sorted files** without renaming:

```python
from lightnamer import sortFn
from pathlib import Path

directory = Path("/path/to/files")
sorted_files = sortFn(directory, order="new", case_sensitive=True)
print(sorted_files)
```

### **Handling Errors Gracefully**

You can wrap it in a try-except block:

```python
try:
    renFn("Example", Path("/home/user/files"), "old", False, False)
except Exception as e:
    print(f"An error occurred: {e}")
```

## **🧪 Running Tests (For Source Code Only)**

Run all tests:

```sh
python -m unittest discover tests
```

## Future Plans

- Add option to rename only specific file type.
- Add Graphic User Interface (GUI).

## **🤝 Contributing**

We welcome contributions! Please check the [CONTRIBUTING.md](https://github.com/MFM-347/LightNamer/blob/main/CONTRIBUTING.md) for guidelines.

## **👨‍💻 Credits**

Created and maintained by [MFM-347](https://github.com/MFM-347).

## **📜 License**

This project is licensed under the **MIT License**.
