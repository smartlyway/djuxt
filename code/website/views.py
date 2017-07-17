from django.http import HttpResponse
import json, urllib


def ssr(uri=None, params=None):
    node = "http://node:9090"

    if uri:
         node += uri

    #return HttpResponse(uri)

    req = urllib.request.Request(node)

    if params:
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        jsondataasbytes = json.dumps(params).encode('utf-8')
        req.add_header('Content-Length', len(jsondataasbytes))
        r = urllib.request.urlopen(req, jsondataasbytes)
    else:
        r = urllib.request.urlopen(req)

    return HttpResponse(r)

    return HttpResponse("sss")


def forward_node(request):
    return ssr(uri= request.get_full_path())