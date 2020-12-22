



import xml.etree.cElementTree as ET
import os

posts = 'Posts.xml'
badges = 'Badges.xml'
tags = 'Tags.xml'
users = 'Users.xml'
votes = 'Votes.xml'

def get_file_size_in_mb(filename):
    file_size = 0
    if os.path.isfile(filename):
        file_size = os.path.getsize(filename)
        file_size = round(file_size / (1024**2),2)
    return str(file_size)+'MB'

def read_xml_file(filename):
    x = 0
    for event, elem in ET.iterparse(filename):
        print(event,x)
        x+=1
        if elem.tag == 'record_tag' and event == 'end':
            print(elem.text)
            elem.clear()
    
if __name__ == '__main__':
    filename = badges
    read_xml_file(filename)
    
