from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for item in old_nodes:
        if isinstance(item.text_type, TextType.TEXT):
            # SPLIT

        else:
            new_nodes.append(item)
