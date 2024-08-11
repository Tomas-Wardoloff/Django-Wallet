from django.contrib import admin

from .models import Category


class DefaultCategoryFilter(admin.SimpleListFilter):
    title = 'default category'
    parameter_name = 'default'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'Yes'),
            ('no', 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(user__isnull=True)
        if self.value() == 'no':
            return queryset.filter(user__isnull=False)
        return queryset


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_filter = ['type', DefaultCategoryFilter]
    list_display = ['name', 'type', 'user']


admin.site.register(Category, CategoryAdmin)
