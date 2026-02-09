from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link


def text_to_textnodes(text):
    node = [TextNode(text, TextType.TEXT)]
    delims = ['**', '_', '`']
    node = split_nodes_delimiter(node, delims[0], TextType.BOLD)
    node = split_nodes_delimiter(node, delims[1], TextType.ITALIC)
    node = split_nodes_delimiter(node, delims[2], TextType.CODE)
    node = split_nodes_link(node)
    node = split_nodes_image(node)
    return node
