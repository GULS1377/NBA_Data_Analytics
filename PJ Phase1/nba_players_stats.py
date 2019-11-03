import csv
import string
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests


def main():
    # list to store player-stats-page urls
    player_list = []
    with open('player_url_list.csv', 'r', newline='') as textFile:
        csv_reader = csv.reader(textFile, delimiter='\n')
        for row in csv_reader:
            for url in row:
                player_list.append(url)
    # player's stats data terms
    stats_names = ['Season', 'Age', 'Tm', 'Lg', 'Pos', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA',
                   '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
    # scrape data
    n = 0
    for player in player_list:
        n = n + 1
        response = requests.get(player)
        if response.status_code == 404:
            print("404!")
        html = response.content

        soup = BeautifulSoup(html, 'html.parser')
        h1 = soup.find('h1', attrs={'itemprop': 'name'})
        name = h1.string

        tables = soup.find_all('table')
        tab = tables[0]
        t_head = set()
        for td in tab.thead.tr.find_all('th'):
            t_head.add(td.getText())

        # store career PerGame stats
        with open('player_career_stats.csv', 'a', newline='') as textFile:
            csv_writer = csv.writer(textFile)
            for tr in tab.tfoot.find_all('tr'):
                row = [name.encode("gbk", 'ignore').decode("gbk", 'ignore')]
                for stats_name in stats_names:
                    text = ''
                    if stats_name in t_head:
                        if stats_name == 'Season':
                            text = tr.findNext('th').getText()
                        else:
                            text = tr.findNext('td').getText()
                            tr = tr.findNext('td')
                    row.append(text.encode("gbk", 'ignore').decode("gbk", 'ignore'))
                csv_writer.writerow(row)
        print(n)


        # store PerGame stats each season
        with open('player_stats.csv', 'a', newline='') as textFile:
            csv_writer = csv.writer(textFile)
            for tr in tab.tbody.find_all('tr'):
                row = [name.encode("gbk", 'ignore').decode("gbk", 'ignore')]
                for stats_name in stats_names:
                    text = ''
                    if stats_name in t_head:
                        if stats_name == 'Season':
                            text = tr.findNext('th').getText()
                        else:
                            text = tr.findNext('td').getText()
                            tr = tr.findNext('td')
                    row.append(text.encode("gbk", 'ignore').decode("gbk", 'ignore'))
                csv_writer.writerow(row)
        print(n)


if __name__ == '__main__':
    main()




# url = "https://www.basketball-reference.com/players/b/barbole01.html"
# html = urlopen(url).read()
#
# soup = BeautifulSoup(html, 'html.parser')
# tables = soup.find_all('table')
# tab = tables[0]
#
# with open('barbole.csv', 'a', newline='') as textFile:
#     csv_writer = csv.writer(textFile)
#     for tr in tab.tbody.find_all('tr'):
#         row = []
#         for td in tr.find_all('td'):
#             text = td.getText()
#             row.append(text)
#         print(row)
#         csv_writer.writerow(row)


# url = "https://www.basketball-reference.com/players/"
# letters = []
# for letter in string.ascii_letters:
#     letters.append(letter)
# letters = letters[:26]
# n = 0
# for letter in letters:
#     response = requests.get(url+letter)
#     if response.status_code == 404:
#         print("404!")
#         continue
#     html = response.content
#     soup = BeautifulSoup(html, 'html.parser')
#     n += int(soup.find(name='span', attrs={'class': 'section_anchor', 'id': 'players_link'})['data-label'].split()[0])
# print(n)
