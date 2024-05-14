#from django.shortcuts import render
from django.http import HttpResponse

def mt(request,n,m):
    ht = "<html><body><h1><a href=\"https://github.com/Vigneshwaran-18\">Multiplication Table</a></h1><table border='1'><th>Num1</th><th>Num2</th><th>Result</th>"
    for i in range(1,m+1):
        ht += "<tr><td>%d</td><td>%d</td><td>%d</td></tr>" % (n,i,n*i)
    ht += "</table><br><p>Follow me at <a href=\"https://github.com/Vigneshwaran-18\">Vics-18</a></body></html>"
    return HttpResponse(ht)

def hw(request):
    htm = "<!DOCTYPE html><html><head><script type=\"Text/Javascript\"><body><input type=\"Number\" id=\"n\" placeholder=\"Enter a number\"><input type=\"Number\" id=\"m\" placeholder=\"Enter a number\"><button onclick=\"window.location.href='/mtab/'+document.getElementById('n').value+'/'+document.getElementById('m').value\">Generate Table</button></body></html>"
    return HttpResponse(htm)