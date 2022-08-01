import wikipediaapi

wiki = wikipediaapi.Wikipedia("en")
search = input("What do you want to search for? ")
page = wiki.page(search)
while not page.exists():
    print("That does not exist.")
    search = input("What do you want to search for? ")
    page = wiki.page(search)

item = input("What do you want to retrieve from the page? (summary, url, text, sections, categories) ")
choices = ["summary", "url", "text", "sections", "categories"]
lower = item.lower()
result = lower in choices
while not result:
    item = input("What do you want to retrieve from the page? (summary, url, text, sections, categories) ")
    lower = item.lower()
    result = lower in choices

if lower == "summary":
    print(page.summary)
elif lower == "url":
    print(page.url)
elif lower == "text":
    print(page.text)
elif lower == "sections":
    print(page.sections)
elif lower == "categories":
    print(page.categories)

