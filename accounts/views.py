from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse  # <-- needed for admin redirect

# ---------------- Login View ----------------
def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')  # Already logged in, go to home

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"✅ Welcome, {user.username}!")
            return redirect('index')  # Redirect to home after login
        else:
            messages.error(request, "❌ Invalid username or password.")
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')


# ---------------- Logout View ----------------
def logout_view(request):
    logout(request)
    messages.success(request, "✅ You have been logged out.")
    return redirect('login')
