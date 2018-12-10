import time
from datetime import datetime, timedelta
from django.core.exceptions import *
from django.contrib.auth.hashers import *

import pytz
# import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
import calendar
from django.conf import settings
from .models import *
import logging
import json

from django.contrib.auth.models import User, Group

def abc():
    a = Category.objects.all()