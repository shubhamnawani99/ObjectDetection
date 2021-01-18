from django.shortcuts import render,redirect,HttpResponse,Http404
from django.utils.encoding  import smart_str
from YOLO import main
import os
# Create your views here.

def handle_uploaded_file(f):  
    with open('media/input/test.jpg' , 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  

def download(request):
    file_path = 'media/output/testoutput.jpg'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/force-download")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def index(request):
	if request.method == 'POST':
		img = request.FILES.get('imginput',False)
		if img == False:
			return redirect('index')
		print(img)
		handle_uploaded_file(img)
		main.run()
		return redirect('output')
	
	return render(request,'index.html')

def output(request):
	return render(request,'output.html')