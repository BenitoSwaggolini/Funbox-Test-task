import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Link


@api_view(['POST'])
def visited_links(request, *args, **kwargs):
    try:
        for link in request.data.get('links'):
            try:
                Link.objects.create(link=link)
            except:
                continue
        return Response({"status": "ok"})
    except Exception as error:
        return Response({"status": f"{error}"})


@api_view(["GET"])
def visited_domains(request, *args, **kwargs):
    date = datetime.datetime.now().timestamp()
    from_date = request.GET.get('from', 0)
    to_date = request.GET.get('to', date)

    try:
        from_date = float(from_date)
        to_date = float(to_date)
    except ValueError:
        response = {'status': 'Wrong parameter'}
        return Response({"status": "error"})

    queryset = []
    for link in Link.objects.group_by('link').all():
        if from_date <= date <= to_date:
            queryset.append(link)
    return Response({"status": "ok", "domains": queryset})
