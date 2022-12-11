# from rest_framework import permissions
#
#
# class IsStudentPermissions(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if DefaultUser.objects.get(pk=self.request.user.pk).group == 'S':
#             return True
#         return False
#
#
# class IsCompanyPermissions(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if DefaultUser.objects.get(pk=self.request.user.pk).group == 'C':
#             return True
#         return False
