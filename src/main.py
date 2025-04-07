from textnode import TextNode, TextType

def main():
    # Create a TextNode object
    text_node = TextNode("This is some anchor text", TextType.LINKS, "https://www.boot.dev")
    
    # Print the TextNode object
    print(text_node)  # Should print the same representation


if __name__ == "__main__":
    main()