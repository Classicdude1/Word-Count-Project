from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def count(request):
    full_text = request.GET["fulltext"]
    word_list = full_text.split()
    
    return render(request,"count.html",{"count":len(word_list),"fulltext":full_text, })


    