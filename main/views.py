from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import OuterRef, Subquery, F
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
        'University Type', 'Burs Türü', 'Genel Kontenjan', 'İlk Yerleşme Oranı', 'Puan Türü', 'Yıl'
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
            item.get('pro_code'), item.get('bolum_adi'), item.get('üniversite'),
            item.get('üniversite_türü'), item.get('burs_türü'), item.get('genel_kontenjan'),
            item.get('i_lk_yerleşme_oranı'),
            item.get('puan_türü'), item.get('yil')
        ]
        for col_num, cell_value in enumerate(row, 1):
            cell = ws.cell(row=row_num, column=col_num)
            cell.value = cell_value

    # Save the workbook to the response
    wb.save(output)
    return output


def filters_page(request):
    form = YourModelFilterForm(request.GET)
    data_list = GenelBilgilerLast2024.objects.all().order_by('üniversite')

    if form.is_valid():
        university_type = form.cleaned_data.get('university_type')
        university_name = form.cleaned_data.get('university_name')
        year = form.cleaned_data.get('year')
        scholarship = form.cleaned_data.get('scholarship')
        major_name = form.cleaned_data.get('major_name')

        if university_type:
            data_list = data_list.filter(üniversite_türü=university_type)
        if university_name:
            data_list = data_list.filter(üniversite=university_name)
        if major_name:
            data_list = data_list.filter(bolum_adi=major_name)
        if year:
            try:
                year = int(year)
                data_list = data_list.filter(yil=year)
            except ValueError:
                print("passing..")
                pass
        if scholarship:
            data_list = data_list.filter(burs_türü=scholarship)

        request.session['filtered_data'] = []
        request.session['filtered_data'] = list(data_list.values())

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form.fields['university_type'].choices = [('', 'Hepsi')] + [(choice, choice) for choice in
                                                                    data_list.values_list('üniversite_türü',
                                                                                          flat=True).distinct()]
        form.fields['university_name'].choices = [('', 'Hepsi')] + [(choice, choice) for choice in
                                                                    data_list.values_list('üniversite',
                                                                                          flat=True).distinct()]
        form.fields['major_name'].choices = [('', 'Hepsi')] + [(choice, choice) for choice in
                                                                    data_list.values_list('bolum_adi',
                                                                                          flat=True).distinct()]

        form.fields['year'].choices = [('', 'Hepsi')] + [(choice, choice) for choice in
                                                         data_list.values_list('yil', flat=True).distinct()]
        form.fields['scholarship'].choices = [('', 'Hepsi')] + [(choice, choice) for choice in
                                                                data_list.values_list('burs_türü',
                                                                                      flat=True).distinct()]

        return render(request, 'filters.html', {'form': form})

    if 'export' in request.GET:
        filtered_data = request.session.get('filtered_data', [])
        print("filtered", filtered_data)
        return export_to_excel(filtered_data)

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


def high_school_page(request):
    high_school_data = HighSchoolTable.objects.all().order_by('university')
    paginator = Paginator(high_school_data, 50)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'high_school.html', {'high_school_data': page_obj})
