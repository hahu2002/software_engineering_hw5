class FunnyJsonExplorer:
    def __init__(self, factory):
        self.factory = factory

    def show(self):
        container = self.factory.create_container('icon.png', 'Main Container', 0)
        leaf1 = self.factory.create_leaf('Leaf 1')
        leaf2 = self.factory.create_leaf('Leaf 2')
        leaf3 = self.factory.create_leaf('Leaf 3')
        leaf4 = self.factory.create_leaf('Leaf 4')

        container.add(leaf1)
        container.add(leaf2)
        container.add(leaf3)
        container.add(leaf4)

        container.draw()
