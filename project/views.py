from django.shortcuts import render
from django.http import HttpResponse
from project.Similarity import main

from django.core.files.storage import FileSystemStorage
# Create your views here.
def form_index(request):
    if request.method == 'POST':
        file1 = request.POST['file_1']
        file2 = request.POST['file_2']
        cal = main.main(file1,file2)
        contex = {'cal':cal}
        return render(request,'app/hasil.html',contex)
    return render(request,'app/index.html')
    # return render(request, 'app/index.html')

def similarity(request):
    # if request.method == 'POST':
    #     file1 = request.FILES['file_1']
    #     file2 = request.FILES['file_2']

        #fs = FileSystemStorage()
        #filename1 = fs.save(file1.name, file1)
        # filename2 = fs.save(file2.name, file2)
        # uploaded_file_url1 = fs.url(filename1)
        # uploaded_file_url2 = fs.url(filename2)

        # cal = main.main(file1,file2)
        # contex = {'cal':cal}
        # return render(request,'app/index.html',contex)
    return render(request,'app/index.html')