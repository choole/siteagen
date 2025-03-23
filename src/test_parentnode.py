import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("p", "first child")
        child2 = LeafNode("p", "second child")
        parent = ParentNode("div", [child1, child2])
        self.assertEqual(parent.to_html(),
                         "<div><p>first child</p><p>second child</p></div>")

    def test_to_html_with_no_children_raises_error(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", None).to_html()
        self.assertEqual(str(context.exception), "missing children")

    def test_to_html_with_no_tag_raises_error(self):
        child = LeafNode("span", "child")
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [child]).to_html()
        self.assertEqual(str(context.exception), "missing tag")

    def test_to_html_with_attributes(self):
        child = LeafNode("span", "child")
        parent = ParentNode(
            "div", [child], {"class": "container", "id": "main"})
        self.assertEqual(
            parent.to_html(), '<div class="container" id="main"><span>child</span></div>')

    def test_props_to_html_with_empty_props(self):
        parent = ParentNode("div", [LeafNode("span", "child")], {})
        self.assertEqual(parent.props_to_html(), "")

    def test_props_to_html_with_multiple_attributes(self):
        parent = ParentNode("div", [LeafNode("span", "child")], {
                            "class": "my-class", "style": "color:red;"})
        self.assertEqual(parent.props_to_html(),
                         ' class="my-class" style="color:red;"')

    def test_nested_empty_parent_nodes(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", [ParentNode("span", None)]).to_html()
        self.assertEqual(str(context.exception), "missing children")


if __name__ == "__main__":
    unittest.main()
