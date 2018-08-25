from googlesearch import search
from bs4 import BeautifulSoup
import requests


i = 0
counter = 0

bookList = []
ratingList = []

goodreadsURL = ''
raingSoup = ''


def printingFunc():
    for k in range(len(bookList)):
        print((bookList[k]) + " " + (ratingList[k]))

print('Please enter the name of an author')
author = str(input())

#Runs google search to obtain authors goodreads
#profile url
for urlResult in search(author, num = 10, stop=10, pause=2):
    if 'goodreads' in urlResult:
        goodreadsURL = urlResult

goodreadsPage = requests.get(goodreadsURL)
soup = BeautifulSoup(goodreadsPage.content, 'html.parser')
titleHTML = soup.find_all(class_="bookTitle")

for book in titleHTML:
    book = (book.get_text())
    book = (str(book)) #Chaning from bs4 item to string
    book = (book.rstrip()) #Cleaning either side of the Title
    book = (book.lstrip())
    bookList.append(book) #Adds book to end of bookList list
    i += 1

for counter in bookList:
    ratingSearchPhrase = counter + ' goodreads'
    for ratingSearchPhrase in search(ratingSearchPhrase, num = 1, stop = 1, pause=2):
        ratingSearchURL = ratingSearchPhrase
        goodreadsRatingPage = requests.get(ratingSearchURL)
        ratingSoup = BeautifulSoup(goodreadsRatingPage.content, 'html.parser')
        rating = ratingSoup.find(class_="average")
        try:
            rating = (rating.get_text())
            rating = (str(rating))
            ratingList.append(rating)
        except AttributeError: #Assigns 0 when there is not a rating Available on GoodReads
            ratingList.append("0")
printingFunc();
