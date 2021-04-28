from django.shortcuts import render
from .models import AiModel
from .forms import AimodelUploadForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def upload_form(request):
    if request.method == 'POST':
        pass

    form = AimodelUploadForm()
    return render(request,'storage/add_ai_model.html',{'UploadForm':form})

def view_ai_models(request):
    return render(request, 'storage/view_ai_model.html',{})