from django.shortcuts import render
from .models import Lead
import csv
from django.http import HttpResponse
from openpyxl import Workbook
# Create your views here.
def lead_list(request):

    leads = Lead.objects.all()

    query = request.GET.get('q')

    if query:
        leads = leads.filter(
            company_name__icontains=query
        )

    return render(
        request,
        'leads/lead_list.html',
        {
            'leads': leads
        }
    )


def export_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="leads.csv"'

    writer = csv.writer(response)

    writer.writerow([
        'Company Name',
        'Website',
        'Location',
    ])

    for lead in Lead.objects.all():

        writer.writerow([
            lead.company_name,
            lead.website,
            lead.location,
        ])

    return response



def export_excel(request):

    workbook = Workbook()

    worksheet = workbook.active
    worksheet.title = "Leads"

    worksheet.append([
        'Company Name',
        'Website',
        'Location',
    ])

    for lead in Lead.objects.all():

        worksheet.append([
            lead.company_name,
            lead.website,
            lead.location,
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    response['Content-Disposition'] = (
        'attachment; filename="leads.xlsx"'
    )

    workbook.save(response)

    return response