from rest_framework import permissions
from broadcasts.models import Broadcasting, Channel

class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        bk = request.POST['bk']
        broadcasting = Broadcasting.objects.get(pk=int(bk))
        channel = broadcasting.channel
        
        if channel.public_channel:
            return True
        elif request.user.is_authenticated():
            if request.user in channel.members.all() or request.user == channel.owner:
                return True
            else:
                return False
        else:
            return False