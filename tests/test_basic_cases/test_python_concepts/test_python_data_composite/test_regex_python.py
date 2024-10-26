import re
multilinetext = "I began with result dict: { hi this is the text on line1\
        followed by on line2\
        and line3 but here is a catch on line 4 \
        Here, I have a }"

text = "abbbbbbccc"

re_obj = re.compile(r".")
print(f"re match {re_obj.match(text)}\n")
print(f"re search {re_obj.search(text)}\n")

re_obj = re.compile(r"^")
print(f"re match {re_obj.match(text)}\n")
print(f"re search {re_obj.search(text)}\n")

re_obj = re.compile(r"$")
print(f"re match {re_obj.match(text)}\n")
print(f"re search {re_obj.search(text)}\n")
