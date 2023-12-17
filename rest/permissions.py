from rest_framework import permissions


class AdminChangeRecordPermission(permissions.BasePermission):
    message = 'You don\'t have permission to change information about records.'

    # пользователи не могут вносить изменения в записи, только администратор
    def has_permission(self, request, view):
        if view.action not in ('list', 'retrieve'):
            return bool(request.user and request.user.is_staff)
        return True
