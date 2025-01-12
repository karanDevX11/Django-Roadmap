from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile


# Create your views here.

# def store_file(file):
#     with open("temp/image.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()   #instantiate the Profileform
        return render(request, "profiles/create_profile.html", {
            "form": form
        })

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)  #fetches the submitted data as well as submitted forms
        if submitted_form.is_valid():     #validates the form
            profile = UserProfile(image = request.FILES["user_image"])      #sets the image from the user_image and adds to model
            profile.save()                                               #stores file path to the database
            return HttpResponseRedirect("/profiles")
        
        return render(request, "profiles/create_profile.html", {
            "form": submitted_form
        })

        
