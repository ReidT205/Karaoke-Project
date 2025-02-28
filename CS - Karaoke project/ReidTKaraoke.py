import pygame
import time
import threading
from tkinter import Tk, Text, END

Lyrics = [
    {"lyric": "You", "time": 22},
    {"lyric": "can", "time": 22.1},
    {"lyric": "feel", "time": 22.5},
    {"lyric": "it", "time": 22.8},
    {"lyric": "in", "time": 23.4},
    {"lyric": "the", "time": 23.7},
    {"lyric": "streets", "time": 24},

    {"lyric": "On", "time": 24.6},
    {"lyric": "a", "time": 24.8},
    {"lyric": "day", "time": 25.2},
    {"lyric": "like", "time": 25.4},
    {"lyric": "this,", "time": 25.9},
    {"lyric": "the", "time": 26.2},
    {"lyric": "heat", "time": 26.6},

    {"lyric": "It", "time": 26.9},
    {"lyric": "feel", "time": 27.2},
    {"lyric": "like", "time": 27.7},
    {"lyric": "summer", "time": 28},

    {"lyric": "I", "time": 32.6},
    {"lyric": "feel", "time": 33.1},
    {"lyric": "like", "time": 33.4},
    {"lyric": "summer", "time": 33.7},

    {"lyric": "I", "time": 38.3},
    {"lyric": "feel", "time": 38.4},
    {"lyric": "like", "time": 38.8},
    {"lyric": "summer", "time": 39.2},

    {"lyric": "You", "time": 44.4},
    {"lyric": "can", "time": 44.6},
    {"lyric": "feel", "time": 45},
    {"lyric": "it", "time": 45.3},
    {"lyric": "in", "time": 45.9},
    {"lyric": "the", "time": 46.1},
    {"lyric": "streets", "time": 46.4},

    {"lyric": "On", "time": 47.5},
    {"lyric": "a", "time": 47.6},
    {"lyric": "day", "time": 48},
    {"lyric": "like", "time": 48.4},
    {"lyric": "this,", "time": 48.7},
    {"lyric": "the", "time": 49.1},
    {"lyric": "heat", "time": 49.5},

    {"lyric": "I", "time": 50.1},
    {"lyric": "feel", "time": 50.5},
    {"lyric": "like", "time": 50.9},
    {"lyric": "summer", "time": 51.2},

    {"lyric": "She", "time": 54.5},
    {"lyric": "feel", "time": 55},
    {"lyric": "like", "time": 55.3},
    {"lyric": "summer", "time": 55.7},

    {"lyric": "This", "time": 60.8},
    {"lyric": "feel", "time": 61},
    {"lyric": "like", "time": 61.5},
    {"lyric": "summer", "time": 61.6},

    {"lyric": "I", "time": 65.7},
    {"lyric": "feel", "time": 65.9},
    {"lyric": "like", "time": 66.2},
    {"lyric": "summer", "time": 66.4},
    
    {"lyric": "Seven", "time": 66.9},
    {"lyric": "billion", "time": 68.1},
    {"lyric": "souls", "time": 68.6},
    {"lyric": "that", "time": 69.9},
    {"lyric": "move", "time": 70.3},
    {"lyric": "around", "time": 70.7},
    {"lyric": "the", "time": 71.3},
    {"lyric": "sun", "time": 71.7},

    {"lyric": "Rolling", "time": 73.3},
    {"lyric": "faster,", "time": 74.35},
    {"lyric": "fast", "time": 75.4},
    {"lyric": "and", "time": 76.2},
    {"lyric": "not", "time": 76.7},
    {"lyric": "a", "time": 77.1},
    {"lyric": "chance", "time": 77.4},
    {"lyric": "to", "time": 77.6},
    {"lyric": "slow", "time": 78},
    {"lyric": "down", "time": 78.7},

    {"lyric": "Slow", "time": 83.65},
    {"lyric": "down", "time": 84.4},

    {"lyric": "Men", "time": 89.45},
    {"lyric": "who", "time": 90.3},
    {"lyric": "made", "time": 90.8},
    {"lyric": "machines", "time": 91.55},
    {"lyric": "that", "time": 92.5},
    {"lyric": "want", "time": 92.9},
    {"lyric": "what", "time": 93.3},
    {"lyric": "they", "time": 93.6},
    {"lyric": "decide", "time": 94.1},

    {"lyric": "Parents", "time": 95.45},
    {"lyric": "tryna", "time": 96.4},
    {"lyric": "tell", "time": 97.5},
    {"lyric": "their", "time": 98.4},
    {"lyric": "children", "time": 98.8},
    {"lyric": "please", "time": 99.35},
    {"lyric": "slow", "time": 100.1},
    {"lyric": "down", "time": 100.8},

    {"lyric": "Slow", "time": 104.8},
    {"lyric": "down", "time": 105.7},

    {"lyric": "I", "time": 109.8},
    {"lyric": "know", "time": 110.1},

    {"lyric": "Oh,", "time": 111.55},
    {"lyric": "I", "time": 114.2},
    {"lyric": "know", "time": 114.6},
    {"lyric": "you", "time": 113.6},
    {"lyric": "know", "time": 115.35},
    {"lyric": "that", "time": 115.8},
    {"lyric": "pain", "time": 116.05},

    {"lyric": "I'm", "time": 117.3},
    {"lyric": "hopin'", "time": 117.75},
    {"lyric": "that", "time": 118.6},
    {"lyric": "this", "time": 118.75},
    {"lyric": "world", "time": 119.2},
    {"lyric": "will", "time": 119.6},
    {"lyric": "change", "time": 119.8},

    {"lyric": "But", "time": 124.1},
    {"lyric": "it", "time": 124.6},
    {"lyric": "just", "time": 124.85},
    {"lyric": "seems", "time": 125.2},
    {"lyric": "the", "time": 125.4},
    {"lyric": "same", "time": 125.75},

    {"lyric": "(It", "time": 127.2},
    {"lyric": "feels", "time": 127.5},
    {"lyric": "like", "time": 127.8},
    {"lyric": "the", "time": 128.2},
    {"lyric": "same)", "time": 128.6},

    {"lyric": "You", "time": 130.95},
    {"lyric": "can", "time": 131.2},
    {"lyric": "feel", "time": 131.5},
    {"lyric": "it", "time": 131.9},
    {"lyric": "in", "time": 132.2},
    {"lyric": "the", "time": 132.8},
    {"lyric": "streets", "time": 133},

    {"lyric": "On", "time": 133.8},
    {"lyric": "a", "time": 134},
    {"lyric": "day", "time": 134.3},
    {"lyric": "like", "time": 134.6},
    {"lyric": "this,", "time": 135},
    {"lyric": "the", "time": 135.4},
    {"lyric": "heat", "time": 135.8},

    {"lyric": "It", "time": 136.2},
    {"lyric": "feels", "time": 136.6},
    {"lyric": "like", "time": 136.9},
    {"lyric": "summer", "time": 137.1},

    {"lyric": "(I", "time": 139.1},
    {"lyric": "feel", "time": 139.4},
    {"lyric": "like", "time": 139.9},
    {"lyric": "summer)", "time": 140.1},

    {"lyric": "I", "time": 142},
    {"lyric": "feel", "time": 142.3},
    {"lyric": "like", "time": 142.8},
    {"lyric": "summer", "time": 143.1},

    {"lyric": "(I", "time": 145.1},
    {"lyric": "feel", "time": 145.3},
    {"lyric": "like", "time": 145.7},
    {"lyric": "summer)", "time": 145.9},

    {"lyric": "I", "time": 145.8},
    {"lyric": "feel", "time": 146.2},
    {"lyric": "like", "time": 146.5},
    {"lyric": "summer", "time": 146.8},

    {"lyric": "Every", "time": 148.3},
    {"lyric": "day", "time": 149.3},
    {"lyric": "gets", "time": 150},
    {"lyric": "hotter", "time": 150.6},
    {"lyric": "than", "time": 151.4},
    {"lyric": "the", "time": 151.8},
    {"lyric": "one", "time": 152.5},
    {"lyric": "before", "time": 152.8},

    {"lyric": "Running", "time": 153.9},
    {"lyric": "out", "time": 155},
    {"lyric": "of", "time": 156},
    {"lyric": "water,", "time": 156.5},
    {"lyric": "it's", "time": 157.1},
    {"lyric": "about", "time": 157.8},
    {"lyric": "to", "time": 158.3},
    {"lyric": "go", "time": 158.6},
    {"lyric": "down", "time": 159.3},

    {"lyric": "Go", "time": 161.4},
    {"lyric": "down", "time": 162.2},

    {"lyric": "Air", "time": 171.3},
    {"lyric": "that", "time": 172},
    {"lyric": "kill", "time": 172.3},
    {"lyric": "the", "time": 173.1},
    {"lyric": "bees", "time": 173.5},
    {"lyric": "that", "time": 174.2},
    {"lyric": "we", "time": 174.6},
    {"lyric": "depend", "time": 175.3},
    {"lyric": "upon", "time": 175.9},

    {"lyric": "Birds", "time": 179.1},
    {"lyric": "were", "time": 179.8},
    {"lyric": "made", "time": 180.2},
    {"lyric": "for", "time": 180.9},
    {"lyric": "singing", "time": 181.1},

    {"lyric": "Waking", "time": 182.3},
    {"lyric": "up", "time": 183},
    {"lyric": "to", "time": 183.3},
    {"lyric": "no", "time": 183.7},
    {"lyric": "sound", "time": 184.3},

    {"lyric": "No", "time": 177.5},
    {"lyric": "sound", "time": 178},

    {"lyric": "I", "time": 189.3},
    {"lyric": "know", "time": 189.5},

    {"lyric": "Oh,", "time": 191.2},
    {"lyric": "I", "time": 194},
    {"lyric": "know", "time": 194.3},
    {"lyric": "you", "time": 194.7},
    {"lyric": "know", "time": 195},
    {"lyric": "my", "time": 195.3},
    {"lyric": "pain", "time": 195.5},

    {"lyric": "I'm", "time": 198.9},
    {"lyric": "hopin'", "time": 199.4},
    {"lyric": "that", "time": 200.1},
    {"lyric": "this", "time": 200.5},
    {"lyric": "world", "time": 200.8},
    {"lyric": "will", "time": 201.2},
    {"lyric": "change", "time": 201.5},
    {"lyric": "(yeah)", "time": 204.2},

    {"lyric": "But", "time": 205.7},
    {"lyric": "it", "time": 206},
    {"lyric": "just", "time": 206.3},
    {"lyric": "seems", "time": 206.4},
    {"lyric": "the", "time": 207},
    {"lyric": "same", "time": 207.2},

    {"lyric": "I", "time": 212.5},
    {"lyric": "know", "time": 212.7},

    {"lyric": "Oh,", "time": 214.3},
    {"lyric": "I", "time": 217.9},
    {"lyric": "hope", "time": 218.3},
    {"lyric": "we", "time": 218.6},
    {"lyric": "change", "time": 218.8},

    {"lyric": "I", "time": 221.1},
    {"lyric": "really", "time": 221.6},
    {"lyric": "thought", "time": 222.1},
    {"lyric": "this", "time": 222.6},
    {"lyric": "world", "time": 223},
    {"lyric": "could", "time": 223.4},
    {"lyric": "change", "time": 223.6},

    {"lyric": "But", "time": 228.6},
    {"lyric": "it", "time": 228.9},
    {"lyric": "seems", "time": 229.1},
    {"lyric": "like", "time": 229.7},
    {"lyric": "the", "time": 230},
    {"lyric": "same", "time": 230.3},

    {"lyric": "I", "time": 235.7},
    {"lyric": "know", "time": 235.8},

    {"lyric": "Oh,", "time": 237.5},
    {"lyric": "my", "time": 230.3},
    {"lyric": "mind", "time": 230.6},
    {"lyric": "is", "time": 230.9},
    {"lyric": "still", "time": 231.3},
    {"lyric": "the", "time": 231.7},
    {"lyric": "same", "time": 231.9},

    {"lyric": "I'm", "time": 235.2},
    {"lyric": "hoping", "time": 235.5},
    {"lyric": "that", "time": 236.3},
    {"lyric": "this", "time": 236.8},
    {"lyric": "world", "time": 237.1},
    {"lyric": "will", "time": 237.5},
    {"lyric": "change", "time": 237.8},

    {"lyric": "But", "time": 241.8},
    {"lyric": "it", "time": 242.2},
    {"lyric": "just", "time": 242.5},
    {"lyric": "seems", "time": 242.7},
    {"lyric": "the", "time": 243.2},
    {"lyric": "same", "time": 243.7},

    {"lyric": "I", "time": 248.8},
    {"lyric": "know", "time": 248.9},

    {"lyric": "Oh,", "time": 250.7},
    {"lyric": "I", "time": 254},
    {"lyric": "hope", "time": 254.5},
    {"lyric": "we", "time": 254.7},
    {"lyric": "change", "time": 255.1},

]

