from django.shortcuts import render
from django.http import HttpResponse
from last_kgo.settings import *
from django.core.paginator import Paginator
from .models import *
from .forms import *
import openpyxl


def home(request):
    return render(request, 'base.html')


def export_to_excel(data_list):
    # Create an in-memory output file for the new workbook.
    output = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    output['Content-Disposition'] = 'attachment; filename=universities_data.xlsx'

    # Create workbook and worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Universities Data"

    # Define the titles for columns
    columns = [
        'Program Code', 'Department Name', 'University Name',
        'University Type', 'Genel Kontenjan', 'İlk Yerleşme Oranı', 'Puan Türü', 'Yıl'
    ]
    row_num = 1

    # Assign the titles for each cell of the header
    for col_num, column_title in enumerate(columns, 1):
        cell = ws.cell(row=row_num, column=col_num)
        cell.value = column_title

    # Write data to cells
    for item in data_list:
        row_num += 1
        row = [
            item.pro_code, item.bolum_adi, item.üniversite,
            item.üniversite_türü, item.genel_kontenjan, item.i_lk_yerleşme_oranı,
            item.puan_türü, item.yil
        ]
        for col_num, cell_value in enumerate(row, 1):
            cell = ws.cell(row=row_num, column=col_num)
            cell.value = cell_value

    # Save the workbook to the response
    wb.save(output)
    return output


def filters_page(request):
    form = YourModelFilterForm(request.GET)
    data_list = GenelBilgilerLast2024.objects.all()

    if form.is_valid():
        university_type = form.cleaned_data.get('university_type')
        university_name = form.cleaned_data.get('university_name')
        year = form.cleaned_data.get('year')
        if university_type:
            data_list = data_list.filter(üniversite_türü=university_type)
        if university_name:
            data_list = data_list.filter(üniversite=university_name)
        if year:
            data_list = data_list.filter(yil=year)

    if 'export' in request.GET:
        return export_to_excel(data_list)

    paginator = Paginator(data_list, 50)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'form': form
    }

    return render(request, 'filters.html', context)


def contact_us(request):
    return render(request, 'contact.html')


def old_hc_data_page(request):
    return render(request, 'hc.html')


def compare_page(request):
    form = CompareUniversitiesForm()
    university_left_data = None
    university_right_data = None
    university_name_left = None
    university_name_right = None

    if request.method == 'POST':
        form = CompareUniversitiesForm(request.POST)
        if form.is_valid():
            university_name_left = form.cleaned_data['university_name_left']
            university_name_right = form.cleaned_data['university_name_right']
            major_name_left = form.cleaned_data['major_name_left']
            major_name_right = form.cleaned_data['major_name_right']
            university_type_left = form.cleaned_data['university_type_left']
            university_type_right = form.cleaned_data['university_type_right']
            year_left = form.cleaned_data['year_left']
            year_right = form.cleaned_data['year_right']

            left_filter = {}
            right_filter = {}

            if university_name_left:
                left_filter['üniversite'] = university_name_left
            if university_type_left:
                left_filter['üniversite_türü'] = university_type_left
            if year_left:
                left_filter['yil'] = year_left
            if major_name_left:
                left_filter['bolum_adi'] = major_name_left

            if university_name_right:
                right_filter['üniversite'] = university_name_right
            if university_type_right:
                right_filter['üniversite_türü'] = university_type_right
            if year_right:
                right_filter['yil'] = year_right
            if major_name_right:
                right_filter['bolum_adi'] = major_name_right

            university_left_data = GenelBilgilerLast2024.objects.filter(**left_filter)
            university_right_data = GenelBilgilerLast2024.objects.filter(**right_filter)

    context = {
        'form': form,
        'university_left_data': university_left_data,
        'university_right_data': university_right_data,
        'university_name_left': university_name_left,
        'university_name_right': university_name_right,
    }

    return render(request, 'compare.html', context)
