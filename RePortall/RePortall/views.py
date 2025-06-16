from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib import messages
from .forms import createUserForm
from .decorators import unauthenticated_user
from .models import Review, Customer, ReportSubmission


def homepage(request):
    return render(request, "index.html")


@login_required(login_url='login')
def admin_dashboard(request):
     customers = Customer.objects.all()
     reviews = Review.objects.filter(reportsubmission__isnull=False).distinct()
     total_customers = customers.count()
     total_reviews = reviews.count()
     context = {
          'customers': customers,
          'reviews': reviews,
          'total_customers': total_customers,
          'total_reviews': total_reviews
     }
     return render(request, "admin_dashboard.html", context)

@login_required(login_url='login')
def customer(request, pk):
     user = User.objects.get(id=pk)
     customer = Customer.objects.get(user=user)
     reportsubmission = ReportSubmission.objects.filter(customer=customer)
     total_report= reportsubmission.count()
     context = {'customer': customer, 'reportsubmission' : reportsubmission, 'total_report': total_report}  
     return render(request, "customer.html", context)

@login_required(login_url='login')
def savereport(request):
     if request.method == "POST":
          name = request.POST.get('name')
          description = request.POST.get('description')
          address = request.POST.get('address')
          phone = request.POST.get('phone')
          date_created = request.POST.get('date_created')
          
          data = Review(name=name, description=description, address=address, phone=phone, date_created=date_created)
          data.save()
          
          user = request.user
          customer = Customer.objects.get(user=user)
          
          review = Review.objects.create(
            name=name,
            phone=phone,
            description=description,
            address=address
          ) 
          
          ReportSubmission.objects.create(
            customer=customer,
            review=review
          )
          
          return redirect('customer', pk=user.id) 
          
     return render(request, "customer.html")         


@login_required(login_url='login')
def review(request):
     savedreviews = Review.objects.filter(reportsubmission__isnull=False).distinct()
     context = {'reviews': savedreviews}
     return render(request, "review.html", context)

def aboutUs(request):
     return render(request, "aboutUs.html")
 
def contactUs(request):
     return render(request, "contactUs.html")

@unauthenticated_user
def login_page(request):
     if request.method == "POST":
          username = request.POST.get('username')
          password = request.POST.get('password')
          
          user = authenticate(request, username=username, password=password)
          
          if user is not None:
               login(request, user)
               return redirect('after_login')
          else:
               messages.info(request, 'Username or Password is incorrect')
     
     context={}     
     return render(request, "login.html", context)
     
          
def logout_page(request):
     logout(request)
     return redirect('login')          

@unauthenticated_user
def signup(request):
    form = createUserForm()
    
    if request.method == "POST":
        form = createUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Now we create the related customer
            Customer.objects.create(
                user=user,
                name=user.username,
                email=user.email
            )
            messages.success(request, f'Account created successfully! Welcome, {user.username}')
            return redirect('login')  # Make sure 'login' is a valid URL name
        else:
            print("Form is invalid:", form.errors)  # Debug: shows you what's wrong

    context = {'form': form}
    return render(request, 'signup.html', context)  # Always return a response

# @login_required(login_url='login')
# def report(request):
#      return render(request, "report.html") 



@login_required(login_url='login')
def after_login_redirect(request):
    user = request.user
    if user.is_staff:  # For admin
        return redirect('admin_dashboard')
    else:
     #    try:
          #   customer = Customer.objects.get(user=user)
          #   return redirect('customer', pk=customer.user.id)
     #    except Customer.DoesNotExist:
          return redirect('review')
       
       
       
       
@login_required(login_url='login')
def update_review(request, pk):
    submission = get_object_or_404(ReportSubmission, id=pk, customer__user=request.user)
    review = submission.review

    if request.method == 'POST':
        review.description = request.POST.get('description')
        review.address = request.POST.get('address')
        review.save()
        return redirect('customer', pk=request.user.id)

    context = {'review': review}
    return render(request, 'update_review.html', context) 


@login_required(login_url='login')
def delete_review(request, pk):
    submission = get_object_or_404(ReportSubmission, id=pk, customer__user=request.user)
    review = submission.review
    if request.method == 'POST':
        review.delete()
        submission.delete()
        return redirect('customer', pk=request.user.id)
    return render(request, 'delete_confirm.html', {'submission': submission})
      
      
      
      
# from django.contrib.admin.views.decorators import staff_member_required
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Review, ReportSubmission

@staff_member_required(login_url='login')
def update_review_admin(request, pk):
    review = get_object_or_404(Review, id=pk)
    report = ReportSubmission.objects.filter(review=review).first()

    if not report:
        return redirect('admin_dashboard')

    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(ReportSubmission.STATUS):
            report.status = new_status
            report.save()
            return redirect('admin_dashboard')

    context = {
        'report': report,
        'status_choices': ReportSubmission.STATUS
    }
    return render(request, 'update_review_admin.html', context)



@staff_member_required(login_url='login')
def delete_review_admin(request, pk):
    review = get_object_or_404(Review, id=pk)
    report = ReportSubmission.objects.filter(review=review).first()

    if not report or report.status != 'Completed':
        return redirect('admin_dashboard')

    if request.method == 'POST':
        report.delete()
        review.delete()
        return redirect('admin_dashboard')

    context = {'review': review, 'report': report}
    return render(request, 'delete_review_admin.html', context)


     