# Combine the lyrics into lines for display
lines = [
    " ".join([lyric["lyric"] for lyric in Lyrics[:7]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[7:14]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[14:18]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[18:22]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[22:26]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[26:33]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[33:40]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[40:44]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[44:48]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[48:52]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[52:56]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[56:64]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[64:74]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[74:76]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[76:85]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[85:93]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[93:95]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[95:97]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[97:104]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[104:111]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[111:117]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[117:122]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[122:129]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[129:136]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[136:140]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[140:144]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[144:148]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[148:152]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[152:156]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[156:164]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[164:173]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[173:175]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[175:184]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[184:189]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[189:194]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[194:196]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[196:198]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[198:205]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[205:213]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[213:219]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[219:221]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[221:226]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[226:233]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[233:239]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[239:241]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[241:248]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[248:255]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[255:261]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[261:263]]),
    " ".join([lyric["lyric"] for lyric in Lyrics[263:]])
]

# Track positions of each word in the combined lines
positions = []
for line in lines:
    pos = []
    start = 0
    for word in line.split():
        start = line.find(word, start)
        pos.append((start, start + len(word)))
        start += len(word)
    positions.append(pos)

# Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load("CGFLS.mp3")
pygame.mixer.music.play()

# Initialize tkinter
root = Tk()
root.configure(bg='black')

