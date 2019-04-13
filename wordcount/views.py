
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET["fulltext"]
    word_list = fulltext.split()
    
    word_dict = {}
    
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    
    sortedwords = sorted( word_dict.items(), key=operator.itemgetter(1), reverse=True  )    
     
        
    return render(request, 'count.html', 
                  {'fulltext': fulltext, 'word_list': len(word_list), 'sorted_word':sortedwords }
                 )


def about_us(request):
    return render(request, 'about_us.html')


##def judah(request):
    ##return HttpResponse("<h2>Judah is so alive baby!!!!!</h2>")