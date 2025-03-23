import unittest

from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), "<a href=\"https://www.google.com\">Click!</a>")

    def test_leaf_to_html_img(self):
        node = LeafNode("img", "Click!", {
                        "src": "https://www.google.com", "alt": "idk"})
        self.assertEqual(
            node.to_html(), "<img src=\"https://www.google.com\" alt=\"idk\">Click!</img>")

    def test_leaf_to_html_img_valueError(self):
        node = LeafNode("a", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_tagless(self):
        node = LeafNode(None, "smth")
        self.assertEqual(
            node.to_html(), "smth")


if __name__ == "__main__":
    unittest.main()
