from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from services.EntryService import EntryService
from services.MemberService import MembersService
from services.GuestService import GuestService
from services.AffiliateService import AffiliateService
from datetime import datetime

@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['GET'])
def index(request):


    entry_service = EntryService()

    entries = entry_service.getEntries()

    context = {
        'entries' : entries,
    }

    return render(request, 'Admin/Guests/index_entries.html', context) 


@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['GET'])
def create_index(request):

    context = {
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Guests/new_guests_members.html', context)


@login_required
@permission_required('dummy.permission_admin', login_url='login:ini')
@require_http_methods(['POST'])
def insert(request):

    insert_data = {}

    type = request.POST['type']

    #busco al responsable

    filter_data = {}

    member_service = MembersService()

    filter_data["document_number"] = request.POST['doc_member']

    filter_data["state"] = 1

    member = member_service.filter(filter_data)

    insert_data["member"] = member[0]

    #1 para miembro, 2 para afiliado, 3 para invitado, 0 para nuevo invitado
    if(type == '2'):

        affiliate_service = AffiliateService()

        filter_data = {}

        filter_data["document_number"] = request.POST['dni']

        filter_data["state"] = 1

        affiliate = affiliate_service.filter(filter_data)

        insert_data["affiliate"] = affiliate[0]

    elif(type == '3'):

        guest_service = GuestsService()

        filter_data = {}

        filter_data["dni"] = request.POST['dni']

        guest = guest_service.filter(filter_data)

        insert_data["guest"] = guest[0]

    elif(type == '0'):

        print("entre aca")

        insert_guest = {}

        insert_guest["name"] = request.POST['names']

        insert_guest["surname"] = request.POST['surnames']

        insert_guest["dni"] = request.POST['dni']

        insert_guest["status"] = 1

        guest_service = GuestService()

        guest = guest_service.create(insert_guest)

        insert_data["guest"] = guest

    insert_data["initialDate"] = datetime.strptime(request.POST['initialDate'], '%m/%d/%Y')

    insert_data["finalDate"] = datetime.strptime(request.POST['finalDate'], '%m/%d/%Y')

    entry_service = EntryService()

    entry_service.create(insert_data)

    return HttpResponseRedirect(reverse('entry:index'))
