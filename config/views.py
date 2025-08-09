from django.http import HttpResponse

def welcome(request):
    html_content = """
    <html>
      <head><title>Welcome to E-Commerce API</title></head>
      <body>
        <h1>Welcome to the E-Commerce API !!</h1>
        <p>
          <a href="/swagger/">Swagger UI</a><br>
          <a href="/docs/">API Documentation</a>
        </p>
      </body>
    </html>
    """
    return HttpResponse(html_content)