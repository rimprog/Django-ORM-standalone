import os
import sys
from datetime import datetime

import django
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard, Visit


if __name__ == "__main__":
    passcards = Passcard.objects.all()
    first_passcard = passcards[2]
    print(first_passcard.owner_name)
    print(first_passcard.passcode)
    print(first_passcard.created_at)
    print(first_passcard.is_active)

    print('Количество пропусков:', Passcard.objects.count())

    active_passcards = Passcard.objects.filter(is_active=True)
    print('Активных пропусков:', len(active_passcards))

    not_leaved_visits = Visit.objects.filter(leaved_at=None)
    print(not_leaved_visits)

    now_time = timezone.localtime(timezone.now())
    for not_leaved_visit in not_leaved_visits:
        visit_entered_at_local_time = timezone.localtime(not_leaved_visit.entered_at)
        time_in_storage = now_time - visit_entered_at_local_time
        formated_time_in_storage = str(time_in_storage).split('.')[0]
        print(not_leaved_visit.passcard.owner_name)
        print('Зашёл в хранилище, время по Москве:\n{}\n\nНаходится в хранилище:\n{}'.format(visit_entered_at_local_time, formated_time_in_storage))
