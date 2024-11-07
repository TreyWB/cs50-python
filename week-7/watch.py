import re
import sys


def main():
    print(f"\n", parse(input("HTML: ")), sep="")

def parse(html):
    match = re.search(r"src=\"https?://(?:www\.)?youtube\.com/embed/(.+?)\"", html)

    try:
        embed_link = match.group(1)
    except AttributeError:
        sys.exit("None")

    short_link = "https://youtu.be/" + embed_link
    
    return short_link


if __name__ == "__main__":
    main()