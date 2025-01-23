# Inheritance for File I/O with Collaboration

## Overview
This assignment is designed to help you practice object-oriented programming concepts, inheritance, and file/folder operations in a collaborative environment. 

## Problem Statement
Your task is to design a file management system similar to Google Drive. Implement a system that handles:
- File and folder creation.
- File and folder deletion.
- Moving files or folders.
- Setting permissions at the parent and child levels (read-only or editor access).
- Checking permissions for users (viewer or editor roles).

### Requirements
#### Implement the following functions in `file_management_system.py`:
1. `create_node(name, type, parent=None, permissions=None)`:
   - Create a file or folder.
2. `set_permissions(node, permissions)`:
   - Set permissions for a file or folder. These should inherit by default but allow for child-level overrides.
3. `assign_role(node, user, role)`:
   - Assign roles (`Viewer` or `Editor`) to users.
4. `move_node(node, new_parent)`:
   - Move a file or folder to a new parent and handle permission inheritance.
5. `delete_node(node)`:
   - Delete a folder and all its contents.
6. `check_permissions(user, node, action)`:
   - Check if a user has permission to perform an action (e.g., `read` or `write`).

#### Test Cases to Pass
1. **Basic File Operations**
    - Create a root folder and a file.
    - Assign permissions and verify inheritance.
    - Override permissions at the child level.
2. **Moving a File**
    - Create two folders.
    - Assign permissions to the first folder and deny them in the second.
    - Move the file from the first folder to the second and check if the new permissions are inherited.
3. **Deleting a Folder**
    - Create a folder structure.
    - Delete a folder and verify that its children are also deleted.
4. **Conflict Resolution**
    - Assign conflicting permissions to a file and its parent.
    - Ensure child permissions override parent restrictions.
5. **Role-based Access**
    - Assign the Viewer role to a user and ensure they can only read, not write.

## Setup
1. Clone the repository:
   ```bash
   git clone <repo-link>
