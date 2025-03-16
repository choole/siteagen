import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("p", "PARAGRAPH", "", {
                        "href": "www.google.com", "style": "{width:100px}"})
        self.assertEqual(node.props_to_html(),
                         " href=\"www.google.com\" style=\"{width:100px}\"")

    def test_props2(self):
        node2 = HTMLNode("a", "anchor", "smth", {
            "href": "www.boot.dev", "target": "_blank"})
        self.assertEqual(node2.props_to_html(),
                         " href=\"www.boot.dev\" target=\"_blank\"")

    def test_not_eq_type(self):
        node3 = HTMLNode("h1", "Header1", "header", {"style": "{width:100px}"})
        self.assertEqual(node3.props_to_html(),
                         " style=\"{width:100px}\"")


if __name__ == "__main__":
    unittest.main()
