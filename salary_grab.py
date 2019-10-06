from bs4 import BeautifulSoup
import bs4
import requests

def getSalary(url):
    contents = requests.get(url).text
    # fp = open("Kobe Bryant Stats _ Basketball-Reference.com.html", encoding="utf-8")
    # contents = fp.read()
    soup = BeautifulSoup(contents, "html.parser")
    name = soup.find("div", {"id":"meta"}).find("h1").string
    divs1 = soup.find(id="all_all_salaries")
    if(divs1==None):
        print(url,"None")
    else:
        print(url,"starts")
        divs=divs1.find("div", {"class":"placeholder"}).next_siblings
        for div in divs:
            if type(div) == bs4.element.Comment:
                soup = BeautifulSoup(div.string, "html.parser")
                tbody = soup.find("tbody")
                trs = tbody.find_all("tr")
                output = open("result.csv", "a",encoding="utf-8")
                # output.write("name,season,team_nam,Lg,salary\n")
                for tr in trs:
                    th = tr.find("th")
                    output.write(name)
                    output.write("," + th.string)
                    tds = tr.find_all("td")
                    output.write("," + str(tds[0].string))
                    output.write("," + str(tds[1].string))
                    # salary = tds[2].string.replace(",","")
                    cont= tds[2].contents
                    if(len(cont)==0):
                        output.write(",None")
                        output.write("\n")
                    else:
                        salary = tds[2].contents[0].replace(",","")
                        output.write("," + str(salary))
                        output.write("\n")
                output.close()

# if __name__ == '__main__':
#     url="https://www.basketball-reference.com/players/s/shengto01.html"
#     getSalary(url)