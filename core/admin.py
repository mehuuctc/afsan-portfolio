from django.contrib import admin
from .models import  Journey, Project, ProjectCategory,SkillCategory, Skill
from .models import AboutProfile, AboutFact,HeroSection,ContactInfo, ContactMessage



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
