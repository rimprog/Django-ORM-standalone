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

    for not_leaved_visit in not_leaved_visits:
        visit_entered_at_local_time = timezone.localtime(not_leaved_visit.entered_at)
        print(not_leaved_visit.passcard.owner_name)
        print('Зашёл в хранилище, время по Москве:\n{}\nНаходится в хранилище:\n{}\n\n'.format(visit_entered_at_local_time, not_leaved_visit.format_duration()))

    passcard = Passcard.objects.all()[0]
    all_passcard_visits = Visit.objects.filter(passcard=passcard)
    # print(passcard)
    # print(all_passcard_visits)
    # print(len(all_passcard_visits))
    print(all_passcard_visits[0])
    print(all_passcard_visits[0].is_visit_long(minutes=20))
    strange_visits = []
    for visit in Visit.objects.all():
        if visit.is_visit_long():
            strange_visits.append(visit)
    print(len(strange_visits))
