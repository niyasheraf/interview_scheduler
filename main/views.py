from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from main.models import TimeSlots


# Create your views here.

@csrf_exempt
def register(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        from_time = request.POST.get('from_time')
        to_time = request.POST.get('to_time')
        from_time = datetime.strptime(from_time, "%d-%m-%Y %H:%M").timestamp()
        to_time = datetime.strptime(to_time, "%d-%m-%Y %H:%M").timestamp()
        if to_time < from_time:
            return JsonResponse({"status": "failed", "error": "invalid slot"})
        TimeSlots.objects.get_or_create(user_id=user_id, from_stamp=from_time, to_stamp=to_time)
        return JsonResponse({"status": "success"})


def time_slots(request):
    if request.method == 'GET':
        interviewer_id = request.GET.get('interviewer_id')
        candidate_id = request.GET.get('candidate_id')
        duration = request.GET.get('duration')

        if duration:
            duration = 3600.0 * float(duration)
        else:
            duration = 3600.0

        interviewer_slots = TimeSlots.objects.filter(user_id=interviewer_id).values_list('from_stamp', 'to_stamp')
        candidate_slots = TimeSlots.objects.filter(user_id=candidate_id).values_list('from_stamp', 'to_stamp')
        matching_slots = list(map(stamp_to_date, find_matching(interviewer_slots, candidate_slots, duration)))
        return JsonResponse(matching_slots, safe=False)


def stamp_to_date(stamp_range):
    return datetime.fromtimestamp(stamp_range[0]), datetime.fromtimestamp(stamp_range[1])


def find_matching(interviewer_stamps, candidate_stamps, duration):
    for interviewer_slot in interviewer_stamps:
        for candidate_slot in candidate_stamps:
            from_time = max(interviewer_slot[0], candidate_slot[0])
            to_time = min(interviewer_slot[1], candidate_slot[1])
            if to_time - from_time >= duration:
                yield from_time, to_time
