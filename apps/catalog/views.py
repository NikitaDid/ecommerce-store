from apps.catalog.models import Category, Product
from django.views import generic


class CategoryIndexView(generic.ListView):
    model = Category
    template_name = 'catalog/category_list.html'  # Check if changes needed
    queryset = Category.objects.filter(parent=None)  # only want top-level categories
    context_object_name = 'categories'


class ProductsByCategoryView(generic.ListView):  # list of each category products
    template_name = 'catalog/products_list.html'
    # category = None
    # categories = Category.objects.all()
    model = Product
    context_object_name = 'products'


    # defines the list of objects that will be displayed in the template and saves the category for further work
    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug']) # self.kwargs['slug'] - <slug:slug>
        queryset = Product.objects.filter(categories=self.category)
        return queryset

    # updating the main method get_context_data (which has to have **kwargs when u have CBV) with category we founded un get_queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'catalog/product.html'
