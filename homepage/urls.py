from django.urls import path
from .import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.store, name='store'),
    path('accounts/', views.accounts, name='accounts'),
    path('contact', views.contact, name='contact'),
    path('accounts/login', views.login_user, name='login'),  # these work when form is submitted
    path('accounts/register', views.register, name="register"),  # same with this one
    path('logout/', views.logout, name='logout'),  # when logout link is clicked
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.update_item, name='update_item'),
    path('checkout/process_order', views.processOrder, name='process_order'),
    path('user/', views.customer, name='customer'),
    path('delete_user/',views.deleteUser,name="delete_user"),
    path('update_email/',views.updateEmail,name="update_email"),
    path('verify_email/',views.verifyemail,name="verify_email"),
    path('delete_item/<str:pk>/',views.deleteItem,name="delete_item"),
    path('feedback/<str:pk>/',views.feedback,name="feedback"),
    # views for password resetting
    path('reset_password/', auth_view.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    path('reset_password_complete/', auth_view.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete")
]