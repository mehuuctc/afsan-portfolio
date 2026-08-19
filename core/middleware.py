from .models import PageView

class AnalyticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Ignore static files, media, and admin paths
        path = request.path
        if not path.startswith('/static/') and not path.startswith('/media/') and not path.startswith('/admin/'):
            ip = request.META.get('HTTP_X_FORWARDED_FOR')
            if ip:
                ip = ip.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')

            PageView.objects.create(
                path=path,
                ip_address=ip,
                user_agent=request.META.get('HTTP_USER_AGENT', '')
            )

        response = self.get_response(request)
        return response