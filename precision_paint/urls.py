"""precision_paint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from precision_paint_api.views.estimates import EstimateView
from precision_paint_api.views.invoices import InvoiceView

from precision_paint_api.views.work_order import WorkOrderView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'work_orders', WorkOrderView, 'work_order')
router.register(r'estimates', EstimateView, 'estimate')
router.register(r'invoices', InvoiceView, 'invoice')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))

]
