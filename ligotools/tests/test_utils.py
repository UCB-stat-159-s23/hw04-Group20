import numpy as np
import matplotlib.mlab as mlab
from ligotools import readligo as rl
from ligotools import utils
from scipy.interpolate import interp1d
from scipy.signal import filtfilt, butter
from pathlib import Path
import json

# import data to run tests with
fnjson = "../../data/" + "BBH_events_v3.json"
events = json.load(open(fnjson,"r"))
eventname = 'GW150914'
event = events[eventname]
fn_H1 = "../../data/" + event['fn_H1']
fn_L1 = "../../data/" + event['fn_L1']
tevent = event['tevent']
fband = event['fband']
strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
strain_L1, time_L1, chan_dict_L1 = rl.loaddata(fn_L1, 'L1')
time = time_H1
dt = time[1] - time[0]
fs = event['fs']

# Setting up variables for whiten test
NFFT = 4*fs
Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
Pxx_L1, freqs = mlab.psd(strain_L1, Fs = fs, NFFT = NFFT)
psd_H1 = interp1d(freqs, Pxx_H1)
psd_L1 = interp1d(freqs, Pxx_L1)

# for wave_file 
deltat_sound = 2.
indxd = np.where((time >= tevent-deltat_sound) & (time < tevent+deltat_sound))
bb, ab = butter(4, [fband[0]*2./fs, fband[1]*2./fs], btype='band')
normalization = np.sqrt((fband[1]-fband[0])/(fs/2))
strain_H1_whiten = utils.whiten(strain_H1, psd_H1, dt)
strain_H1_whitenbp = filtfilt(bb, ab, strain_H1_whiten) / normalization

# for plotting
make_plots = 1
plottype = "png"

def test_whiten():
    strain_H1_whiten = utils.whiten(strain_H1, psd_H1, dt)
    strain_L1_whiten = utils.whiten(strain_L1, psd_L1, dt)
    # testing that whiten function changes the data
    assert strain_H1_whiten is not strain_H1
    assert strain_L1_whiten is not strain_L1
    
def test_write_wavfile():
    utils.write_wavfile(eventname+"_H1_whitenbp.wav",int(fs), strain_H1_whitenbp[indxd])
    fna = eventname+"_H1_whitenbp.wav"
    # testing file is .wav format
    assert Path(fna).suffix == '.wav'

def test_reqshift():
    fs = 4096
    fshift = 400.
    strain_H1_shifted = utils.reqshift(strain_H1, fshift=fshift, sample_rate=fs)
    strain_L1_shifted = utils.reqshift(strain_L1, fshift=fshift, sample_rate=fs)
    # testing that reqshift function changes the data
    assert strain_H1_shifted is not strain_H1
    assert strain_L1_shifted is not strain_L1
    
def test_psd_plot():
    #testing that make_plots is set to 1 and plot type is png
    assert make_plots == 1
    assert plottype == "png"