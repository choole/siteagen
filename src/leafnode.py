from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self,   tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError()
        elif self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def props_to_html(self):
        if self.props is None:
            return ""
        html_text = ""
        for item in self.props:
            html_text += f" {item}=\"{self.props[item]}\""
        return html_text

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"
