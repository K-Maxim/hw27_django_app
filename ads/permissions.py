from rest_framework.permissions import BasePermission

from ads.models import Ad
from users.models import User


class SelectionUpdateDeletePermission(BasePermission):
    message = 'You are not an admin or moderator'

    def has_permission(self, request, view):
        if request.user.role == User.ADMIN:
            return True

        if request.user.role == User.MODERATOR:
            return True

        return False


class AdUpdateDeletePermission(BasePermission):
    message = 'Only admins, moderators and users who created the ad'

    def has_permission(self, request, view):
        ad = Ad.objects.get(pk=view.kwargs['pk'])
        if ad.author_id == request.user.id:
            return True

        if request.user.role == User.ADMIN:
            return True

        if request.user.role == User.MODERATOR:
            return True

        return False