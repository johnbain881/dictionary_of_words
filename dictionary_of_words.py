"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["bellicose"] = "inclined or eager to fight; aggressively hostile; belligerent; pugnacious."
word_definitions["hollow"] = "having a space or cavity inside; not solid; empty:"
"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
# print(word_definitions["bellicose"])
# print(word_definitions["hollow"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for word, definition in word_definitions.items():
  print(f"The definition of {word} is {definition}")

