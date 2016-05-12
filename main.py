from os import listdir
from os.path import isfile, join, splitext

notes = {
0:	'C',
1:	'C#',
2:	'D',
3:	'D#',
4:	'E',
5:	'F',
6:	'F#',
7:	'G',
8:	'G#',
9:	'A',
10:	'A#',
11:	'B',
12:	'C',
13:	'C#',
14:	'D',
15:	'D#',
16:	'E',
17:	'F',
18:	'F#',
19:	'G',
20:	'G#',
21:	'A',
22:	'A#',
23:	'B',
24:	'C',
25:	'C#',
26:	'D',
27:	'D#',
28:	'E',
29:	'F',
30:	'F#',
31:	'G',
32:	'G#',
33:	'A',
34:	'A#',
35:	'B',
36:	'C',
37:	'C#',
38:	'D',
39:	'D#',
40:	'E',
41:	'F',
42:	'F#',
43:	'G',
44:	'G#',
45:	'A',
46:	'A#',
47:	'B',
48:	'C',
49:	'C#',
50:	'D',
51:	'D#',
52:	'E',
53:	'F',
54:	'F#',
55:	'G',
56:	'G#',
57:	'A',
58:	'A#',
59:	'B',
60:	'C',
61:	'C#',
62:	'D',
63:	'D#',
64:	'E',
65:	'F',
66:	'F#',
67:	'G',
68:	'G#',
69:	'A',
70:	'A#',
71:	'B',
72:	'C',
73:	'C#',
74:	'D',
75:	'D#',
76:	'E',
77:	'F',
78:	'F#',
79:	'G',
80:	'G#',
81:	'A',
82:	'A#',
83:	'B',
84:	'C',
85:	'C#',
86:	'D',
87:	'D#',
88:	'E',
89:	'F',
90:	'F#',
91:	'G',
92:	'G#',
93:	'A',
94:	'A#',
95:	'B',
96:	'C',
97:	'C#',
98:	'D',
99:	'D#',
100:	'E',
101:	'F',
102:	'F#',
103:	'G',
104:	'G#',
105:	'A',
106:	'A#',
107:	'B',
108:	'C',
109:	'C#',
110:	'D',
111:	'D#',
112:	'E',
113:	'F',
114:	'F#',
115:	'G',
116:	'G#',
117:	'A',
118:	'A#',
119:	'B',
120:	'C',
121:	'C#',
122:	'D',
123:	'D#',
124:	'E',
125:	'F',
126:	'F#',
127:	'G',
}

def getSize(fileobject):
    fileobject.seek(0,2)
    size = fileobject.tell()
    fileobject.seek(0,0)
    return size

STEREO_1 = 0
STEREO_2 = 1
LEFT_1 = 2
RIGHT_1 = 3
LEFT_2 = 4
RIGHT_2 = 5

# set this to the desired midilayout
desired_midi_layout = [34, 37, 56, 38, 27, 41, 46]
desired_output_setup = [LEFT_1, RIGHT_1, RIGHT_1, RIGHT_1, RIGHT_1, RIGHT_1]

num_midi_channels = 7
num_voices = 6
my_path = './presets'

def bulk_output_setup():

    files = [f for f in listdir(my_path) if isfile(join(my_path, f))]

    for file in files:
        name, ext = splitext(file)

        if ext == '.SND':
            voice_outputs = []
            in_file = open(join(my_path, file), "r+")

            size = getSize(in_file)
            preset_name = in_file.read(8)

            # offset is seven + six bytes from the end
            in_file.seek(size-(num_voices+num_midi_channels))

            # read the outputs
            for i in range(0, num_voices):
                voice_output = in_file.read(1)
                voice_outputs.append(ord(voice_output))

            file_size_string = "%s bytes" % str(size)
            status = "OK"

            if(desired_output_setup != voice_outputs):
                status = "UPDATED"

                # put the pointer at the note-offset
                in_file.seek(size-(num_midi_channels+num_voices))

                for i in range(0, num_voices):
                    desired_output = desired_output_setup[i]
                    in_file.write(chr(desired_output))

            print "%s - %s: %s" % (file,preset_name.rstrip(), status)

            in_file.close()

def bulk_midi_mapping():

    files = [f for f in listdir(my_path) if isfile(join(my_path, f))]

    for file in files:
        name, ext = splitext(file)

        if ext == '.SND':
            voice_notes = []
            in_file = open(join(my_path, file), "r+")

            size = getSize(in_file)
            preset_name = in_file.read(8)

            # offset is seven bytes from the end
            in_file.seek(size-num_midi_channels)

            # read the notes
            for i in range(0, num_midi_channels):
                voice_note = in_file.read(1)
                voice_notes.append(ord(voice_note))

            file_size_string = "%s bytes" % str(size)
            status = "OK"

            if(desired_midi_layout != voice_notes):
                status = "UPDATED"

                # put the pointer at the note-offset
                in_file.seek(size-num_midi_channels)

                for i in range(0, num_midi_channels):
                    desired_note = desired_midi_layout[i]
                    in_file.write(chr(desired_note))

            print "%s - %s: %s" % (file,preset_name.rstrip(), status)

            in_file.close()

bulk_output_setup()




