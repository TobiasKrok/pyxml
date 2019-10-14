from xml.dom import minidom

xml_file = minidom.parse("ViewActions.xml")

nodes = ("textInput", "textInputService", "values", "domainObjectList", "selectService", "type")
xml_file.getElementsByTagName("textInput")
found_keys = []
missing_keys = []


def get_node_keys(node_list):
    atrs = ("label", "groupId", "hintText", "prompt", "help", "description")
    for element in node_list:
        for atr in atrs:
            if element.hasAttribute(atr):
                if not (element.getAttribute(atr + "Key")).__eq__(""):
                    found_keys.append(str(element.getAttribute(atr + "Key") + "=" + (element.getAttribute(atr))))
                else:
                    missing_keys.append(str(element.nodeValue))


for node in nodes:
    get_node_keys(xml_file.getElementsByTagName(node))

print(found_keys)
print(missing_keys)
