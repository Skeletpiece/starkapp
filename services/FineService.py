from repositories import FineRepository

class FineService(object):

    """docstring for FineService"""

    __fine_repository = FineRepository.FineRepository()

    def create(self, insert_data):
        return self.__fine_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__fine_repository.update(id, update_data)

    def delete(self, id):
        return self.__fine_repository.delete(id)

    def getFines(self):
        return self.__fine_repository.all()
