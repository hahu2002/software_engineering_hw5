from funny_json_explorer import FunnyJsonExplorer
from tree_factory import TreeFactory
from rectangle_factory import RectangleFactory
from icon_family import PokerFaceIconFamily, SmileIconFamily

if __name__ == "__main__":
    icon_families = [PokerFaceIconFamily(), SmileIconFamily()]

    for icon_family in icon_families:
        print(f"Using icon family: {icon_family.__class__.__name__}")

        print("\nTree Style:")
        explorer = FunnyJsonExplorer(TreeFactory(icon_family))
        explorer.show()

        print("\nRectangle Style:")
        explorer = FunnyJsonExplorer(RectangleFactory(icon_family))
        explorer.show()
