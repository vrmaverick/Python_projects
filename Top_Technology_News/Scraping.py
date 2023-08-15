import requests
from bs4 import BeautifulSoup
import pprint
def main():
  mega_subtext = []
  mega_links = []

  def sort_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

  def create_custom_hn(links, subtext):
    hn = []

    for idx, item in enumerate(links):
      title = item.getText()
      href = item.get('href', None)
      vote = subtext[idx].select('.score')

      if len(vote):
        points = int(vote[0].getText().replace(' points', ''))

        if points > 99:
          hn.append({'title': title, 'link': href, 'votes': points})

    return sort_by_votes(hn)


  while(True):
    
    try:
      pages_to_scrape = int(input("Enter nummber of pages of hacker news you want to scrape and get top stories : "))

      if pages_to_scrape < 10 and pages_to_scrape > 0 :

        for i in range(pages_to_scrape):
          res = requests.get(f'https://news.ycombinator.com/news?p={i}')
          # res2 = requests.get('https://news.ycombinator.com/news?p=2')
          soup = BeautifulSoup(res.text, 'html.parser')
          # soup2 = BeautifulSoup(res2.text, 'html.parser')
          links = soup.select('.titleline > a') #storylink changed to .titleline
          subtext = soup.select('.subtext')
          # links2 = soup2.select('.titleline > a')#storylink changed to .titleline
          # subtext2 = soup2.select('.subtext')
          mega_links = mega_links + links
          mega_subtext = mega_subtext + subtext

        pprint.pprint(create_custom_hn(mega_links, mega_subtext))
        break

      else:
        print("Please Enter a number less than 10")

    except ValueError :
      print("Enter a Number !!!! less than 10")

if __name__ == '__main__':
  main()

