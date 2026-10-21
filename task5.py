def make_node(value):
    return {"value": value, "left": None, "right": None}
def build():
    root = make_node(50)
    root["left"] = make_node(30)
    root["right"] = make_node(70)
    root["left"]["left"] = make_node(20)
    root["left"]["right"] = make_node(40)
    root["right"]["left"] = make_node(60)
    root["right"]["right"] = make_node(80)
    return root

def print_tree(root):
    print(f"     {root['value']}")
    print(f"    / \\")
    print(f"   {root['left']['value']}    {root['right']['value']}")
    print("  / \\    /\\")
    print(f" {root['left']['left']['value']}  {root['left']['right']['value']}  {root['right']['left']['value']}  {root['right']['right']['value']}")
tree=build()

print_tree(tree)

def leftmost_value(tree):
    while tree["left"] is not None:
        tree=tree["left"]
    return tree["value"]

def rightmost_value(tree):
    while tree["right"] is not None:
        tree=tree["right"]
    return tree["value"]

tree = build()
print("leftmost value is:",leftmost_value(tree))
print("rightmost value is:",rightmost_value(tree))