import argparse
import os
from duplicate_finder import DuplicateFinder

class Main:
    def __init__(self, directory_path:str, method:str):
        self._duplicate_finder = DuplicateFinder(directory_path)
        self._method = method
        self._directory_path = directory_path

    def run(self):
        """Main function to run the Duplicate Finder."""

        if self._method == "hash":
            duplicates = self._duplicate_finder.find_duplicates_by_hash()
            print(f"\n--- Duplicate Files (by Hash) in {self._directory_path} ---")
        else:
            duplicates = self._duplicate_finder.find_duplicates_by_name()
            print(f"\n--- Duplicate Files (by Name) in {self._directory_path} ---")

        if duplicates:
            for key, paths in duplicates.items():
                print(f"\nDuplicates for {key}:")
                for path in paths:
                    print(f"  - {path}")
        else:
            print("No duplicate files found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find duplicate files in a directory.")
    parser.add_argument("directory", type=str, help="The path to the directory to scan.")
    parser.add_argument("--method", type=str, default="hash",
                        choices=["hash", "name"],
                        help="The method to use for duplicate detection: 'hash' (default) or 'name'.")

    args = parser.parse_args()

    directory_path = args.directory
    method = args.method

    if not os.path.isdir(directory_path):
        msg = f"Error: Directory not found: {directory_path}"
        print(msg)
        raise FileNotFoundError(msg)
    
    main = Main(directory_path, method)
    main.run()

