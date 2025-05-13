from django.shortcuts import render
import dashboard_app.dash_app
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')
