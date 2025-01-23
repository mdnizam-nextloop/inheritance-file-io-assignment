
---

#### 2. **`file_management_system.py` (Starter Code)**


```python
class Node:
    def __init__(self, name, type, parent=None, permissions=None):
        """
        Initialize a Node object with name, type (folder or file),
        an optional parent, and optional permissions.
        """
        pass  # Implement this

    def set_permissions(self, permissions):
        """
        Set or update permissions for this node.
        """
        pass  # Implement this

    def assign_role(self, user, role):
        """
        Assign a role to a user (Viewer or Editor).
        """
        pass  # Implement this

    def move(self, new_parent):
        """
        Move this node to a new parent.
        """
        pass  # Implement this

    def delete(self):
        """
        Delete this node and all its children.
        """
        pass  # Implement this

    def check_permissions(self, user, action):
        """
        Check if a user has permission to perform the action.
        """
        pass  # Implement this
