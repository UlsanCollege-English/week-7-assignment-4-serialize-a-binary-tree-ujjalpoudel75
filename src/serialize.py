class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    """
    Serializes a binary tree to a string using pre-order traversal.
    '#' is used to represent a None node.
    Values are separated by spaces.
    """
    # List to hold the string representations of nodes
    res = []
    
    def preorder(node):
        # Base case: if node is None, append '#'
        if not node:
            res.append('#')
            return
        
        # Append the node's value (converted to string)
        res.append(str(node.val))
        # Recurse on left child
        preorder(node.left)
        # Recurse on right child
        preorder(node.right)
    
    # Start the traversal
    preorder(root)
    # Join all values with a space
    return ' '.join(res)

def deserialize(s):
    """
    Deserializes a string (created by serialize) back into a binary tree.
    """
    # Split the string into a list of tokens
    tokens = s.split(' ')
    # Use an iterator to easily consume tokens one by one
    it = iter(tokens)
    
    def build_tree():
        """
        Recursive helper function to build the tree from the token iterator.
        """
        try:
            # Get the next token
            val = next(it)
        except StopIteration:
            # Should not happen with a valid serialized string
            return None
        
        # Base case: if token is '#', this branch is None
        if val == '#':
            return None
        
        # Recursive step:
        # Create a new node with the value.
        # Note: All values are stored as strings, which is consistent
        # with the serialize(deserialize(s)) == s test logic.
        node = Node(val)
        # Build the left subtree
        node.left = build_tree()
        # Build the right subtree
        node.right = build_tree()
        
        # Return the constructed node
        return node
    
    # Start building the tree
    return build_tree()

