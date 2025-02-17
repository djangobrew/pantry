import os
import django

def print_heading():
    header = """
--------------------------------------------------------
    ______      _                __        ____  ______
   / ____/___  (_)________  ____/ /__     / __ \/ ____/
  / __/ / __ \/ / ___/ __ \/ __  / _ \   / / / /___ \  
 / /___/ /_/ / (__  ) /_/ / /_/ /  __/  / /_/ /___/ /  
/_____/ .___/_/____/\____/\__,_/\___/   \____/_____/   
     /_/                                               
--------------------------------------------------------\n"""
    print(header)

if __name__ == '__main__':

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangobrew.settings')
    django.setup()
    
    print_heading()

    from django.conf import settings
    # from ep05.models import Item, Barista, Order
    # from ep05.serializers import ItemSerializer, BaristaSerializer, OrderSerializer
    from ep05.models import *
    from ep05.serializers import *
