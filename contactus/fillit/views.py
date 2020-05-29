from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ContactForm

# Views START FROM HERE
def contact(request):
    if request.method == "POST":
      cc = ContactForm(request.POST)
      if cc.is_valid():

          name = cc.cleaned_data['name']
          mail=cc.cleaned_data['mail']
          message=cc.cleaned_data['message']
          subject=cc.cleaned_data['subject']
          query=cc.cleaned_data['query']
          cc.save()
          return redirect('contact') 
    else:
      cc = ContactForm(request.POST)
    parms={
        
        
    }
    return render(request, 'contact.html', parms)
