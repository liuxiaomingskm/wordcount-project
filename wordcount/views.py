from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary = {}
    for word in wordlist:
        worddictionary[word] = worddictionary.get(word,0) + 1

    sortedWords = sorted(worddictionary.items(), key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext': fulltext,'count': len(wordlist),'sortedWords':sortedWords})

def about(request):
    return render(request, 'about.html')