from bs4 import BeautifulSoup
import requests
import time

page = ''
while page == '':
    try:
        response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
        break
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(5)
        print("Was a nice sleep, now let me continue...")
        continue

web_archive = response.text

soup = BeautifulSoup(web_archive, 'html.parser')

all_titles = soup.find_all(name="h3", class_="title")
titles_list = []

for title in all_titles:
    titles_list.append(title.text)

titles_list.reverse()
print(titles_list)

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for ele in titles_list:
        file.write(f"{ele}\n")