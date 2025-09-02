# apps/sharedapp/middleware.py

class LoggingsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code executed BEFORE the view is called (request hook)
        print(f"Request received for: {request.path}")
        # Example: Add a custom header to the request
        # request.custom_data = "Some important data"

        response = self.get_response(request)

        # Code executed AFTER the view is called (response hook)
        print(f"Response status code: {response.status_code}")
        # Example: Add a custom header to the response
        # response['X-My-Custom-Header'] = 'Processed by MyCustomMiddleware'

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Optional: Code executed just before the view function is called
        print(f"Processing view: {view_func.cls.__name__}")
        return None # Return None to continue processing, or an HttpResponse to short-circuit

    def process_exception(self, request, exception):
        # Optional: Code executed if an exception occurs during view processing
        print(f"Exception caught: {exception}")
        return None # Return None to let Django handle it, or an HttpResponse for custom error page