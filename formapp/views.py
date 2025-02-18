from django.shortcuts import render
from .forms import FeedbackForm
from .models import Feedback

def feedback(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            Feedback.objects.create(name=name, email=email, phone=phone, message=message)
            return render(request, 'formapp/success.html')
    return render(request, 'formapp/feedback.html', {'form': form})