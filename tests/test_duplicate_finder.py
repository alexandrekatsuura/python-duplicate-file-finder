import pytest
import os
import hashlib
from src.duplicate_finder import DuplicateFinder

# Fixture to create a temporary directory with test files
@pytest.fixture
def temp_test_dir(tmp_path):
    # Create some dummy files
    (tmp_path / "file1.txt").write_text("content A")
    (tmp_path / "file2.txt").write_text("content B")
    (tmp_path / "file3.txt").write_text("content A") # Duplicate of file1.txt by content
    (tmp_path / "file4.txt").write_text("content C")
    (tmp_path / "file1_copy.txt").write_text("content A") # Duplicate of file1.txt by content and similar name
    (tmp_path / "subdir").mkdir()
    (tmp_path / "subdir" / "file1.txt").write_text("content D") # Duplicate of file1.txt by name, different content
    (tmp_path / "subdir" / "file5.txt").write_text("content B") # Duplicate of file2.txt by content
    return tmp_path

def test_duplicate_finder_init_valid_directory(temp_test_dir):
    finder = DuplicateFinder(str(temp_test_dir))
    assert finder.directory == str(temp_test_dir)

def test_duplicate_finder_init_invalid_directory():
    with pytest.raises(ValueError, match="Directory not found"):
        DuplicateFinder("/non/existent/path")

def test_hash_file(temp_test_dir):
    finder = DuplicateFinder(str(temp_test_dir))
    filepath = temp_test_dir / "file1.txt"
    expected_hash = hashlib.md5(b"content A").hexdigest()
    assert finder._hash_file(str(filepath)) == expected_hash

def test_find_duplicates_by_hash(temp_test_dir):
    finder = DuplicateFinder(str(temp_test_dir))
    duplicates = finder.find_duplicates_by_hash()

    # Expected duplicates by hash
    hash_A = hashlib.md5(b"content A").hexdigest()
    hash_B = hashlib.md5(b"content B").hexdigest()

    assert hash_A in duplicates
    assert len(duplicates[hash_A]) == 3
    assert str(temp_test_dir / "file1.txt") in duplicates[hash_A]
    assert str(temp_test_dir / "file3.txt") in duplicates[hash_A]
    assert str(temp_test_dir / "file1_copy.txt") in duplicates[hash_A]

    assert hash_B in duplicates
    assert len(duplicates[hash_B]) == 2
    assert str(temp_test_dir / "file2.txt") in duplicates[hash_B]
    assert str(temp_test_dir / "subdir" / "file5.txt") in duplicates[hash_B]

    # Ensure no non-duplicate hashes are present
    assert hashlib.md5(b"content C").hexdigest() not in duplicates
    assert hashlib.md5(b"content D").hexdigest() not in duplicates

def test_find_duplicates_by_name(temp_test_dir):
    finder = DuplicateFinder(str(temp_test_dir))
    duplicates = finder.find_duplicates_by_name()

    # Expected duplicates by name
    assert "file1.txt" in duplicates
    assert len(duplicates["file1.txt"]) == 2
    assert str(temp_test_dir / "file1.txt") in duplicates["file1.txt"]
    assert str(temp_test_dir / "subdir" / "file1.txt") in duplicates["file1.txt"]

    # Ensure no non-duplicate names are present
    assert "file2.txt" not in duplicates # file2.txt and file5.txt have different names
    assert "file3.txt" not in duplicates
    assert "file4.txt" not in duplicates
    assert "file1_copy.txt" not in duplicates
    assert "file5.txt" not in duplicates


