
Project idea: The aim of the project is to create a place where everyone can donate unnecessary things to trusted institutions. 
A registered user can donate. To log in, the user must provide an e-mail address and password.


** APP SUMMARY **

MODELS: 5.

Account (AbstractUser),
Category, 
Institution,
Donation

FORMS:

LoginForm,
RegisterForm,
DonationModelForm

VIEWS:

'', LandingPageView
'add_donation/', AddDonationView
'confirmation/', ConfirmationView
'user/', UserPageView
'user/<int:donation_id>/', UserPageDetailView
'login/', LoginView
'logout/', LogoutView
'register/', RegisterView
