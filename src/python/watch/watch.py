import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    html = re.search(r".*(\"http.*youtube.*title=).*", s)
    if html:
        link = str(html[1])
        updated_link = link.replace(' title=', '').replace('"', '')
        return(updated_link)
    
if __name__ == "__main__":
    main()