class XmlElementType():
    ELEMENT_UNKNOWN = 1
    ELEMENT_OPENING_TAG = 2
    ELEMENT_CLOSING_TAG = 3
    ELEMENT_TEXT = 4

# trim spaces from both sides
def trim(st):
    print(st.strip())

class XmlElement:
    def __init__(self):
        self.element_type = XmlElementType.ELEMENT_UNKNOWN
        self.node_name = ""

class XmlTokenizer:
    def __init__(self, xml_str):
        self.xml = xml_str
        self.current_index = 0

    def get_next_element(self, element):
        i = self.xml.find("<", self.current_index)

        if i == -1:
            return False

        temp = self.xml[self.current_index : i]
        temp = temp.strip()

        if len(temp) != 0:
            element.node_name = temp
            element.element_type = XmlElementType.ELEMENT_TEXT
      
            self.current_index = i
            return True

        j = self.xml.find(">", i)
    
        if self.xml[i+1] == '/':
            element.node_name = self.xml[i + 2 : j]
            element.element_type = XmlElementType.ELEMENT_CLOSING_TAG
        else:

            element.node_name = self.xml[i + 1 : j]
            element.element_type = XmlElementType.ELEMENT_OPENING_TAG

        self.current_index = j + 1
        return True

class Node:
    def __init__(self, name):
        self.node_name = name
        self.children = []

def create_xml_tree(xml):
  
    tok = XmlTokenizer(xml)
    element = XmlElement()

    if tok.get_next_element(element) == False:
        return None

    print(element.node_name)

    st = []
    root = Node(element.node_name)
    st.append(root)

    while tok.get_next_element(element) == True:

        print(element.node_name)

        n = None
        if (element.element_type == XmlElementType.ELEMENT_OPENING_TAG or
             element.element_type == XmlElementType.ELEMENT_TEXT):
            n = Node(element.node_name)
            st[-1].children.append(n)

        if element.element_type == XmlElementType.ELEMENT_OPENING_TAG:
            st.append(n)
        elif element.element_type == XmlElementType.ELEMENT_CLOSING_TAG:
            st.pop()

    return root