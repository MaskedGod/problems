"""Implement a pagination class helpful for arranging text on pages and listing content on the given page. The class should take in a text and a positive integer, which indicate how many symbols will be allowed per page (take spaces into account as well).

You need to get the number of whole symbols in the text, get the number of pages that came out and the method that accepts the page number, and return the number of symbols on this page. If the provided number of the page is missing, raise an exception with the message "Invalid index. Page is missing".

Implement searching/filtering pages by using symbols/words and displaying pages with all the symbols on them. If the provided symbols/words are missing, raise an exception with the message "'<symbol/word>' is missing on the pages".

If you're querying by a symbol that appears on many pages or if you are querying by the word that is split in two, return an array of all the occurrences.

Pages indexing starts with 0.

Example:

>>> pages = Pagination('Your beautiful text', 5)
>>> pages.page_count
4
>>> pages.item_count
19

>>> pages.count_items_on_page(0)
5
>>> pages.count_items_on_page(3)
4
>>> pages.count_items_on_page(4)
Exception: Invalid index. Page is missing.
>>> pages.find_page('Your')
[0]
>>> pages.find_page('e')
[1, 3]
>>> pages.find_page('beautiful')
[1, 2]
>>> pages.find_page('great')
Exception: 'great' is missing on the pages
>>> pages.display_page(0)
'Your '"""

from math import ceil


class Pagination:
    def __init__(self, data, items_on_page):
        self.data = data
        self.items_on_page = items_on_page
        self.content = self.paginate()

    @property
    def page_count(self):
        return ceil(len(self.data) / self.items_on_page)

    @property
    def item_count(self):
        return len(self.data)

    def paginate(self):
        temp = ""
        paginated = {}
        page_num = 0
        for char in self.data:
            if len(temp) == self.items_on_page:
                paginated[page_num] = temp
                temp = ""
                page_num += 1
                temp += char
            else:
                temp += char

        if temp:
            paginated[page_num] = temp

        return paginated

    def count_items_on_page(self, page_number):
        try:
            page = len(self.content.get(page_number))

            if page is None:
                raise IndexError("Invalid index. Page is missing.")
        except IndexError as e:
            print(f"Exception: {e}")
        else:
            return page

    def find_page(self, data):
        result = []

        if data:
            for i, v in self.content.items():
                if data in v or v.strip() in data:
                    result.append(i)
            if not result:
                raise Exception(f"'{data}' is missing on the pages")

        return result

    def display_page(self, page_number):

        page = self.content.get(page_number)

        if page is None:
            raise Exception("Invalid index. Page is missing.")

        return page


pages = Pagination("Y", 5)
print(pages.page_count)

"""
class Pagination:
    def __init__(self, data, items_on_page):
        self.data = data
        self.items_on_page = items_on_page
        self.content = self.paginate()

    @property
    def page_count(self):
        return round(len(self.data) / self.items_on_page)

    @property
    def item_count(self):
        return len(self.data)

    def paginate(self):
        temp = ""
        paginated = {}
        page_num = 0
        for char in self.data:
            if len(temp) == self.items_on_page:
                paginated[page_num] = temp
                temp = ""
                page_num += 1
                temp += char
            else:
                temp += char

        if temp:
            paginated[page_num] = temp

        return paginated

    def count_items_on_page(self, page_number):
        try:
            page = len(self.content.get(page_number))

            if page is None:
                raise IndexError("Invalid index. Page is missing.")
        except IndexError as e:
            print(f"Exception: {e}")
        else:
            return page

    def find_page(self, data):
        result = []

        if data:
            try:
                for i, v in self.content.items():
                    if data in v:
                        result.append(i)
                if not result:
                    raise ValueError(f"'{data}' is missing on the pages")
            except ValueError as e:
                print(f"Exception {e}")

        return result

    def display_page(self, page_number):
        try:
            page = self.content.get(page_number)

            if page is None:
                raise IndexError("Invalid index. Page is missing.")
        except IndexError as e:
            print(f"Exception: {e}")
        else:
            return page

"""
