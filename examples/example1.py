import os
import numpy as np
from datetime import datetime
from dateutil.tz import tzlocal
import pynwb
from pynwb import NWBFile, NWBHDF5IO, get_manager, ProcessingModule
from pynwb.core import DynamicTable, DynamicTableRegion, VectorData
from pynwb.misc import DecompositionSeries

manager = get_manager()

# Creates file 1
nwb = NWBFile(session_description='session', identifier='1', session_start_time=datetime.now(tzlocal()))

# data: (ndarray) dims: num_times * num_channels * num_bands
Xp = np.zeros((1000,10,3))

# Spectral band power
# bands: (DynamicTable) frequency bands that signal was decomposed into
band_param_0V = VectorData(name='filter_param_0',
                  description='frequencies for bandpass filters',
                  data=np.array([1.,2.,3.]))
band_param_1V = VectorData(name='filter_param_1',
                  description='frequencies for bandpass filters',
                  data=np.array([1.,2.,3.]))
bandsTable = DynamicTable(name='bands',
                          description='Series of filters used for Hilbert transform.',
                          columns=[band_param_0V,band_param_1V],
                          colnames=['filter_param_0','filter_param_1'])
decs = DecompositionSeries(name='DecompositionSeries',
                           data=Xp,
                           description='Analytic amplitude estimated with Hilbert transform.',
                           metric='amplitude',
                           unit='V',
                           bands=bandsTable,
                           #source_timeseries=lfp
                           rate=1.)

ecephys_module = ProcessingModule(name='ecephys',
                                  description='Extracellular electrophysiology data.')
nwb.add_processing_module(ecephys_module)
ecephys_module.add_data_interface(decs)

with NWBHDF5IO('file_1.nwb', mode='w', manager=manager) as io:
    io.write(nwb)
