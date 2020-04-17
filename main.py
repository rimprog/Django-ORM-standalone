import os
import sys
import django

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
