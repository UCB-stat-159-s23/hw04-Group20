import numpy as np
import matplotlib.mlab as mlab
from ligotools import readligo as rl
from ligotools import utils
from scipy.interpolate import interp1d
import json

# import some data to run tests with
fnjson = "../../data/" + "BBH_events_v3.json"
events = json.load(open(fnjson,"r"))
eventname = 'GW150914'
event = events[eventname]
fn_H1 = "../../data/" + event['fn_H1']
fn_L1 = "../../data/" + event['fn_L1']
strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
strain_L1, time_L1, chan_dict_L1 = rl.loaddata(fn_L1, 'L1')
time = time_H1
dt = time[1] - time[0]
fs = event['fs']

def test_whiten():
    NFFT = 4*fs
    Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
    # Pxx_L1, freqs = mlab.psd(strain_L1, Fs = fs, NFFT = NFFT)
    psd_H1 = interp1d(freqs, Pxx_H1)
    # psd_L1 = interp1d(freqs, Pxx_L1)
    strain_H1_whiten = utils.whiten(strain_H1, psd_H1, dt)
    assert strain_H1_whiten is not strain_H1
    
# def test_write_wavfile():
    

def test_reqshift():
    fs = 4096
    fshift = 400.
    strain_H1_shifted = utils.reqshift(strain_H1, fshift=fshift, sample_rate=fs)
    assert strain_H1_shifted is not strain_H1
    
# def test_psd_plot():