# main.py
import json
from funny_json_explorer import FunnyJsonExplorer
from tree_factory import TreeFactory
from rectangle_factory import RectangleFactory
from icon_family import ChessIconFamily, SmileIconFamily

if __name__ == "__main__":
    with open('src.json') as json_file:
        json_data = json.load(json_file)

    icon_families = [ChessIconFamily(), SmileIconFamily()]

    for icon_family in icon_families:
        print(f"Using icon family: {icon_family.__class__.__name__}")

        print("Tree Style:")
        explorer = FunnyJsonExplorer(TreeFactory(icon_family))
        explorer.show(json_data)
        print("\n")

        print(f"Using icon family: {icon_family.__class__.__name__}")

        print("Rectangle Style:")
        explorer = FunnyJsonExplorer(RectangleFactory(icon_family))
        explorer.show(json_data)
        print("\n")