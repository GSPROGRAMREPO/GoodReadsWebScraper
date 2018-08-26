from googlesearch import search
from bs4 import BeautifulSoup
import requests

bookList = []
ratingList = []

def printingFunc():
    for k in range(len(bookList)):
        print((bookList[k]) + " " + (ratingList[k]))

def mainFunction():
    
    i = 0
    counter = 0
    
    goodreadsURL = ''
    raingSoup = ''

    author = input('Please enter the name of an author \n')

    #Runs google search to obtain authors goodreads
    for urlResult in search(author, num = 10, stop=10, pause=2):
        if 'goodreads' in urlResult:
            goodreadsURL = urlResult

    goodreadsPage = requests.get(goodreadsURL)
    soup = BeautifulSoup(goodreadsPage.content, 'html.parser')
    titleHTML = soup.find_all(class_="bookTitle")

    for book in titleHTML:
        book = book.get_text()
        book = str(book) #Chaning from bs4 item to string
        book = book.strip()
        bookList.append(book)
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
            except AttributeError: #Assigns 0 when there is not a rating available
                ratingList.append("0")

mainFunction();         
printingFunc();
