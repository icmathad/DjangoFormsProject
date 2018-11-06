from django.shortcuts import render
from . import form


# Create your views here.

def index(request):
    return render(request, 'forms_app/index.html')


def form_view(request):
    forms = form.formName()

    if request.method == "POST":
        forms = form.formName(request.POST)

        if forms.is_valid():
            print("validation success..!")
            print("NAME :" + forms.cleaned_data['name'])
            print("E-mail :" + forms.cleaned_data['email'])
            print("TEXT :" + forms.cleaned_data['text'])
            print(forms.cleaned_data)

    return render(request, 'forms_app/form.html', {'forms': forms})
