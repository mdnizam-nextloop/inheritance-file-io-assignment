class Node:
    def __init__(self, name, node_type, parent=None, permissions=None):
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

    def check_permissions(self, user, action):
        """Check if the user has the required permission to perform an action."""
         pass  # Implement this

    def move(self, new_parent):
        """Move the node to a new parent and inherit new permissions if not explicitly set."""
        
         pass  # Implement this

    def delete(self):
        """Recursively delete a folder or file."""

         pass  # Implement this


# Required Functions (to be used in test cases)

def create_node(name, node_type, parent=None, permissions=None):
    """Create a file or folder node."""


def set_permissions(node, permissions):
    """Set or override permissions on a node."""


def assign_role(node, user, role):
    """Assign a user role on a node. 'Editor' means full access, 'Viewer' means read-only."""
    


def move_node(node, new_parent):
    """Move a file/folder node to a new parent folder."""
    


def delete_node(node):
    """Delete a node and all its contents."""
    


def check_permissions(user, node, action):
    """Check if a user has permissions for a given action on a node."""
    
