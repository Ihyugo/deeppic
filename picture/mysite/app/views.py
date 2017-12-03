from django.shortcuts import render,render_to_response
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from .models import FileUpload
from .forms import UploadForm
import pdb
# Create your views here.

@csrf_protect
def index(request):
	fileform = UploadForm(request.FILES or None, request.FILES or None)
	if request.method == 'POST':
		if fileform.is_valid():
			file = FileUpload(picture_1=request.FILES['picture_1'], picture_2=request.FILES['picture_2'])
			file.save()

	c={}
	c.update(csrf(request))

	c["name"] = "django"
	c["form"] = UploadForm
	return render(request, 'app/index.html', c)
