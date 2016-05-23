
from providers.models import Provider
from contracts.repositories import AbstractBaseRepository
from .BaseRepository import BaseRepository 

class ProvidersRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Provider)

    def find_ruc(self, find_ruc):
    	try:
    		provider_ruc = Provider.objects.get(ruc=find_ruc)
    	except Provider.DoesNotExist:
    		return None
    	return provider_ruc