from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
# Create your views here.


def home(request):
    form = SignUpForm(request.POST or None)
    #learn what this means
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'We will be in touch')
        #   redirects to a page upon success 
        return HttpResponseRedirect('/thank-you/');
    
    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))

def thankyou(request):
    return render_to_response("thankyou.html",
                              locals(),
                              context_instance=RequestContext(request))

def aboutus(request):
    return render_to_response("aboutus.html",
                              locals(),
                              context_instance=RequestContext(request))
