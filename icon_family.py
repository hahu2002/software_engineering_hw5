# icon_family.py
class IconFamily:
    def get_icon(self, component_type):
        raise NotImplementedError

class ChessIconFamily(IconFamily):
    def get_icon(self, component_type):
        icons = {
            'container': '♔',
            'leaf': '♙'
        }
        return icons.get(component_type, '')

class SmileIconFamily(IconFamily):
    def get_icon(self, component_type):
        icons = {
            'container': '😉',
            'leaf': '😎'
        }
        return icons.get(component_type, '')
