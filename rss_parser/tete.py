from typing import List, Optional, Sequence
import xml.etree.ElementTree as ET
import requests
import json as json_lib

REQ_TAGS = [
    "title",
    "link",
    "lastBuildDate",
    "pubDate",
    "language",
    "category",
    "managingEditor",
    "description",
]
REQ_ITEM_TAGS = [
    "title",
    "author",
    "pubDate",
    "link",
    "category",
    "description",
]
TAG_MAP = {
    "lastBuildDate": "Last Build Date",
    "pubDate": "Publish Date",
    "category": "Categories",
    "managingEditor": "Editor",
}


class UnhandledException(Exception):
    pass


"""
EX:
Feed: Yahoo News - Latest News & Headlines
Link: https://news.yahoo.com/rss
Description: Yahoo news description

Title: Nestor heads into Georgia after tornados damage Florida
Published: Sun, 20 Oct 2019 04:21:44 +0300
Link: https://news.yahoo.com/wet-weekend-tropical-storm-warnings-131131925.html

Nestor raced across Georgia as a post-tropical cyclone late Saturday, hours after the former tropical storm spawned a tornado that damaged homes and a school in central Florida while sparing areas of the Florida Panhandle devastated one year earlier by Hurricane Michael. The storm made landfall Saturday on St. Vincent Island, a nature preserve off Florida's northern Gulf Coast in a lightly populated area of the state, the National Hurricane Center said. Nestor was expected to bring 1 to 3 inches of rain to drought-stricken inland areas on its march across a swath of the U.S. Southeast... <--- !!! THIS IS DESCRIPTION !!!

Title: Some Other Title
Published: Sun, 20 Oct 2019 04:21:44 +0300
Link: https://some.other.link/some-other-news


Some other new cool information. <--- !!! THIS IS DESCRIPTION
"""


def parse_to_list(channel, items, limit=None):
    result = []

    for tag in REQ_TAGS:
        data = channel.findtext(tag)
        if data:
            tag_name = TAG_MAP.get(tag, tag.capitalize())
            if tag == "title":
                result.append(f"Feed: {data}")
            else:
                result.append(f"{tag_name}: {data}")

    for idx, item in enumerate(items):
        if limit and idx >= limit:
            break
        result.append("\n")
        for tag in REQ_ITEM_TAGS:
            data = item.findtext(tag)
            if data:
                tag_name = TAG_MAP.get(tag, tag.capitalize())
                if tag == "description":
                    result.append(f"\n{data}")
                else:
                    result.append(f"{tag_name}: {data}")
    return result


def parse_to_json(channel, items, limit):
    result = {}

    for tag in REQ_TAGS:
        data = channel.findtext(tag)
        if data:
            result[tag] = data

    item_list = []
    for idx, item in enumerate(items):
        if limit and idx >= limit:
            break
        item_data = {}
        for tag in REQ_ITEM_TAGS:
            data = item.findtext(tag)
            if data:
                item_data[tag] = data
        item_list.append(item_data)
    result["items"] = item_list
    return result


def rss_parser(
    xml: str,
    limit: Optional[int] = None,
    json: bool = False,
) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.

    Examples:
        >>> xml = '<rss><channel><title>Some RSS Channel</title><link>https://some.rss.com</link><description>Some RSS Channel</description></channel></rss>'
        >>> rss_parser(xml)
        ["Feed: Some RSS Channel",
        "Link: https://some.rss.com"]
        >>> print("\\n".join(rss_parser(xmls)))
        Feed: Some RSS Channel
        Link: https://some.rss.com
    <channel>...</channel> <!-- Required tags are <title>, <link>, <description>  but we are asking you to be able to parse <title>, <link>, <description>, <category>, <language>, <lastBuildDate>, <managingEditor>, <pubDate>, <item> -->
    <item>...</item> <!-- All of the fields here are optional, but each item should have at least <title> or <description>, but for the purposes of the test we are asking to be able to parse <title>, <author>, <pubDate>, <link>, <category>, <description> -->

    """

    root = ET.fromstring(xml)
    channel = root.find("channel")
    items = channel.findall("item")

    result = parse_to_list(channel, items, limit)

    if json:
        result = json_lib.dumps(parse_to_json(channel, items, limit), indent=2)

    return result


xml = requests.get("https://news.yahoo.com/rss").text
# xml = requests.get("https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en").text
# print("\n".join(rss_parser(xml, limit=1)))
print(rss_parser(xml, limit=2, json=True))
