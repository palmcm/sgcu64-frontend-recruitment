# Get string that show in segment
def get_segment(is_show,display_segment):
    if is_show:
        return display_segment
    return " " * len(display_segment)

# Get display for any segment
def get_display(segments):
    display = ["","",""]
    display[0] += " " 
    display[1] += get_segment(1 in segments,"|")
    display[2] += get_segment(2 in segments,"|")
    display[0] += get_segment(3 in segments,"__")
    display[1] += get_segment(4 in segments,"__")
    display[2] += get_segment(5 in segments,"__")
    display[0] += " "
    display[1] += get_segment(6 in segments,"|")
    display[2] += get_segment(7 in segments,"|")
    return display

'''
     3__
1-->|4__|<--6
2-->|5__|<--7
'''
#number to 7 segment
num_to_seg = {
    '_': {5},
    '1': {6, 7},
    '2': {2, 3, 4, 5, 6},
    '3': {3, 4, 5, 6, 7},
    '4': {1, 4, 6, 7},
    '5': {1, 3, 4, 5, 7},
    '6': {1, 2, 3, 4, 5, 7},
    '7': {3, 6, 7},
    '8': {1, 2, 3, 4, 5, 6, 7},
    '9': {1, 3, 4, 5, 6, 7},
    '0': {1, 2, 3, 5, 6, 7}
}

#Concat display together 
def concat_display(display,concat_display):
    for i in range(len(display)):
        display[i] += concat_display[i]
    return display

#Check if time is valid and return __:__:__ if not valid
def get_validtime(time):
    timelist = time.split(':')
    if len(timelist) == 3:
        if 0 <= int(timelist[1]) <= 59 and 0 <= int(timelist[2]) <= 59:
            return time
    return "__:__:__"

#Get display for input time
def get_timedisplay(time):
    validtime = get_validtime(time)
    display = ["", "", ""]
    for d in validtime:
        if d == ":":
            concat_display(display, [" ", ".", "."])
        else:
            concat_display(display, get_display(num_to_seg[d]))
        concat_display(display, [" ", " ", " "])
    return display

#Print display list
def print_display(display):
    for line in display:
        print(line)


#Get input and display
time = input("input: ")
print_display(get_timedisplay(time))
