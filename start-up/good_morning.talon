os: windows

--

good morning: 
    user.good_morning()

mike off: sound.set_microphone("None")

key(ctrl-\): sound.set_microphone("System Default")

eyes off: tracking.control_toggle()
    
eyes on: tracking.control_toggle()

make eyes big: tracking.control_zoom_toggle()