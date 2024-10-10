from django.shortcuts import render,HttpResponse
from base.models import past_values

# Create your views here.
def helloworld(request):
    if  request.method == "POST":
        val1 = int(request.POST.get("text1"))
        val2 = int(request.POST.get("text2"))
        dropdown = request.POST.get("dropdown")
        output = 0
        if dropdown == 'add':
            output = val1+val2
        elif dropdown == 'sub':
            output = val1-val2
        elif dropdown == 'div':
            output = val1//val2
        obj = past_values(text1=val1, text2=val2, val=output)
        obj.save()
        return render(request,"sample.html", {"op":output})

    return render(request,"sample.html")

def history(request):
    return  render(request,"history.html",{"values":past_values.objects.all()})
