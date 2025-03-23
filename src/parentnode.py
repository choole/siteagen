from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("missing tag")
        elif self.children is None:
            raise ValueError("missing children")
        else:
            html_text = f"<{self.tag}{self.props_to_html()}>"
            for item in self.children:
                html_text += item.to_html()
            html_text += f"</{self.tag}>"
            return html_text

    def props_to_html(self):
        if self.props is None:
            return ""
        html_text = ""
        for item in self.props:
            html_text += f" {item}=\"{self.props[item]}\""
        return html_text

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"
