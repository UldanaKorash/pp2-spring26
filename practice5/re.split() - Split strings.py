import re
text = "Python is fun and powerful"
words = re.split(r'\s+', text)
print("Words:", words)


import re
text = "apple,banana;cherry,orange;grape"
fruits = re.split(r'[;,]', text)
print("Fruits list:", fruits)