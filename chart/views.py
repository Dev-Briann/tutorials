from django.shortcuts import render
from chartit import DataPool,Chart,PivotChart
from .models import *

def SalesChartView(request):

    sales = DataPool(
        series=
            [{'options': {
               'source': SalesRecords.objects.all()},
              'terms': [
                'month',
                'sales',
                'expenses',
                ]}
             ])
    cht = Chart(
        datasource=sales,
        series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'month': [
                    'sales',
                    'expenses',
                    
                    ]
                  }}],
        chart_options =

              {'title': {
                   'text': 'Monthly Sales Report'
                   },

               'xAxis': {
                    'title': {'text': 'Month number'}
                       }
              }

    )
    context = {
        'cht' : cht,

    }
    return render(request,'sales.html',context)
