from repositories import PromotionsRepository


class PromotionsService(object):

    """docstring for PromotionssService"""

    __promotion_repository = PromotionsRepository.PromotionsRepository()

    def create(self, insert_data):
        return self.__promotion_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__promotion_repository.update(id, update_data)

    def getPromotions(self):
        return self.__promotion_repository.all()

    def getPromotion(self, id):
        return self.__promotion_repository.find(id)

    def filter(self,filters):
        return self.__promotion_repository.filter(filters)

