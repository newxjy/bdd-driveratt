from debug.debug_pl_surface_new import *
from functions.et_preprocess import *
# test path from 10/17 recording at lab with calibration
path3 = '/home/whitney/Teresa/demos/old/surfaceANDcalibration_3screens'
# test path from 10/25 recording
path = '/home/whitney/Teresa/demos/3screens_1025'
# test path from 11/4 recording
path4 = '/home/whitney/Teresa/demos/2019_11_04/000'
super_best = '/home/whitney/Teresa/demos/super_best'

original = '/media/whitney/New Volume/Teresa/bdd-driveratt/VP1/raw'
# surfaceMap False in et_import for testing purposes
# data = preprocess_et(subject='', datapath=super_best, save=True, eventfunctions=(make_blinks,make_saccades,make_fixations))

# preprocess_et does not take et anymore


test = map_surface(super_best)

print('done!')