from django.shortcuts import render, redirect
from .models import Expense, Category, Payment
#from .forms import ExpenseForm
from django.views.generic import CreateView, ListView,UpdateView, DeleteView,  DetailView

from  django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

@login_required
def index(request):
    categories= Category.objects.all()
    return render (request, 'expense/index.html')
@login_required
def expense_list(request):

    return render(request,"expense/expense_list.html")


def search(request):
    query=request.GET['search']

    results= Expense.objects.filter(Q(description__icontains=query))

    params={'results':results}
    return render(request,'expense/result.html',params)
#redirect('search',kwargs={'query': request.GET('query')})

def search_cate(request):
    query=request.GET['search']

    results= Category.objects.filter(Q(name__icontains=query))

    params={'results':results}
    return render(request,'expense/result_category.html',params)



@login_required
def expense_form(request):
    form = ExpenseForm()
    #categories= Category.objects.all()
    #payments= Payment.objects.all()
    #context={
        #'categories':categories,
        #'payments':payments

    #}
    return render(request,"expense/expense_form.html",  {'form': form})

@login_required
def expense_delete(request):
    return


class AddExpenseView(CreateView):
    model= Expense
    #form_class = ExpenseForm
    template_name='expense/expense_form.html'
    fields = ['description','amount','category','payment','payment_date']

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id))) this show the article just created.
        return reverse('expense-list')


class ExpenseListView(ListView):
	model = Expense

	template_name = 'expense/expense_list.html'
	context_object_name = 'expenses'

	ordering = ['-created_on']

	#paginate_by =1

class CategoryListView(ListView):
	model = Category

	template_name = 'expense/category_list.html'
	context_object_name = 'categories'

	#ordering = []

	#paginate_by =1

class ExpenseUpdateView(UpdateView):
    model = Expense
    template_name = 'expense/expense_update.html'
    fields = ['description','amount','category','payment','payment_date']


class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = 'expense/expense_delete.html'
    success_url = reverse_lazy('expense-list')





class AddCategoryView( CreateView):
    model = Category
    template_name = 'expense/cateblog_form.html'
    #form_class = ProductForm
    fields = ['name']
    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id))) this show the article just created.
        return reverse('category-list')


class CateblogDetailView( DetailView):
	model = Category

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'expense/cateblog_update_list.html'
    fields = ['name']
    def form_valid(self,form):
    		form.instance.author = self.request.user
    		return super(CategoryUpdateView, self).form_valid(form)

    def test_func(self):
    	category = self.get_object()
    	if self.request.user == category.author:
    		return True
    		return False


class CateblogListView(ListView):
    model = Category
    template_name = 'expense/list_cateblog.html'
    context_object_name = 'categories'
    #ordering = ['-date_posted']
    paginate_by =5
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        categories = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(categories, self.paginate_by)
        try:
            categories = paginator.page(page)
        except PageNotAnInteger:
            categories = paginator.page(1)
        except EmptyPage:
            categories = paginator.page(paginator.num_pages)
        context['categories'] = categories
        return context


class CategoryDeleteView( DeleteView):
    model = Category
    template_name = 'expense/category_confirm_delete.html'
    success_url = reverse_lazy('category-list')

    def test_func(self):
        category = self.get_object()
        if self.request.user == category.author:
                return True
                return False