# Create and configure text widget
text_widget = Text(root, wrap='word', font=('Helvetica', 16), bg='darkblue', fg='white')
text_widget.pack(expand=1, fill='both')

# Insert combined lyrics into text widget with blank lines in between
for line in lines:
    text_widget.insert(END, line + "\n\n")

# Function to update text color based on time
def update_text_color():
    for i in range(0, 2560):
        currentTime = i / 10
        for index, lyric in enumerate(Lyrics):
            if abs(lyric["time"] - currentTime) < 0.1:
                if index < 7:
                    line_index = 1
                    word_index = Lyrics[:7].index(lyric)
                    start_index = f"{line_index}.0 + {positions[0][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[0][word_index][1]}c"
                elif index < 14:
                    line_index = 3  # Adjusted for blank line
                    word_index = Lyrics[7:14].index(lyric)
                    start_index = f"{line_index}.0 + {positions[1][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[1][word_index][1]}c"
                elif index < 18:
                    line_index = 5  # Adjusted for blank lines
                    word_index = Lyrics[14:18].index(lyric)
                    start_index = f"{line_index}.0 + {positions[2][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[2][word_index][1]}c"
                elif index < 22:
                    line_index = 7  # Adjusted for blank lines
                    word_index = Lyrics[18:22].index(lyric)
                    start_index = f"{line_index}.0 + {positions[3][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[3][word_index][1]}c"
                elif index < 26:
                    line_index = 9  # Adjusted for blank lines
                    word_index = Lyrics[22:26].index(lyric)
                    start_index = f"{line_index}.0 + {positions[4][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[4][word_index][1]}c"
                elif index < 33:
                    line_index = 11  # Adjusted for blank lines
                    word_index = Lyrics[26:33].index(lyric)
                    start_index = f"{line_index}.0 + {positions[5][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[5][word_index][1]}c"
                elif index < 40:
                    line_index = 13  # Adjusted for blank lines
                    word_index = Lyrics[33:40].index(lyric)
                    start_index = f"{line_index}.0 + {positions[6][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[6][word_index][1]}c"
                elif index < 44:
                    line_index = 15  # Adjusted for blank lines
                    word_index = Lyrics[40:44].index(lyric)
                    start_index = f"{line_index}.0 + {positions[7][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[7][word_index][1]}c"
                elif index < 48:
                    line_index = 17  # Adjusted for blank lines
                    word_index = Lyrics[44:48].index(lyric)
                    start_index = f"{line_index}.0 + {positions[8][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[8][word_index][1]}c"
                elif index < 52:
                    line_index = 19  # Adjusted for blank lines
                    word_index = Lyrics[48:52].index(lyric)
                    start_index = f"{line_index}.0 + {positions[9][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[9][word_index][1]}c"
                elif index < 56:
                    line_index = 21  # Adjusted for blank lines
                    word_index = Lyrics[52:56].index(lyric)
                    start_index = f"{line_index}.0 + {positions[10][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[10][word_index][1]}c"
                elif index < 64:
                    line_index = 23  # Adjusted for blank lines
                    word_index = Lyrics[56:64].index(lyric)
                    start_index = f"{line_index}.0 + {positions[11][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[11][word_index][1]}c"
                elif index < 74:
                    line_index = 25  # Adjusted for blank lines
                    word_index = Lyrics[64:74].index(lyric)
                    start_index = f"{line_index}.0 + {positions[12][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[12][word_index][1]}c"
                elif index < 76:
                    line_index = 27  # Adjusted for blank lines
                    word_index = Lyrics[74:76].index(lyric)
                    start_index = f"{line_index}.0 + {positions[13][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[13][word_index][1]}c"
                elif index < 85:
                    line_index = 29  # Adjusted for blank lines
                    word_index = Lyrics[76:85].index(lyric)
                    start_index = f"{line_index}.0 + {positions[14][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[14][word_index][1]}c"
                elif index < 93:
                    line_index = 31  # Adjusted for blank lines
                    word_index = Lyrics[85:93].index(lyric)
                    start_index = f"{line_index}.0 + {positions[15][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[15][word_index][1]}c"
                elif index < 95:
                    line_index = 33  # Adjusted for blank lines
                    word_index = Lyrics[93:95].index(lyric)
                    start_index = f"{line_index}.0 + {positions[16][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[16][word_index][1]}c"
                elif index < 97:
                    line_index = 35  # Adjusted for blank lines
                    word_index = Lyrics[95:97].index(lyric)
                    start_index = f"{line_index}.0 + {positions[17][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[17][word_index][1]}c"
                elif index < 104:
                    line_index = 37  # Adjusted for blank lines
                    word_index = Lyrics[97:104].index(lyric)
                    start_index = f"{line_index}.0 + {positions[18][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[18][word_index][1]}c"
                elif index < 111:
                    line_index = 39  # Adjusted for blank lines
                    word_index = Lyrics[104:111].index(lyric)
                    start_index = f"{line_index}.0 + {positions[19][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[19][word_index][1]}c"
                elif index < 117:
                    line_index = 41  # Adjusted for blank lines
                    word_index = Lyrics[111:117].index(lyric)
                    start_index = f"{line_index}.0 + {positions[20][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[20][word_index][1]}c"
                elif index < 122:
                    line_index = 43  # Adjusted for blank lines
                    word_index = Lyrics[117:122].index(lyric)
                    start_index = f"{line_index}.0 + {positions[21][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[21][word_index][1]}c"
                elif index < 129:
                    line_index = 45  # Adjusted for blank lines
                    word_index = Lyrics[122:129].index(lyric)
                    start_index = f"{line_index}.0 + {positions[22][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[22][word_index][1]}c"
                elif index < 136:
                    line_index = 47  # Adjusted for blank lines
                    word_index = Lyrics[129:136].index(lyric)
                    start_index = f"{line_index}.0 + {positions[23][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[23][word_index][1]}c"
                elif index < 140:
                    line_index = 49  # Adjusted for blank lines
                    word_index = Lyrics[136:140].index(lyric)
                    start_index = f"{line_index}.0 + {positions[24][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[24][word_index][1]}c"
                elif index < 144:
                    line_index = 51  # Adjusted for blank lines
                    word_index = Lyrics[140:144].index(lyric)
                    start_index = f"{line_index}.0 + {positions[25][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[25][word_index][1]}c"
                elif index < 148:
                    line_index = 53  # Adjusted for blank lines
                    word_index = Lyrics[144:148].index(lyric)
                    start_index = f"{line_index}.0 + {positions[26][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[26][word_index][1]}c"
                elif index < 152:
                    line_index = 55  # Adjusted for blank lines
                    word_index = Lyrics[148:152].index(lyric)
                    start_index = f"{line_index}.0 + {positions[27][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[27][word_index][1]}c"
                elif index < 156:
                    line_index = 57  # Adjusted for blank lines
                    word_index = Lyrics[152:156].index(lyric)
                    start_index = f"{line_index}.0 + {positions[28][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[28][word_index][1]}c"
                elif index < 164:
                    line_index = 59  # Adjusted for blank lines
                    word_index = Lyrics[156:164].index(lyric)
                    start_index = f"{line_index}.0 + {positions[29][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[29][word_index][1]}c"
                elif index < 173:
                    line_index = 61  # Adjusted for blank lines
                    word_index = Lyrics[164:173].index(lyric)
                    start_index = f"{line_index}.0 + {positions[30][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[30][word_index][1]}c"
                elif index < 175:
                    line_index = 63  # Adjusted for blank lines
                    word_index = Lyrics[173:175].index(lyric)
                    start_index = f"{line_index}.0 + {positions[31][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[31][word_index][1]}c"
                elif index < 184:
                    line_index = 65  # Adjusted for blank lines
                    word_index = Lyrics[175:184].index(lyric)
                    start_index = f"{line_index}.0 + {positions[32][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[32][word_index][1]}c"
                elif index < 189:
                    line_index = 67  # Adjusted for blank lines
                    word_index = Lyrics[184:189].index(lyric)
                    start_index = f"{line_index}.0 + {positions[33][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[33][word_index][1]}c"
                elif index < 194:
                    line_index = 69  # Adjusted for blank lines
                    word_index = Lyrics[189:194].index(lyric)
                    start_index = f"{line_index}.0 + {positions[34][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[34][word_index][1]}c"
                elif index < 196:
                    line_index = 71  # Adjusted for blank lines
                    word_index = Lyrics[194:196].index(lyric)
                    start_index = f"{line_index}.0 + {positions[35][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[35][word_index][1]}c"
                elif index < 198:
                    line_index = 73  # Adjusted for blank lines
                    word_index = Lyrics[196:198].index(lyric)
                    start_index = f"{line_index}.0 + {positions[36][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[36][word_index][1]}c"
                elif index < 205:
                    line_index = 75  # Adjusted for blank lines
                    word_index = Lyrics[198:205].index(lyric)
                    start_index = f"{line_index}.0 + {positions[37][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[37][word_index][1]}c"
                elif index < 213:
                    line_index = 77  # Adjusted for blank lines
                    word_index = Lyrics[205:213].index(lyric)
                    start_index = f"{line_index}.0 + {positions[38][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[38][word_index][1]}c"
                elif index < 219:
                    line_index = 79  # Adjusted for blank lines
                    word_index = Lyrics[213:219].index(lyric)
                    start_index = f"{line_index}.0 + {positions[39][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[39][word_index][1]}c"
                elif index < 221:
                    line_index = 81  # Adjusted for blank lines
                    word_index = Lyrics[219:221].index(lyric)
                    start_index = f"{line_index}.0 + {positions[40][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[40][word_index][1]}c"
                elif index < 226:
                    line_index = 83  # Adjusted for blank lines
                    word_index = Lyrics[221:226].index(lyric)
                    start_index = f"{line_index}.0 + {positions[41][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[41][word_index][1]}c"
                elif index < 233:
                    line_index = 85  # Adjusted for blank lines
                    word_index = Lyrics[226:233].index(lyric)
                    start_index = f"{line_index}.0 + {positions[42][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[42][word_index][1]}c"
                elif index < 239:
                    line_index = 87  # Adjusted for blank lines
                    word_index = Lyrics[233:239].index(lyric)
                    start_index = f"{line_index}.0 + {positions[43][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[43][word_index][1]}c"
                elif index < 241:
                    line_index = 89  # Adjusted for blank lines
                    word_index = Lyrics[239:241].index(lyric)
                    start_index = f"{line_index}.0 + {positions[44][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[44][word_index][1]}c"
                elif index < 248:
                    line_index = 91  # Adjusted for blank lines
                    word_index = Lyrics[241:248].index(lyric)
                    start_index = f"{line_index}.0 + {positions[45][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[46][word_index][1]}c"
                elif index < 255:
                    line_index = 93  # Adjusted for blank lines
                    word_index = Lyrics[248:255].index(lyric)
                    start_index = f"{line_index}.0 + {positions[47][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[47][word_index][1]}c"
                elif index < 261:
                    line_index = 95  # Adjusted for blank lines
                    word_index = Lyrics[255:261].index(lyric)
                    start_index = f"{line_index}.0 + {positions[48][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[48][word_index][1]}c"
                elif index < 263:
                    line_index = 97  # Adjusted for blank lines
                    word_index = Lyrics[261:263].index(lyric)
                    start_index = f"{line_index}.0 + {positions[49][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[49][word_index][1]}c"
                else:
                    line_index = 99  # Adjusted for blank lines
                    word_index = Lyrics[263:].index(lyric)
                    start_index = f"{line_index}.0 + {positions[50][word_index][0]}c"
                    end_index = f"{line_index}.0 + {positions[50][word_index][1]}c"
                text_widget.tag_add(f"highlight{index}", start_index, end_index)
                text_widget.tag_config(f"highlight{index}", foreground="red")
                break
        time.sleep(0.1)

# Start the threading for updating text color
threading.Thread(target=update_text_color).start()

# Run the tkinter main loop
root.mainloop()