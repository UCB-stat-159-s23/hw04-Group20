from ligotools import readligo as rl
import json
import ligotools

def test_readligo_eventname():
	fnjson = "../../data/" + "BBH_events_v3.json"
	try:
		events = json.load(open(fnjson,"r"))
	except IOError:
		print("Cannot find resource file "+fnjson)
		print("You can download it from https://www.gwosc.org/s/events/"+fnjson)
		print("Quitting.")
		quit()
		
	eventname = 'GW150914'
	event = events[eventname]
	assert event["name"] == eventname

def test_readligo_H1_time_len():
	fnjson = "../../data/" + "BBH_events_v3.json"
	try:
		events = json.load(open(fnjson,"r"))
	except IOError:
		print("Cannot find resource file "+fnjson)
		print("You can download it from https://www.gwosc.org/s/events/"+fnjson)
		print("Quitting.")
		quit()
		
	eventname = 'GW150914'
	event = events[eventname]
	fn_H1 = "../../data/" + event['fn_H1']
	
	try:
		# read in data from H1 and L1, if available:
		strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
	except:
		print("Cannot find data files!")
		print("You can download them from https://www.gwosc.org/s/events/"+eventname)
		print("Quitting.")
		quit()
	
	assert len(time_H1) == 131072
	
def test_readligo_H1_array_len():
	fnjson = "../../data/" + "BBH_events_v3.json"
	try:
		events = json.load(open(fnjson,"r"))
	except IOError:
		print("Cannot find resource file "+fnjson)
		print("You can download it from https://www.gwosc.org/s/events/"+fnjson)
		print("Quitting.")
		quit()
		
	eventname = 'GW150914'
	event = events[eventname]
	fn_H1 = "../../data/" + event['fn_H1']
	
	try:
		# read in data from H1 and L1, if available:
		strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
	except:
		print("Cannot find data files!")
		print("You can download them from https://www.gwosc.org/s/events/"+eventname)
		print("Quitting.")
		quit()
	
	assert len(time_H1) == len(strain_H1)
	
def test_readligo_H1_L1_strain_len():
	fnjson = "../../data/" + "BBH_events_v3.json"
	try:
		events = json.load(open(fnjson,"r"))
	except IOError:
		print("Cannot find resource file "+fnjson)
		print("You can download it from https://www.gwosc.org/s/events/"+fnjson)
		print("Quitting.")
		quit()
		
	eventname = 'GW150914'
	event = events[eventname]
	fn_H1 = "../../data/" + event['fn_H1']
	fn_L1 = "../../data/" + event['fn_L1']
	
	try:
		# read in data from H1 and L1, if available:
		strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
		strain_L1, time_L1, chan_dict_L1 = rl.loaddata(fn_L1, 'L1')
	except:
		print("Cannot find data files!")
		print("You can download them from https://www.gwosc.org/s/events/"+eventname)
		print("Quitting.")
		quit()
	
	assert len(strain_H1) == len(strain_L1)