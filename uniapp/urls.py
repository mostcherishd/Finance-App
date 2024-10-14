from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index' ),
    path('login_user', views.login_user, name='login_user' ),
    path('logout_user', views.logout_user, name='logout_user' ),
    path('main_base', views.main_base, name='main_base' ),
    path('dashboard', views.dashboard, name='dashboard' ),
    path('dashbase', views.dashbase, name='dashbase' ),
    path('transaction', views.transaction, name='transaction' ),
    path('create_deposit', views.create_deposit, name='create_deposit' ),
    path('main_dash', views.main_dash, name='main_dash' ),
    path('deposit_history', views.deposit_history, name='deposit_history' ),
    path('invest_plan', views.invest_plan, name='invest_plan' ),
    path('invest_history', views.invest_history, name='invest_history' ),
    path('payout', views.payout, name='payout' ),
    path('register', views.register_user, name='register' ),
]
 