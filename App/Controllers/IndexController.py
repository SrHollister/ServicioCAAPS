from django.shortcuts import render,HttpResponse

class IndexController():
    def index(request):
        #return HttpResponse('<h1>SrHollister</h1>%s' % year)
        return render(request, 'Views/Index/index.html')
    
    def about(request):
        return render(request, 'Views/Index/about.html')
