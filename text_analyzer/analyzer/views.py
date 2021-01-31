from django.shortcuts import render
from backend import ParserModel
from django.http import JsonResponse
import traceback

def analyze(request):
    return render(request, "analyze.html")


def get_prediction(request):
    print("get_prediction function")
    if request.is_ajax():
        try:
            response_data = {}
            text_val = request.POST["hebrew_text"]
            model_obj = ParserModel.ParserModel(text_val)
            response_data["prediction"] =  model_obj.prediction
            response_data["clean_massage"] =  model_obj.clean_massage
            response_data["probabilty"] =  model_obj.probabilty
            print(response_data)
            return JsonResponse(response_data)
        except:
            traceback.print_exc()
    return render(request, "analyze.html")
