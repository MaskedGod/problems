# You can use similar logic when you need to ensure that a certain substring or prefix is found at the start of another string:
# Matching URL Paths
url = "/home/user/documents"
path = "/home/user"
while url.find(path) != 0:
    path = path[0 : len(path) - 1]
print(path)  # Output: "/home/user"


# This can be used to find the longest matching path in URLs.
#  Verifying file extensions
filename = "example.txt"
extension = ".txt"
while filename.find(extension) != len(filename) - len(extension):
    extension = extension[1:]  # strip the first character
print(extension)  # Output: ".txt"

# This ensures that the extension is correctly at the end of the filename.
# Finding common substring
str1 = "abcd"
str2 = "abef"
common_substring = str1
while str2.find(common_substring) != 0:
    common_substring = common_substring[:-1]
print(common_substring)  # Output: "ab"
