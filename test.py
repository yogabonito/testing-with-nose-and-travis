from mara import *

def test_kmph_to_minpkm():
	assert(kmph_to_minpkm(10) == {"minutes": 6, "seconds": 0})
	assert(kmph_to_minpkm(12.5) == {"minutes": 4, "seconds": 48})

def test_minpkm_to_kmph():
	assert(minpkm_to_kmph(6)==10)
	assert(minpkm_to_kmph(4,48)==12.5)

def test_pace_needed_minpkm():
	assert(pace_needed_minpkm(MARATHON, 4) == {"minutes":5, "seconds":41.3})
	assert(pace_needed_minpkm(MARATHON, 3, 30) == {"minutes":4, "seconds":58.6})
	assert(pace_needed_minpkm(HALF_MARATHON, hours=1, minutes=53, seconds=39) ==
		{"minutes":5, "seconds":23.2})
	assert(pace_needed_minpkm(HALF_MARATHON, hours=1, minutes=45)==
		{"minutes":4, "seconds":58.6})

def test_pace_needed_kmph():
	assert(pace_needed_kmph(10, minutes=30) == 20)
	assert(pace_needed_kmph(HALF_MARATHON, hours=1, minutes=53, seconds=39)==11.14)
	assert(pace_needed_kmph(HALF_MARATHON, hours=1, minutes=45)==12.06)
