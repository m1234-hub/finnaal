from django.shortcuts import render
from django.views.generic import View




#  User authetication Under Development #


#from django.contrib import messages
#from validate_email import validate_email
#from django.contrib.auth.models import User
# Create your views here.


class RegistratiobView(View):
    def get(self, request):
      return render(request, 'register.html')


 #   def post(self,request):
        
  #      context={
   #        
    #       'data': request.POST,
     #      'has_error' : False

       # }
         

      #  email=request.POST.get('email')
       # password=request.POST.get('password')
#        password1=request.POST.get('password1')

 #       if len(password)<6:
  #         
   #       messages.add_message(request, messages.ERROR, 'please provide a vailde email')
    #      context['has_error']=True

     #   if password!=password1:
       ##   messages.add_message(request, messages.ERROR, 'please provide a vailde email')
      #    context['has_error']=True

        #if not validate_email(email):
         #  messages.add_message(request, messages.ERROR, 'please provide a vailde email')
          # context['has_error']=True
     
    
        #if User.objects.filter(email=email).exist():
         #  messages.add_message(request, messages.ERROR, 'please provide a vailde email')
          # context['has_error']=True
        
        #if User.objects.filter(username=username).exist():
         #  messages.add_message(request, messages.ERROR, 'please provide a vailde email')
          # context['has_error']=True

        #if context['has_error']:

         #return render(request, 'register.html', context) 
        
        #User=User.objects.create_user(username)
    


         