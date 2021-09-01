from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth import get_user_model
from .models import Message
from django.urls import reverse
from django.contrib import messages
from review.models import Review
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EditProfileForm
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


def MessageView(request, username):
    User = get_user_model()
    message_user = get_object_or_404(User, username=username)
    all_messages = message_user.messages.all()
    if request.method == 'POST':
        message = request.POST['message']
        user_new_message = Message.objects.create(
            customuser=message_user, text=message)
        user_new_message.save()
        messages.success(request, 'Added')
        return redirect('account_signup')

    return render(request, 'message.html', {'all_messages': all_messages,
                                            'message_user': message_user, })


class UserProfile(TemplateView):
    template_name = 'user_profile.html'


CustomUser = get_user_model()


def EditProfile(request):
    user = get_object_or_404(get_user_model(), username=username)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            pass

    form = EditProfileForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})

# class EditProfile(UpdateView):
#     model = CustomUser
#     fields = ['username', 'email']
#     template_name = 'edit_profile.html'
#     # form_class = EditProfileForm
#     def get_queryset(self):
#         return get_user_model().objects.filter(username=self.kwargs['username'])


def delete_message(request, m_id):
    message_instance = get_object_or_404(Message, id=m_id)
    user = message_instance.customuser
    message_instance.delete()
    message_instance.save()

    return redirect(user.get_absolute_url())


def spam_message(request, user_id):
    message_instance = get_object_or_404(Message, id=user_id)
    user = message_instance.customuser
    message_instance.text = 'The owner has marked this message as a spam.'
    message_instance.save()

    return redirect(user.get_absolute_url())


class AbouUs(TemplateView):
    template_name = 'about.html'


class ContactUs(TemplateView):
    template_name = 'contact.html'


def ReviewView(request):
    reviews = Review.objects.all()
    template_name = "review.html"
    paginator = Paginator(reviews, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, template_name, {'page_obj': page_obj})


def SettingsView(request):

    return render(request, 'settings.html', {})


def AddReview(request):
    if request.method == 'POST':
        name = request.POST['name']
        review = request.POST['review']
        occupation = request.POST['occupation']

        new_review = Review.objects.create(
            name=name, review=review, occupation=occupation)
        new_review.save()
        messages.success(request, 'Review submitted successfully')
    return render(request, 'add_review.html', {})
