import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Othman</name>
    <phone type="intl">
        +965 900 90 999
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print("Name:", tree.find("name").text)
print("Attr:", tree.find("email").get("hide"))