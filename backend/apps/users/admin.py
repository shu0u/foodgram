from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models import Count

from apps.users.models import Subscription, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'id', 'username', 'email', 'first_name', 'last_name',
        'recipes_count', 'subscribers_count',
    )
    search_fields = ('username', 'email')
    list_filter = ('username', 'email')
    ordering = ('username',)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            _recipes_count=Count('recipes', distinct=True),
            _subscribers_count=Count('subscribers', distinct=True),
        )

    @admin.display(description='Рецептов')
    def recipes_count(self, obj):
        return obj._recipes_count

    @admin.display(description='Подписчиков')
    def subscribers_count(self, obj):
        return obj._subscribers_count


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'author')
    search_fields = ('user__username', 'author__username')
