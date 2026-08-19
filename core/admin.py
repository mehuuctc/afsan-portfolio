from django.contrib import admin
from django.db.models import Count


from .models import  Journey, Project, ProjectCategory,SkillCategory, Skill
from .models import AboutProfile, AboutFact,HeroSection,ContactInfo, ContactMessage
from .models import PageView, ProjectClick


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'badge_text', 'order', 'is_active')
    list_filter = ('category', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'description', 'tech_stack')



@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    list_display = ('title', 'period_and_company', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title', 'period_and_company', 'description')


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ('name', 'order', 'is_active')

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_wide', 'order', 'is_active')
    list_editable = ('is_wide', 'order', 'is_active')
    inlines = [SkillInline]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order', 'is_active')
    list_filter = ('category', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name',)


@admin.register(AboutProfile)
class AboutProfileAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)

@admin.register(AboutFact)
class AboutFactAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'order', 'is_active')
    list_editable = ('order', 'is_active')




@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'eyebrow', 'is_active')
    list_editable = ('is_active',)




@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'title', 'availability_status', 'is_active')
    list_editable = ('is_active',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')



@admin.register(PageView)
class PageViewAdmin(admin.ModelAdmin):
    list_display = ('path', 'ip_address', 'formatted_timestamp')
    list_filter = ('path', 'timestamp')
    search_fields = ('path', 'ip_address')
    readonly_fields = ('path', 'ip_address', 'user_agent', 'timestamp')

    # Custom date format for cleaner display
    def formatted_timestamp(self, obj):
        return obj.timestamp.strftime('%b %d, %Y - %I:%M %p')
    formatted_timestamp.short_description = 'Logged At'

    # Disable manual creation of page views in Admin UI
    def has_add_permission(self, request):
        return False


@admin.register(ProjectClick)
class ProjectClickAdmin(admin.ModelAdmin):
    list_display = ('project', 'click_type', 'timestamp')
    list_filter = ('click_type', 'project')
    search_fields = ('project__title',)

    def has_add_permission(self, request):
        return False