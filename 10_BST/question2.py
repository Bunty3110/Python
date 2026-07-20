def __invert_tree(self, node):
    if node is None:
        return None

    temp = node.left
    node.left = self.__invert_tree(node.right)
    node.right = self.__invert_tree(temp)
    
    return node