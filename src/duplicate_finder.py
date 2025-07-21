import os
import hashlib
from collections import defaultdict

class DuplicateFinder:
    """
    A class to find duplicate files in a given directory.
    Duplicates can be identified by file hash (MD5) or by file name.
    """

    def __init__(self, directory):
        """
        Initializes the DuplicateFinder with the target directory.

        Args:
            directory (str): The path to the directory to scan.
        """
        if not os.path.isdir(directory):
            raise ValueError(f"Directory not found: {directory}")
        self.directory = directory

    def _hash_file(self, filepath, block_size=65536):
        """
        Generates the MD5 hash of a given file.

        Args:
            filepath (str): The path to the file.
            block_size (int): The size of chunks to read from the file.

        Returns:
            str: The MD5 hash of the file content.
        """
        hasher = hashlib.md5()
        with open(filepath, 'rb') as f:
            buf = f.read(block_size)
            while len(buf) > 0:
                hasher.update(buf)
                buf = f.read(block_size)
        return hasher.hexdigest()

    def find_duplicates_by_hash(self):
        """
        Finds duplicate files based on their MD5 hash.

        Returns:
            dict: A dictionary where keys are MD5 hashes and values are lists of file paths
                  that have that hash.
        """
        hashes = defaultdict(list)
        for dirpath, _, filenames in os.walk(self.directory):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                if os.path.isfile(filepath):
                    file_hash = self._hash_file(filepath)
                    hashes[file_hash].append(filepath)
        return {h: paths for h, paths in hashes.items() if len(paths) > 1}

    def find_duplicates_by_name(self):
        """
        Finds duplicate files based on their file name.

        Returns:
            dict: A dictionary where keys are file names and values are lists of file paths
                  that have that name.
        """
        filenames = defaultdict(list)
        for dirpath, _, files in os.walk(self.directory):
            for filename in files:
                filepath = os.path.join(dirpath, filename)
                filenames[filename].append(filepath)
        return {name: paths for name, paths in filenames.items() if len(paths) > 1}


