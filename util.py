class NonBinTreeNode():
    def __init__(self, action_value, parent):
        self.action_value = action_value
        self.parent = parent
        self.children = []
    
    def add_child(self, child_value):
        child = NonBinTreeNode(child_value, parent=self)
        self.children.append(child)
        return child
    
    def __str__(self):
        return f'{self.parent}, {self.action_value}, {self.children} END'