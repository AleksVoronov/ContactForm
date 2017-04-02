from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import auth, messages
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from .models import Contact

#Форма обратной связи
def contact(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['name']
			second_name = form.cleaned_data['second_name']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']
			recipients = ['info@avitosoft24.ru']
			try:
				send_mail(subject, message, 'info@avitosoft24.ru', recipients)
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			post = form.save()
			post.save()
			return render(request, 'contactform/thank.html')					
	else:
			form = ContactForm()
	return render(request, 'contactform/cont.html', {'form': form })


