import pytest
from file_management_system import Node

def test_basic_file_operations():
    root = Node("Root", "folder")
    folder_a = Node("FolderA", "folder", root)
    file1 = Node("File1", "file", folder_a)
    folder_a.set_permissions({"read": True})
    file1.set_permissions({"read": False})
    assert file1.check_permissions("Alice", "read") == False

def test_move_node():
    root = Node("Root", "folder")
    folder_a = Node("FolderA", "folder", root)
    folder_b = Node("FolderB", "folder", root, {"read": False})
    file1 = Node("File1", "file", folder_a)
    file1.move(folder_b)
    assert file1.check_permissions("Alice", "read") == False

def test_delete_node():
    root = Node("Root", "folder")
    folder_a = Node("FolderA", "folder", root)
    file1 = Node("File1", "file", folder_a)
    folder_a.delete()
    with pytest.raises(Exception):
        file1.check_permissions("Alice", "read")

def test_conflicting_permissions():
    root = Node("Root", "folder")
    folder_a = Node("FolderA", "folder", root)
    file1 = Node("File1", "file", folder_a)
    folder_a.set_permissions({"share": False})
    file1.set_permissions({"share": True})
    assert file1.check_permissions("Alice", "share") == True

def test_role_based_permissions():
    root = Node("Root", "folder")
    file1 = Node("File1", "file", root)
    file1.assign_role("Alice", "Viewer")
    assert file1.check_permissions("Alice", "write") == False
