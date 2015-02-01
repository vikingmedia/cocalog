from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import RequestContext, loader
from driverslog.models import Trip


def index(request):
    trips = Trip.objects.order_by('-date')[:5]
    return render(request, 'driverslog/index.html')


def trips(request):
    trips = Trip.objects.order_by('-date')[:5]
    template = loader.get_template('driverslog/trips.html')
    context = RequestContext(request, {
        'trips': trips,
    })
    return HttpResponse(template.render(context))


def trip(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    return render(request, 'driverslog/trip.html', {'trip': trip})