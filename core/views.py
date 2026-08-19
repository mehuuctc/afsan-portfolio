import resend


from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings


from django.db.models import Prefetch
from .forms import ContactForm

from .models import (
    Project, Journey,ProjectCategory,SkillCategory, Skill,
    AboutProfile, AboutFact, HeroSection,ContactInfo
)



def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # 1. Save message to Database
            contact_msg = form.save()

            # 2. Trigger Resend Email API
            try:
                resend.api_key = settings.RESEND_API_KEY

                resend.Emails.send({
                    "from": "Portfolio ",  # Default free testing domain provided by Resend
                    "to": "afsan.uct@gmail.com",                  # Your recipient email address
                    "subject": f"New Contact: {contact_msg.subject}",
                    "html": f"""
                        New Portfolio Contact Submission
                        Name: {contact_msg.name}
                        Email: {contact_msg.email}
                        Subject: {contact_msg.subject}
                        
                        Message:
                        {contact_msg.message}
                    """
                })
                print("Resend email sent successfully!")
            except Exception as e:
                print(f"Resend error: {e}")

            messages.success(request, "Thank you! Your message has been sent successfully.")
            return redirect('index')
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = ContactForm()

    # Query context data
    hero = HeroSection.objects.filter(is_active=True).first()
    categories = ProjectCategory.objects.all()
    projects = Project.objects.filter(is_active=True).select_related('category')
    journey_items = Journey.objects.filter(is_active=True)
    
    skill_categories = SkillCategory.objects.filter(is_active=True).prefetch_related(
        Prefetch('skills', queryset=Skill.objects.filter(is_active=True))
    )

    about_profile = AboutProfile.objects.filter(is_active=True).first()
    about_facts = AboutFact.objects.filter(is_active=True)
    contact_info = ContactInfo.objects.filter(is_active=True).first()

    context = {
        'hero': hero,
        'categories': categories,
        'projects': projects,
        'journey_items': journey_items,
        'skill_categories': skill_categories,
        'about_profile': about_profile,
        'about_facts': about_facts,
        'contact_info': contact_info,
        'form': form,
    }
    return render(request, 'index.html', context)
