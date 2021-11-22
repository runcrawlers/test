from .models import AllData, Search
from datetime import datetime


def add_all_data(encode, insert_date):
    all_data = AllData(encode=encode, insert_date=insert_date)
    all_data.save()


