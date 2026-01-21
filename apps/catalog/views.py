from django.shortcuts import render, redirect

from apps.catalog.models import Category, Product, Comment
from apps.catalog.forms import CommentForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['comments'] = Comment.objects.filter(product=product,is_checked=True).order_by('-created_at')
        context['form'] = CommentForm()
        return context


def create_comment(request, pk, slug):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        data = request.POST.copy()
        data.update(product=pk, slug=slug)

        if not request.user.is_anonymous:
            user = request.user
            data.update({
                "name": f"{user.last_name} {user.first_name}",
                "is_checked": True,
                "email": user.email,
                "user": user,
            })

        request.POST = data
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return render(request, 'catalog/comment_created.html',{
                "comment": comment,
                "product": product
            })
        else:
            print(form.errors)

