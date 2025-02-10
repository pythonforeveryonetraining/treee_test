import pathlib
import treee.tree

for x in treee.tree.get_flat_tree(pathlib.Path.cwd()):
    print(x)
