from mara import *

def test_kmph_to_minpkm():
	assert(kmph_to_minpkm(10) == PaceMinpkm(6, 0))
	assert(kmph_to_minpkm(12.5) == PaceMinpkm(4, 48))

def test_minpkm_to_kmph():
	assert(minpkm_to_kmph(6)==10)
	assert(minpkm_to_kmph(4,48)==12.5)

def test_pace_needed_minpkm():
	assert(pace_needed_minpkm(MARATHON, 4) == PaceMinpkm(5, 41.3))
	assert(pace_needed_minpkm(MARATHON, 3, 30) == PaceMinpkm(4, 58.6))
	assert(pace_needed_minpkm(HALF_MARATHON, hours=1, minutes=53, seconds=39) ==
		PaceMinpkm(5, 23.2))
	assert(pace_needed_minpkm(HALF_MARATHON, hours=1, minutes=45)==
		PaceMinpkm(4, 58.6))

def test_pace_needed_kmph():
	assert(pace_needed_kmph(10, minutes=30) == 20)
	assert(pace_needed_kmph(HALF_MARATHON, hours=1, minutes=53, seconds=39)==11.14)
	assert(pace_needed_kmph(HALF_MARATHON, hours=1, minutes=45)==12.06)
