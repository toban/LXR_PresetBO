# LXR_PresetBO
LXR Preset Bulk-operations - python script for manipulating LXR Drumsynth .SND preset files

supports:

- changing midi-layout of all presets in folder to a desired one


usage:

1. place the presets in the folder presets/
2. set the mapping for the drums changing the variable to the midi notes

desired_midi_layout = [34, 37, 56, 38, 27, 41, 46]
(The mapping is from voice 0 - 5 in the same order as the array)

3. run the script python main.py