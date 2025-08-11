from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').lower().strip()
        password = request.POST.get('password', '')
        
        # Simple authentication logic
        if username == 'admin' and password:
            # Redirect to admin dashboard
            return redirect('admin_dashboard')
        elif username == 'user' and password:
            # Redirect to user landing page
            return redirect('user_landing')
        else:
            # Invalid credentials - stay on login page
            return render(request, 'main/login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'main/login.html')

def dashboard(request):
    return render(request, 'main/landing.html')

def compliance_actions(request):
    return render(request, 'main/compliance_actions.html')

def compliance_management(request):
    return render(request, 'main/compliance_management.html')

def compliance_creation(request):
    return render(request, 'main/compliance_creation.html')

<<<<<<< HEAD
def admin_compliance_creation(request):
    return render(request, 'main/admin_compliance_creation.html')

=======
>>>>>>> 76feacddb31ba2e99e6bb87737255db39260bd6b
def compliance_edit_delete(request):
    return render(request, 'main/compliance_edit_delete.html')

def create_user(request):
    return render(request, 'main/create_user.html')

def edit_credentials(request):
    return render(request, 'main/edit_credentials.html')

def password_change(request):
    return render(request, 'main/password_change.html')

def edit_compliance(request):
    return render(request, 'main/edit_compliance.html')

def user_landing(request):
    return render(request, 'main/user_landing.html')

def compliance_details(request, selected_date):
    # Mock data for compliances - in a real app, this would come from a database
    # Filter compliances based on the selected date
    mock_compliances = [
        {
            'id': 'gyphyui87654',
            'task': 'Monthly Financial Report',
            'department': 'Finance',
            'deadline': f'{selected_date}/7/25',
            'status': 'Pending'
        },
        {
            'id': 'gyphyui86525',
            'task': 'Regulatory Compliance Check',
            'department': 'Legal',
            'deadline': f'{selected_date}/7/25',
            'status': 'In Progress'
        },
        {
            'id': 'acvdefft59432',
            'task': 'Safety Audit Report',
            'department': 'Operations',
            'deadline': f'{selected_date}/7/25',
            'status': 'Pending'
        }
    ]
    
    # For demo purposes, show compliances for dates 7, 13, 16, and 25
    if selected_date in ['7', '13', '16', '25']:
        compliances = mock_compliances
    else:
        compliances = []
    
    context = {
        'selected_date': selected_date,
        'compliances': compliances
    }
    
    return render(request, 'main/compliance_details.html', context)

def user_dashboard(request):
    return render(request, 'main/user_dashboard.html')

def admin_dashboard(request):
<<<<<<< HEAD
    return render(request, 'main/admin_dashboard_new.html')
=======
    return render(request, 'main/admin_dashboard.html')
>>>>>>> 76feacddb31ba2e99e6bb87737255db39260bd6b
