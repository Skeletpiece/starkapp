import datetime, calendar, collections
import json
from .forms import EnvReservationForm
from adapters.FormValidator import FormValidator
from django.contrib import messages
from django.template import loader, RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.timezone import utc
from services.EnvironmentService import EnvironmentService
from services.EnvironmentTypeService import EnvironmentTypeService
from services.HeadquarterService import HeadquarterService
from django.views.decorators.http import require_http_methods
from .forms import EnvironmentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from environment.models import EnvironmentReservation

@require_http_methods(['GET'])
def index(request):

    environment_service = EnvironmentService()
    headquarter_service = HeadquarterService()

    headquarters = headquarter_service.getHeadquarters()
    environments = environment_service.getEnvironmentByStatus()

    context = {
        'environments' : environments,
        'headquarters' : headquarters,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Environments/List_Environment.html', context)

@require_http_methods(['GET'])
def create_index(request):

    form = EnvironmentForm()

    environment_service = EnvironmentTypeService()
    type_environment = environment_service.getEnvironment()
    headquarter_service = HeadquarterService()
    headquarters = headquarter_service.getHeadquarters()

    context = {
        'titulo' : 'titulo',
        'type_environment' : type_environment,
        'headquarters' : headquarters,
        'form' : form
    }

    return render(request, 'Admin/Environments/Create_Environment.html', context)

@require_http_methods(['GET'])
def edit_index(request, id):

    environment_service = EnvironmentService()
    environment_type_service = EnvironmentTypeService()
    headquarter_service = HeadquarterService()

    headquarters = headquarter_service.getHeadquarters()
    environments = environment_service.getEnviromentById(id)
    type_environment = environment_type_service.getEnvironment()

    print(id)
    #Falta validación de try except dentro de base repository
    if (environments == None):
        return HttpResponseRedirect(reverse('Environments:index'))

    form = EnvironmentForm(instance=environments)
    context = {
		'id' :id,
        'form' : form,
        'environments' : environments,
        'type_environment' : type_environment,
        'headquarters': headquarters,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Environments/Edit_Environment.html', context)

@require_http_methods(['POST'])
def delete_environment(request):

    edit_data = {}

    id_edit = request.POST['id']

    edit_data["status"] = 0

    environment_service = EnvironmentService()

    environment_service.update(id_edit, edit_data)

    return HttpResponseRedirect(reverse('environment:index'))


@require_http_methods(['POST'])
def create_environment(request):
    if request.POST:
        form = EnvironmentForm(request.POST)
        
        if form.is_valid():
            print("pasa")
            insert_data = {}
            insert_data["name"] = request.POST['name']
            insert_data["capacity"] = request.POST['capacity']
            insert_data["status"] = request.POST['status']
            insert_data["environment_type_id"] = request.POST['environment_type']
            insert_data["headquarter_id"] = request.POST['headquarter']
            insert_data["description"] = request.POST['description']
                
            environment_service = EnvironmentService()

            environment_service.create(insert_data)

            return HttpResponseRedirect(reverse('environment:index'))

        else:

            errors = form.errors.as_data()
            for error in errors:
                print(error)
            context = {'form' : form}
            return render(request, 'Admin/Environments/Create_Environment.html', context)


@require_http_methods(['POST'])
def edit_environment(request, id):
    if request.POST:
        form = EnvironmentForm(request.POST)
        
        if form.is_valid():

            #form.save()

            edit_data = {}
            edit_data["name"] = request.POST['name']
            edit_data["capacity"] = request.POST['capacity']
            edit_data["status"] = request.POST['status']
            edit_data["environment_type_id"] = request.POST['environment_type']
            edit_data["headquarter_id"] = request.POST['headquarter']
            edit_data["description"] = request.POST['description']

            environment_service = EnvironmentService()

            environment_service.update(id, edit_data)

            return HttpResponseRedirect(reverse('environment:index'))
        else:

            errors = form.errors.as_data()
            for error in errors:
                print(error)
            context = {'form' : form}
            return render(request, 'Admin/Environments/Edit_Environment.html', context)

    return HttpResponseRedirect(reverse('environment:index'))


# Metodos para la reserva de ambientes

@require_http_methods(['GET'])
def index_book(request):

    environment_service = EnvironmentService()
    headquarter_service = HeadquarterService()

    headquarters = headquarter_service.getHeadquarters()

    filters      = getReservationFilters(request)
    reservations = environment_service.filterReservations(filters)

    paginator = Paginator(reservations, 10)

    page = request.GET.get('page')

    try:
        reservations = paginator.page(page)

    except PageNotAnInteger:
        reservations = paginator.page(1)

    except EmptyPage:
        reservations = paginator.page(paginator.num_pages)

    context = {
        'reservations' : reservations,
        'headquarters' : headquarters,
        'titulo'       : 'titulo'
    }

    return render(request, 'Admin/Environments/List_Reservations.html', context)

@require_http_methods(['GET'])
def create_reservation(request):

    headquarter_service = HeadquarterService()

    headquarters = headquarter_service.getHeadquarters()

    context = {
        'titulo': 'tittle',
        'headquarters' : headquarters,
    }

    return render(request, 'Admin/Environments/Create_Reservation.html', context)


@require_http_methods(['POST'])
def create_reservation_getEnvs(request):

    environment_service = EnvironmentService()

    environments = environment_service.filter({'headquarter_id' : request.POST.get('headquarter_id')})

    context = RequestContext(request)
    
    context = {
        'environments' : environments,
        'titulo'       : 'titulo'
    }
    
    return render_to_response('Admin/Environments/Create_Reservation_Envs.html', context)


@require_http_methods(['POST'])
def refresh_reservation(request):
    start             = int(request.POST['start'])
    end               = int(request.POST['end'])
    if request.POST.get('environment_id'):
        environment_id    = int(request.POST['environment_id'])
    headquarter_id    = int(request.POST['headquarter_id'])

    availableDays = getMonthAvailableDays(headquarter_id, environment_id, start, end)
    response = {
        'events': availableDays
    }
    return JsonResponse(response)

@require_http_methods(['GET'])
def create_reservation_index(request):

    environment_id = request.GET.get('environment_id')
    headquarter_id = request.GET.get('headquarter_id')
    date = datetime.datetime.fromtimestamp(int(request.GET.get('date')))

    environment_service = EnvironmentService()

    reservation = EnvironmentReservation()
    reservation.environment_id = environment_id
    reservation.start_date = date

    context = {
        'reservation': reservation,
        'durationOptions': [1,2,3,4],
        'titulo': 'titulo'
    }

    return render(request, 'Admin/Environments/Create_Reservation_part2.html', context)


@require_http_methods(['POST'])
def insert_reservation(request):

    start_date = datetime.datetime.strptime(request.POST['start_date'], '%d/%m/%Y')
    end_date   = start_date + datetime.timedelta(days=int(request.POST['num_days']))

    create_new_reservation(request.POST['environment_id'], start_date, end_date, request.POST['price'])

    return HttpResponseRedirect(reverse('environment:create_reservation'))


# Helpers



def create_new_reservation(environment_id, start_date, end_date, price):

    insert_data = {}


    insert_data["status"]         = 0

    insert_data["environment_id"] = environment_id

    insert_data["start_date"]     = start_date
    insert_data["end_date"]       = end_date

    insert_data["price"]          = price

    environment_service = EnvironmentService()

    environment_service.createReservation(insert_data)


def getRefreshReservationFilters(request):

    filters = {}

    if ('env_name' in request) or ('headquarter_id' in request) or ('environment_id' in request):

        environment_service = EnvironmentService()
        data = {}

        if 'env_name' in request:
            data['name__icontains'] = request['env_name']

        if 'headquarter_id' in request:
            data['headquarter_id'] = request['headquarter_id']

        if 'environment_id' in request:
            data['id'] = request['environment_id']

        qry_env = environment_service.filter(data).values_list('id', flat=True)

        if qry_env:
            filters['environment_id__in'] = list(qry_env)
        else:
            filters['environment_id'] = -1  #With this value, the filter will return no values.


    if 'start_date' in request:
        filters['start_date__gte'] = request['start_date']

    if 'end_date'   in request:
        filters['end_date__lte']   = request['end_date']

    return filters


def getMonthAvailableDays(headquarter_id, environment_id, start, end):

    startDate = datetime.datetime.fromtimestamp(start)
    endDate   = datetime.datetime.fromtimestamp(end)
    num_days  = (endDate - startDate).days + 1
    days      = [startDate + datetime.timedelta(days=delta) for delta in range(0, num_days)]

    request = {
        'start_date'     : startDate,
        'end_date'       : endDate,
        'headquarter_id' : headquarter_id,
        'environment_id' : environment_id,
    }

    environment_service = EnvironmentService()
    

    filters      = getRefreshReservationFilters(request)
    reservations = environment_service.filterReservations(filters)

    env_req ={
        'headquarter_id' : headquarter_id,
        'id'             : environment_id,
    }
    environments = environment_service.filter(env_req).values_list('id', flat=True)

    # Get list of reserved environments (day, #reservations)
    # print([(r.bungalow_id,r.bungalow_headquarter.id) for r in reservations])

    reservationList = []
    for r in reservations:
        reservationList += r.getReservationDays()
    ocurrences = collections.Counter(reservationList)

    print(int(startDate.strftime('%Y%m%d')), int(endDate.strftime('%Y%m%d')))
    print(ocurrences)
    print(days)
    # print([(int(day.strftime('%Y%m%d')),environments.count() - ocurrences[int(day.strftime('%Y%m%d'))]) for day in days])

    days = [(day, environments.count() - ocurrences[int(day.strftime('%Y%m%d'))]) for day in days]

    # Compose the url (Worst Approach EVER!)
    url = "create/reserve?";
    url += "environment_id=" + str(environment_id) + "&"
    url += "headquarter_id=" + str(headquarter_id) + "&"
    url += "date="

    return [{'title': str(day[1]) + ' Ambientes Disponibles',
             'start': day[0].isoformat(),
             'url': url + str(int(day[0].timestamp()))
             } for day in days if (day[1] != 0)]


def getReservationFilters(request):


    filters = {}

    if request.GET.get('env_name') or request.GET.get('headquarter_id') or request.GET.get('environment_id'):

        environment_service = EnvironmentService()
        data = {}

        if request.GET.get('env_name'):
            data['name__icontains'] = request.GET.get('env_name')

        if request.GET.get('headquarter_id'):
            data['headquarter_id'] = request.GET.get('headquarter_id')

        if request.GET.get('environment_id'):
            data['id'] = request.GET.get('environment_id')

        qry_env = environment_service.filter(data).values_list('id', flat=True)

        if qry_env:
            filters['environment_id__in'] = list(qry_env)
        else:
            filters['environment_id'] = -1  #With this value, the filter will return no values.

    #Verify date section:
    
    start_date = datetime.datetime.min
    end_date   = datetime.datetime.max

    if request.GET.get('start_date'):
        start_date = datetime.datetime.strptime(request.GET.get('start_date'), "%m/%d/%Y")

    if request.GET.get('end_date'):
        end_date   = datetime.datetime.strptime(request.GET.get('end_date'), "%m/%d/%Y")

    filters['start_date__lte'] = end_date.replace(tzinfo=utc)
    filters['end_date__gte']   = start_date.replace(tzinfo=utc)

    return filters

#Este recibe como parametro un dict.
def getReservationFiltersDict(request):

    filters = {}

    if ('env_name' in request) or ('headquarter_id' in request) or ('environment_id' in request):

        environment_service = EnvironmentService()
        data = {}

        if 'env_name' in request:
            data['name__icontains'] = request['env_name']

        if 'headquarter_id' in request:
            data['headquarter_id'] = request['headquarter_id']

        if 'environment_id' in request:
            data['id'] = request['environment_id']

        qry_env = environment_service.filter(data).values_list('id', flat=True)

        if qry_env:
            filters['environment_id__in'] = list(qry_env)
        else:
            filters['environment_id'] = -1  #With this value, the filter will return no values.

    #Verify date section:
    
    start_date = datetime.min
    end_date   = datetime.max

    if 'start_date' in request:
        start_date = datetime.strptime(request['start_date'], "%m/%d/%Y")

    if 'end_date'   in request:
        end_date   = datetime.strptime(request['end_date'], "%m/%d/%Y")

    filters['start_date__lte'] = end_date
    filters['end_date__gte']   = start_date

    return filters
