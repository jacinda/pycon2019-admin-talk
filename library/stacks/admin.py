from django.contrib import admin

from .models import Author, Book, LoanedBook
from django.db.models import Count


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ("first_name", "last_name")
    list_display = ("first_name", "last_name", "book_count")  # 'articles_count')

    def get_queryset(self, request):
        qs = super(AuthorAdmin, self).get_queryset(request)
        qs = qs.annotate(
            book_count=Count("works")
        )  # , articles_count=Count('articles'))
        return qs


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("__unicode__", "authors_display")
    fieldsets = (
        (
            "Identifying Information",
            {
                "fields": (
                    "title",
                    "page_count",
                    "authors",
                    "call_number",
                    "item_number",
                )
            },
        ),
        (
            "Loan Information",
            {
                "fields": (
                    "borrowing_period",
                    "max_renewal_count",
                    "daily_fine",
                    "maximum_fine",
                )
            },
        ),
    )
    filter_horizontal = ("authors",)
    list_max_show_all = 600
    list_select_related = True

    def get_queryset(self, request):
        qs = super(BookAdmin, self).get_queryset(request)
        qs = qs.prefetch_related("authors")
        return qs

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super(BookAdmin, self).get_readonly_fields(request, obj)
        # If we're creating a new Book, anyone can edit
        if not obj:
            return readonly_fields
        else:
            if request.user.groups.filter(name="Employed Librarians").exists():
                return readonly_fields
            else:
                return readonly_fields + ("call_number",)


class LoanedBookInline(admin.TabularInline):
    model = LoanedBook
    extra = 1


@admin.register(LoanedBook)
class LoanedBookAdmin(admin.ModelAdmin):
    # list_display = ('patron', 'book')
    # list_display = ('__unicode__', 'is_overdue', 'highlighted_due_date', 'fine')
    list_select_related = ("patron", "book")
    show_full_result_count = False

    def get_queryset(self, request):
        qs = super(LoanedBookAdmin, self).get_queryset(request)
        # qs = qs.select_related('patron', 'book').only('patron__first_name', 'patron__last_name', 'book__title')
        qs = qs.only("patron__first_name", "patron__last_name", "book__title")
        return qs
