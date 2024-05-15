#from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vc_count(request,st):
    st = st.lower()
    vowels = 'aeiou'
    vcount = 0
    ccount = 0
    for i in st:
        if i in vowels:
            vcount += 1
        else:
            ccount += 1
    ht = ("<html><body><h1><a href=\"https://github.com/Vigneshwaran-18\">Vowels and Consonants Count<a></h1><table "
          "border='1'><th>String</th><th>Vowels</th><th>Consonants</th><tr><td>%s</td><td>%d</td><td>%d</td></tr></table><br><p>Follow me at <a href=\"https://github.com/Vigneshwaran-18\">Vics-18</a></body></html>" % (st,vcount,ccount))
    return HttpResponse(ht)
