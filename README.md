# 📝 Python Duplicate File Finder

![GitHub repo size](https://img.shields.io/github/repo-size/alexandrekatsuura/python-duplicate-file-finder?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/alexandrekatsuura/python-duplicate-file-finder?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/alexandrekatsuura/python-duplicate-file-finder?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/alexandrekatsuura/python-duplicate-file-finder?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/alexandrekatsuura/python-duplicate-file-finder?style=for-the-badge)

## 📚 Academic Use Disclaimer

> ⚠️ This is an academic project created for learning purposes only.
> It is not intended for production use.

## ℹ️ About

This project is a command-line application built in Python that identifies duplicate files within a specified directory. It supports two methods for detection: by file hash (MD5) for accurate content comparison, and by file name for quick identification of similarly named files.
It's designed to demonstrate clean code structure, encapsulation, and testing with `pytest`.

## 🚀 Features

*   **Duplicate Detection by Hash**: Identifies files with identical content using MD5 hashing.
*   **Duplicate Detection by Name**: Finds files with the same name in different locations.
*   **Command-Line Interface (CLI)**: Simple interface for user interaction.
*   **Error Handling**: Handles invalid input paths and file access issues gracefully.
*   **Unit Testing**: Tests included using `pytest`.
*   **Clean Project Structure**: Modular organization for clarity and scalability.

## 🛠️ Technologies Used

*   **Python 3.x**
*   **`pytest`**: Framework used to create and run unit tests.

## ⚙️ How to Run the Project

### Prerequisites

Ensure that Python 3.x is installed on your machine.

### Installation

1.  Clone this repository:

    ```bash
    git clone https://github.com/alexandrekatsuura/python-duplicate-file-finder
    cd python-duplicate-file-finder
    ```

2.  (Optional but recommended) Create and activate a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate      # On Linux/macOS
    # .venv\\Scripts\\activate       # On Windows
    ```

3.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

To run the program, use the following command:

```bash
python src/main.py <directory_path> [--method <hash|name>]
```

*   `<directory_path>`: The path to the directory to scan for duplicate files.
*   `--method <hash|name>`: (Optional) The method to use for duplicate detection. Defaults to `hash`.

Example:

```bash
python src/main.py /path/to/your/folder --method hash
```

## ✅ Running the Tests

To run the unit tests, from the project root directory:

```bash
pytest -v
```

This will execute all test cases located in the `tests/` directory.

## 📁 Project Structure

```bash
python-duplicate-file-finder/
├── src/
│   └── main.py             # Main logic for execution and CLI
│   └── duplicate_finder.py # Logic for finding duplicate files
├── tests/
│   └── test_duplicate_finder.py # Unit tests for the DuplicateFinder class
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
└── requirements.txt        # Project dependencies
```

## 📄 License

This project is licensed under the [MIT License](LICENSE).

