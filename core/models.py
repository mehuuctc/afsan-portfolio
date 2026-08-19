from tkinter import CASCADE

from django.db import models



class ProjectCategory(models.Model):
    name = models.CharField(max_length=50, help_text="Display name, e.g. Generative AI")
    slug = models.SlugField(max_length=50, unique=True, help_text="Filter identifier, e.g. genai, backend, data, other")

    class Meta:
        verbose_name_plural = "Project Categories"

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, related_name='projects')
    badge_text = models.CharField(max_length=50, default="Featured", help_text="e.g. Featured, PostgreSQL, Django")
    description = models.TextField()
    
    # Tech stack as plain text or comma-separated
    tech_stack = models.CharField(max_length=255, help_text="e.g. Python · Streamlit · Gemini API · Pydantic")
    
    # Feature Bullet Points (optional multiline text field)
    features = models.TextField(
        blank=True, 
        null=True, 
        help_text="Enter key feature bullet points on new lines."
    )
    
    # Links
    source_code_url = models.URLField(blank=True, null=True)
    live_demo_url = models.URLField(blank=True, null=True)
    
    # Ordering & Visibility
    order = models.PositiveIntegerField(default=0, help_text="Smaller numbers appear first")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return self.title

    def features_list(self):
        """Splits multiline features string into a clean list for the template."""
        if self.features:
            return [line.strip().lstrip('-').strip() for line in self.features.strip().splitlines() if line.strip()]
        return []





class Journey(models.Model):
    title = models.CharField(max_length=200, help_text="e.g. AI Engineer")
    period_and_company = models.CharField(
        max_length=255, 
        help_text="e.g. Freelance / Remote / Various clients - (2025 — Present)"
    )
    description = models.TextField(
        help_text="Enter bullet points or paragraphs. You can use HTML like or separate lines."
    )
    order = models.PositiveIntegerField(
        default=0, 
        help_text="Controls display order (smaller numbers appear first)."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', '-id']
        verbose_name = 'Journey Entry'
        verbose_name_plural = 'Journey Entries'

    def __str__(self):
        return f"{self.title} ({self.period_and_company})"




class SkillCategory(models.Model):
    name = models.CharField(
        max_length=100, 
        help_text="e.g. Programming, Backend / Tools & Infra, AI / Generative AI"
    )
    is_wide = models.BooleanField(
        default=False, 
        help_text="Check this to add the 'skill-card-wide' class for multi-column / wide layout cards."
    )
    order = models.PositiveIntegerField(
        default=0, 
        help_text="Controls display order of categories (smaller numbers appear first)."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory, 
        on_delete=models.CASCADE, 
        related_name='skills'
    )
    name = models.CharField(max_length=100, help_text="e.g. Python, Django, RAG, Docker")
    order = models.PositiveIntegerField(
        default=0, 
        help_text="Controls display order inside the category."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.name} ({self.category.name})"




class AboutProfile(models.Model):
    title = models.CharField(
        max_length=255, 
        default="From Django backends to production AI applications."
    )
    body = models.TextField(
        help_text="Enter bio paragraphs. Use line breaks to separate paragraphs."
    )
    is_active = models.BooleanField(
        default=True, 
        help_text="Select one active profile to show on the main page."
    )

    class Meta:
        verbose_name = "About Profile"
        verbose_name_plural = "About Profiles"

    def __str__(self):
        return self.title


class AboutFact(models.Model):
    label = models.CharField(max_length=100, help_text="e.g. Base, Status, Core stack, Focus")
    value = models.CharField(max_length=255, help_text="e.g. Chattogram, Bangladesh")
    order = models.PositiveIntegerField(
        default=0, 
        help_text="Controls display order (smaller numbers appear first)."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "About Fact"
        verbose_name_plural = "About Facts"

    def __str__(self):
        return f"{self.label}: {self.value}"




class HeroSection(models.Model):
    eyebrow = models.CharField(
        max_length=255, 
        default="AI Engineer · Generative AI · Python / Django"
    )
    title = models.CharField(
        max_length=255, 
        default="Afsan Habib — Building AI-Powered Systems"
    )
    subtitle = models.TextField(
        default="AI Engineer focused on practical, AI-powered applications — RAG pipelines, LLM tooling, and prompt-driven workflows — built on a backend foundation of Python and Django. I integrate language models into real systems rather than train them from scratch."
    )
    
    # CTA Buttons
    primary_cta_text = models.CharField(max_length=100, default="View Projects")
    primary_cta_link = models.CharField(max_length=255, default="#projects")
    secondary_cta_text = models.CharField(max_length=100, default="Contact Me")
    secondary_cta_link = models.CharField(max_length=255, default="#contact")

    # Status / Availability Links
    status_text_1 = models.CharField(max_length=100, default="Open to freelance & contract")
    status_link_1 = models.URLField(default="https://github.com/AfsanHabib")
    status_text_2 = models.CharField(max_length=100, default="Remote — available worldwide")
    status_link_2 = models.URLField(default="https://www.linkedin.com/in/afsan-habib-566340215/")

    # Profile Image
    profile_image = models.ImageField(
        upload_to='hero/', 
        blank=True, 
        null=True, 
        help_text="Upload custom profile photo. If empty, falls back to default static image."
    )
    
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"

    def __str__(self):
        return self.title





class ContactInfo(models.Model):
    title = models.CharField(max_length=255, default="Building something with AI?")
    lead_text = models.CharField(max_length=255, default="Let's Work Together")
    email = models.EmailField(default="afsan.uct@gmail.com")
    github_url = models.URLField(default="https://github.com/AfsanHabib")
    availability_title = models.CharField(max_length=100, default="Availability -")
    availability_status = models.CharField(max_length=255, default="Open to freelance & contract")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Contact Info Settings"
        verbose_name_plural = "Contact Info Settings"

    def __str__(self):
        return f"Contact Details ({self.email})"


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"




class PageView(models.Model):
    path = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.path} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


class ProjectClick(models.Model):
    # project = models.ForeignKey('Project', on_delete=CASCADE, related_name='clicks')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='clicks')
    click_type = models.CharField(max_length=50, choices=[('github', 'GitHub'), ('demo', 'Live Demo')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.title} - {self.click_type} ({self.timestamp.strftime('%Y-%m-%d')})"