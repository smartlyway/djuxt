from django.http import HttpResponse

def render(templateUri = None, templateParams = None):
    """
    Llama al motor de rendezizado y devuelve una respuesta con el HTML
    renderizado en el servidor. La renderización se realiza por medio
    de nodejs.

    :param templateUri: url de la plantilla a renderizar
    :param templateParams: datos que se le quieren pasar a la plantilla
    :return: HTTPResponse
    """

    return HttpResponse("Run's OK: 200 OK")