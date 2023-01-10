from bs4 import BeautifulSoup
# import lxml


with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)


for tag in all_anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading.string)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.string)

company_url = soup.select_one(selector="p a")
print(company_url)

headings = soup.select(".heading")
print(headings)
