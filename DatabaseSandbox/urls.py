from django.conf.urls import url
from DatabaseSandbox.views import BasicUploadExample, UserAgentTracker, KubaNetAnalytics


# UploadDataTA

urlpatterns = [
    url(r'^KubaNetAnalytics/', KubaNetAnalytics.as_view(), name='KubaNetAnalytics'),
    url(r'^BasicUploadExample/', BasicUploadExample.as_view(), name='BasicUploadExample'),
    url(r'^UserAgentTracker/', UserAgentTracker.as_view(), name='UserAgentTracker'),

]

