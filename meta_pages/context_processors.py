from .models import Schema, MetaTag

def meta(request):
    if MetaTag.objects.filter(url=request.path).exists():
        return {'meta':MetaTag.objects.get(url=request.path)}
    return {'meta':None}


def schema(request):
    if Schema.objects.filter(url=request.path).exists():
        return {'schema':Schema.objects.get(url=request.path)}
    return {'schema':None}

