#!/usr/bin/env python
"""

Usage: script.py [-i input]

Options:
-i input  input file [default: ../data/km3net_jul13_90m_muatm10T1.km3_v5r1.evt]
"""

import docopt
import numpy as np
import sounddevice as sd

from sonification import pentatinic_utils as pt
from sonification import km3net_utils as km3
from sonification import sound_generation as sg

sampling_rate = 48000
pentatonic = pt.get_a_minor_pentatonic_scale_frequencies()
print(pentatonic)

arguments = docopt.docopt(__doc__)
counter = 0

for event in km3.EvtFile(arguments["-i"]):
    sample = []
    counter += 1

    print(counter, "number of hits: ", len(event))
    event.sort_by_time()
    old_time = 0
    for time, pmt_id in zip(event.time_list, event.pmt_id_list):
        if old_time == 0:
            delta_time = 1
        else:
            delta_time = time - old_time
        storey_id = km3.pmt_id_to_storey(pmt_id)
        sample.append(sg.make_sound(pentatonic[storey_id],delta_time/50.))

    if not sample:
        continue
    sample_np = np.concatenate(sample).ravel()
    sd.play(sample_np, sampling_rate)
    status = sd.wait()
