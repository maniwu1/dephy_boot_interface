# DISTRIBUTION STATEMENT A. Approved for public release. Distribution is unlimited.
#
# This material is based upon work supported by the Under Secretary of Defense for Research and Engineering under Air Force Contract No. FA8702-15-D-0001. 
# Any opinions, findings, conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the 
# Under Secretary of Defense for Research and Engineering.
#
# © 2020 Massachusetts Institute of Technology.
#
# The software/firmware is provided to you on an As-Is basis
#
# Delivered to the U.S. Government with Unlimited Rights, as defined in DFARS Part 252.227-7013 or 7014 (Feb 2014). 
# Notwithstanding any copyright notice, U.S. Government rights in this work are defined by DFARS 252.227-7013 or DFARS 252.227-7014 as detailed above. 
# Use of this work other than as specifically authorized by the U.S. Government may violate any copyrights that exist in this work.
#
# P. Stegall 2020, Modified by M. Wu 2023.

import time 
import numpy as np 

class FixedCollins:
    def __init__(self, user_mass, left_boot, right_boot):
        self.user_mass = user_mass
        self.left_boot = left_boot
        self.right_boot = right_boot
        self.start_time = time.monotonic()	# initialize the time for keeping track of when each trial started, this will be overwritten when the trial starts.
        rspg = 0
        opg = 27.1
        ppg = 52.4
        spg = 62.7
        ot = 2
        npt = .175
		
        self.left_boot.init_collins_profile(mass = self.user_mass, ramp_start_percent_gait = rspg, 
                                            onset_percent_gait = opg, peak_percent_gait = ppg,
                                            stop_percent_gait = spg, onset_torque = ot, normalized_peak_torque = npt)	# initialize the Zhang/Collins profile
        self.right_boot.init_collins_profile(mass = self.user_mass, ramp_start_percent_gait = rspg, 
                                             onset_percent_gait = opg, peak_percent_gait = ppg, 
                                             stop_percent_gait = spg, onset_torque = ot, normalized_peak_torque = npt)	# initialize the Zhang/Collins profile
		
    def check_time(self, duration, restart_trial = False):
        return 0 