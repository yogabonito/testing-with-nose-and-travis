import math


MARATHON = 42.195
HALF_MARATHON = MARATHON / 2


def kmph_to_minpkm(kmph):
	minpkm = 1 / (kmph/60)
	minutes = math.floor(minpkm)
	seconds = round(60*(minpkm-minutes),1)
	return {"minutes": minutes, "seconds": seconds}

def minpkm_to_kmph(minutes, seconds=None):
	if seconds is not None:
		minutes += seconds/60
	kmph = 1 / (minutes/60)
	return kmph

def pace_needed_kmph(km, hours=0, minutes=0, seconds=0, dec_precision=2):
	seconds = seconds + 60 * (minutes + 60 * hours)
	hours = seconds / (60**2)
	#print(round(km / hours, dec_precision))
	return round(km / hours, dec_precision)

def pace_needed_minpkm(km, hours=0, minutes=0, seconds=0):
	seconds = seconds + 60 * (minutes + 60 * hours)
	spkm = seconds / km
	minpkm = spkm / 60
	minutes = math.floor(minpkm)
	seconds = round(60*(minpkm-minutes),1)
	return {"minutes":minutes, "seconds":seconds}

def time_needed_at_pace_minpkm(minutes, seconds):
	pass # todo

def time_needed_at_pace_kmph(kmph):
	pass # todo

# todo: use NamedTuple instead of dict with "minutes" and "seconds".

# todo: refactor: minpkm vs kmph as keywordarg with default minpkm OR EVEN BETTER
# generic function called e.g. pace_needed with keywordarg and a very simple
# if-else calling the existing specialised functions.


