from.models import Junle


def common(request):

    params = {
        'junle_list': Junle.objects.all()
    }
    return params


