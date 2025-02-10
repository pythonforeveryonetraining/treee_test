from pathlib import Path

def get_flat_tree(folder, indent=""):
    if indent == "":
        yield f"{folder.name}/"

    # Load directory items and sort them, first by type (folders on top), then by name.
    sorted_items = [i for i in sorted(folder.iterdir(), key=lambda path: (not path.is_dir(), path.name))]

    # Turn items into a list of tuples where the first tuple element marks a regular node or an end node.
    connected_items = [("├── " if i < len(sorted_items) - 1 else "└── ", x) for i, x in enumerate(sorted_items)]

    for connector, path in connected_items:
        if path.is_dir():
            yield f"{indent}{connector}{path.name}/"
            if connector == "├── ":
                yield from get_flat_tree(path, indent + "│   ")  # Node must be followed down by a vertical line.
            else:
                yield from get_flat_tree(path, indent + "    ")  # End node must be followed by empty space.
        else:
            yield f"{indent}{connector}{path.name}"

def print_tree():
    for x in get_flat_tree(Path.cwd()):
        print(x)
