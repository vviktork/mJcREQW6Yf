import json
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.views import View
from marshmallow import Schema, fields
from marshmallow.validate import Length, Range
from marshmallow import ValidationError #as MarshmallowError
from .dot_graph import dot_graf
from .image_graph import image_graph


class Servis2Schema(Schema):
    formula = fields.Str(validator=Length(6, 7), required=True)
    interval = fields.Integer(validator=Range(1, 365), required=True)
    dt = fields.Integer(validator=Range(1, 24), required=True)


class Servis2View(View):

    def get(self,request):
        return HttpResponse(status=400)

    def post(self, request):
        try:
            document = json.loads(request.body.decode())
            schema = Servis2Schema()
            data = schema.load(document)
            response = {'data': dot_graf(data)}
            return JsonResponse(response, status=201)
        except json.JSONDecodeError:
            return JsonResponse(status=400)
        except ValidationError:
            return JsonResponse(status=400)


class Servis3View(View):

    def get(self,request):
        return HttpResponse(status=400)

    def post(self, request):
        try:
            document = json.loads(request.body.decode('utf-8'))
            response = {'data': image_graph(document['data'])}
            return JsonResponse(response, status=201)
        except json.JSONDecodeError:
            return JsonResponse(status=400)
        except ValidationError:
            return JsonResponse(status=400)