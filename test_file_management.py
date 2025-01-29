import pytest
from file_management_system import (
    create_node,
    set_permissions,
    assign_role,
    move_node,
    delete_node,
    check_permissions,
)


@pytest.fixture
def setup_file_structure():
    """Setup a basic folder structure for testing."""
    root = create_node("Root", "folder", None, permissions={"Alice": {"read": True}})
    folder_a = create_node("FolderA", "folder", root)
    file_1 = create_node("File1", "file", folder_a)
    return root, folder_a, file_1

def test_create_folder_file(setup_file_structure):
    root, folder_a, file_1 = setup_file_structure
    
    assert folder_a.parent == root
    assert file_1.parent == folder_a
    assert file_1 in folder_a.children

def test_inherited_permissions(setup_file_structure):
    """Test whether permissions inherit correctly."""
    root, folder_a, file_1 = setup_file_structure
    
    # FolderA and File1 should inherit "read": True from Root
    assert check_permissions("Alice", folder_a, "read") is True
    assert check_permissions("Alice", file_1, "read") is True

def test_override_permissions(setup_file_structure):
    """Test whether overriding permissions works correctly."""
    root, folder_a, file_1 = setup_file_structure
    
    # Override File1's permissions to deny read
    set_permissions(file_1, {"Alice": {"read": False}})
    
    assert check_permissions("Alice", file_1, "read") is False
    assert check_permissions("Alice", folder_a, "read") is True

def test_move_node():
    """Test moving a file and inheriting new parent permissions."""
    root = create_node("Root", "folder", None)
    folder_a = create_node("FolderA", "folder", root)
    folder_b = create_node("FolderB", "folder", root, permissions={"Alice": {"read": False}})
    file_1 = create_node("File1", "file", folder_a)
    
    # Move File1 from FolderA to FolderB
    move_node(file_1, folder_b)
    
    assert file_1.parent == folder_b
    assert check_permissions("Alice", file_1, "read") is False  # Should inherit FolderB’s permissions

def test_delete_node():
    """Test deleting a folder removes all children."""
    root, folder_a, file_1 = create_node("Root", "folder", None), create_node("FolderA", "folder", None), create_node("File1", "file", None)
    folder_a.children.append(file_1)
    
    delete_node(folder_a)
    
    # FolderA and File1 should be gone
    assert folder_a.children == []
    
def test_conflicting_permissions():
    """Test if child permissions override parent restrictions."""
    root = create_node("Root", "folder", None)
    folder_a = create_node("FolderA", "folder", root, permissions={"Alice": {"share": False}})
    file_1 = create_node("File1", "file", folder_a)

    # Override share permission at file level
    set_permissions(file_1, {"Alice": {"share": True}})
    
    assert check_permissions("Alice", file_1, "share") is True
    assert check_permissions("Alice", folder_a, "share") is False

# ✅ Fix the test function to use the fixture as a parameter
def test_role_based_permissions(setup_file_structure):
    root, folder_a, file_1 = setup_file_structure

    assign_role(file_1, user="Alice", role="Viewer")  # Assign Alice as Viewer
    assert check_permissions("Alice", file_1, "write") == False  # Viewers cannot write

def test_invalid_move(setup_file_structure):
    root, folder_a, file_1 = setup_file_structure

    folder_c = None  # This folder does not exist

    with pytest.raises(Exception):  # Expect an error when moving to a non-existent folder
        move_node(file_1, folder_c)

if __name__ == "__main__":
    pytest.main()
