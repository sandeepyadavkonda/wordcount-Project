from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    word_dict = dict()
    for word in wordlist:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1

    return render(request, 'count.html', {'fulltext': fulltext, 'count':len(wordlist), 'word_dict': word_dict.items()})
