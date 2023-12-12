class AfterRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if hasattr(response, 'data'):
            if response.data.get("name", False):
                if response.data.get("artist", False):
                    print(f'Detail viewing of record "{response.data.get("name")}" {response.data.get("artist")}')
                else:
                    print(f'Detail viewing of collection "{response.data.get("name")}"')
                return response
            print(f'Not detail viewing')
            return response
        print(f'Not REST viewing')
        return response
