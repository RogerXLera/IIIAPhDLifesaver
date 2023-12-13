"""
Roger Lera
2023/01/07
"""
import os
import datetime as dt
import pandas as pd
import numpy as np
import csv

def month_name(month):
    months = ['January','February','March','April','May','June','July',
              'August','September','October','November','December']
    return months[month-1]


class Event:
    """
    This class stores the information about the events.
    """

    def __init__(self,id_,name,description,date,url=None):
        self.id = id_
        self.name = name
        self.description = description
        self.date = date #datetime object
        self.url = url
        self.documents = []
        

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.id

    def print_date(self):
        month = month_name(self.date.month)
        return f"{self.date.day} of {month} of {self.date.year} at {self.date.hour}:{self.date.minute}"

class Document:
    """
    This class stores the information about the material
    """
    def __init__(self,id_,name,description,dir_,event):
        self.id = id_
        self.name = name
        self.description = description
        self.dir = dir_
        self.event = event
        

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.id

                 