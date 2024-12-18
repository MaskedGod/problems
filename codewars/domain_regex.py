import re


def get_domain_name(url):
    # Regex to match and capture the domain name part
    pattern = r"(https?://)?(www\.)?([a-zA-Z0-9-]+)\."
    match = re.search(pattern, url)
    if match:
        return match.group(3)
    return None


print(get_domain_name("http://codewars.com"))
print(get_domain_name("www.xakep.ru"))
print(get_domain_name("icann.org"))
