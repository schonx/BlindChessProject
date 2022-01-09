# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 11:16:04 2022

@author: felix
"""

import pyaudio
import wave
import pathlib


def record_coord(coord, output_name, counter_record=None):
    
    parent_dir = pathlib.Path(__file__).parent.resolve()
    local_dir = parent_dir / "audio_files" / "coords" / coord
    
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1
    fs = 44100  # Record at 44100 samples per second
    seconds = 2
    filename = "".join([output_name, ".wav"])
    save_path = local_dir / filename
       
    p = pyaudio.PyAudio()  # Create an interface to PortAudio
    
    print("".join(['Recording sample ', str(counter_record)]))
    
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    
    frames = []  # Initialize array to store frames
    
    # Store data in chunks for 2 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    
    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()
    
    print('Finished recording')
    
    # Save the recorded data as a WAV file
    wf = wave.open(str(save_path), 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    
num_records = 10
coord_recorded = "a1"
for i in range(num_records):
    if i<10:
        output_name = "".join([coord_recorded, "_00", str(i+1)])
    elif i > 9 and i < 100:
        output_name = "".join([coord_recorded, "_0", str(i+1)])
    else:
        output_name = "".join([coord_recorded, "_", str(i+1)])
    record_coord(coord_recorded, output_name, i)