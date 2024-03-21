from django.shortcuts import render
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


# Create your views here.
def index_view(request):
    return render(request, 'index.html')


def predictdata_view(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    else:
        data = CustomData(
            gender=request.POST.get('gender'),
            race_ethnicity=request.POST.get('ethnicity'),
            parental_level_of_education=request.POST.get('parental_level_of_education'),
            lunch=request.POST.get('lunch'),
            test_preparation_course=request.POST.get('test_preparation_course'),
            reading_score=float(request.POST.get('writing_score')),
            writing_score=float(request.POST.get('reading_score')),
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline = PredictPipeline()
        print("Mid Prediction")
        results = predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render(request, 'home.html', {'results': results[0]})
