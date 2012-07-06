import base64
import hmac
import time
import uuid

from django.conf import settings
from django.contrib.auth import authenticate
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext as _
from tastypie.http import HttpUnauthorized


from tastypie.authentication import Authentication, ApiKeyAuthentication

class ApiKeyOnlyAuthentication(ApiKeyAuthentication):
    """
    Handles API key auth, in which a user provides an API key.
    
    The same as tastypie.authentication.ApiKeyAuthentication, but doesn't 
    require a username.
        """

    def extract_credentials(self, request):
        if request.META.get('HTTP_AUTHORIZATION') and request.META['HTTP_AUTHORIZATION'].lower().startswith('apikey '):
            (auth_type, data) = request.META['HTTP_AUTHORIZATION'].split()

            if auth_type.lower() != 'apikey':
                raise ValueError("Incorrect authorization header.")

            api_key = data
        else:
            api_key = request.GET.get('api_key') or request.POST.get('api_key')

        return api_key

    def is_authenticated(self, request, **kwargs):
        """
        Finds the user and checks their API key.

        Should return either ``True`` if allowed, ``False`` if not or an
        ``HttpResponse`` if you need something custom.
        """
        from django.contrib.auth.models import User

        try:
            api_key = self.extract_credentials(request)
        except ValueError:
            return self._unauthorized()

        if not api_key:
            return self._unauthorized()

        return self.get_key(api_key)

    def get_key(self, api_key):
        """
        Attempts to find the API key for the user. Uses ``ApiKey`` by default
        but can be overridden.
        """
        from tastypie.models import ApiKey

        try:
            ApiKey.objects.get(key=api_key)
        except ApiKey.DoesNotExist:
            return self._unauthorized()

        return True

    def get_identifier(self, request):
        """
        Provides a unique string identifier for the requestor.

        This implementation returns the user's username.
        """
        api_key = self.extract_credentials(request)
        return 'nouser'

class PrivateDataAuthentication(ApiKeyOnlyAuthentication):
    def is_authenticated(self, request, **kwargs):
        """
        Finds the user and checks their API key.

        Should return either ``True`` if allowed, ``False`` if not or an
        ``HttpResponse`` if you need something custom.
        """
        from django.contrib.auth.models import User

        try:
            api_key = self.extract_credentials(request)
        except ValueError:
            return self._unauthorized()

        if not api_key:
            return self._unauthorized()
        api_model = self.get_key(api_key)
        if not api_model:
            return self._unauthorized()
        if api_model.user.permissionlevel.private_access:
            return True
        else:
            return self._unauthorized()
        
    def get_key(self, api_key):
        """
        Attempts to find the API key for the user. Uses ``ApiKey`` by default
        but can be overridden.
        """
        from tastypie.models import ApiKey

        try:
            ApiKey = ApiKey.objects.get(key=api_key)
            return ApiKey
        except ApiKey.DoesNotExist:
            return self._unauthorized()

    
        