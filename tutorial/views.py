from django.shortcuts import redirect
def login_redirect(requests):
	return redirect('/accounts/login/')