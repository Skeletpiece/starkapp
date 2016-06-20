from repositories import FieldReservationRepository
from django.utils import timezone
import datetime, calendar, time,collections

class FieldReservationService(object):

    """docstring for BungalowsService"""

    __field_reservation_repository = FieldReservationRepository.FieldReservationRepository()

    def create(self, insert_data):
        return self.__field_reservation_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__field_reservation_repository.update(id, update_data)

    def delete(self, id):
        return self.__field_reservation_repository.delete(id)

    def getReservations(self):
        return self.__field_reservation_repository.all()

    def filter(self,filters):
        return self.__field_reservation_repository.filter(filters)

    def getDayAvailableHours(self, courts,courtHeadquarterId, courtTypeId, start, end):
        startDate = datetime.datetime.fromtimestamp(start)
        endDate = datetime.datetime.fromtimestamp(end)
        num_days = (endDate - startDate).days + 1

        hours = [12,13,14,15,16,17,18,19,20,21,22]

        days = []


        for delta in range(0,num_days):
            for hour in hours:
                print (startDate + datetime.timedelta(days=delta) +  datetime.timedelta(hours=hour))
                if(startDate + datetime.timedelta(days=delta) +  datetime.timedelta(hours=hour) > datetime.datetime.today()):
                    days.append(startDate + datetime.timedelta(days=delta) + datetime.timedelta(hours=hour))

        reservations = self.getReservations()

        reservations = reservations.filter(reservation_date=startDate)

        if (courtHeadquarterId != -1):

            print("Filter by Headquarter_ID")
            reservations = reservations.filter(headquarter_id=courtHeadquarterId)

        if (courtTypeId != -1):

            print("Filter by court_type_id")
            reservations = reservations.filter(court_type=courtTypeId)


        reservations_list= []

        for r in reservations:
            hours = r.reservation_duration
            while hours < 0:
                reservations_list += r.reservation_hour + datetime.timedelta(hours=hours)
                hours -= 1

        ocurrences = collections.Counter(reservations_list)


        date = [(day,courts.count() - ocurrences[int(day.strftime("%Y%m%d%H%M%S"))]) for day in days]

        url = "create/reserve/?";
        url += "court_type=" + str(courtTypeId) + "&"
        url += "headquarter=" + str(courtHeadquarterId) + "&"

        availableHours = [{
            'title': 'Canchas disponibles' if(day[1] == 0) else "No disponible",
            'start': day[0].strftime("%Y-%m-%dT%H:%M:%S"),
            'end': (day[0]+datetime.timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S"),
            'url': url + "date="+ day[0].strftime("%Y-%m-%dT%H:%M:%S"),
        } for day in date if (day[1] == 0)]

        print(availableHours)

        return availableHours

