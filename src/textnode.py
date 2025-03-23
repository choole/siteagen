from enum import Enum
from leafnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (self.text == other.text and self.text_type == other.text_type and self.url == other.url):
            return True
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    if not isinstance(text_node.text_type, TextType):
        raise Exception("Text type is of wrong type")
    match text_node.text_type:
        case TextType.TEXT:
            node = LeafNode(None, text_node.text)
        case TextType.BOLD:
            node = LeafNode("b", text_node.text)
        case TextType.ITALIC:
            node = LeafNode("i", text_node.text)
        case TextType.CODE:
            node = LeafNode("code", text_node.text)
        case TextType.LINK:
            node = LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            node = LeafNode(
                "a", "", {"src": text_node.url, "alt": text_node.text})
    return node
