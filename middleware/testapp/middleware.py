class ExecutionFlowMiddleware(object):
    def __init__(self,get_response):
        print("init method executed")
        self.get_response=get_response

    def __call__(self,request):
        print("preprocess")
        response=self.get_response(request)
        print("post")
        return response