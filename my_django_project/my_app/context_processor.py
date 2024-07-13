from datetime import datetime


''' If you wants to pass something i.e current time for every template then instead
of passing the current_time to every template for rendering, we can actually add 
it in context processor of settings.py, so that it will be automatically available
for all the templates without sending it every times for rendering '''
def current_time(request):
    return {
        'current_time': datetime.now()
    }