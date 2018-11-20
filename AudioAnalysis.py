import librosa

filename = "Ariana Grande - thank u, next (audio).wav"

#Load the song into librosa to analyze
#y stands for the amplitude of the wave form at the sample time t
#sr stands for the sampling rate (or samples per second) 
y, sr = librosa.load(filename)

#Tempo is speed at which a song is played
#Beat frames are little windows of 512 samples, centered on each frame where a beat occurs in a song
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)

#The number prints out are when each beat occurs in the audio file
print("Tempo: %.2f" %tempo)
print("List of beats:")
print(beats)
print("end.")
#Exact time in second
print("In seconds:")
beat_times = librosa.frames_to_time(beats, sr=sr)

print(beat_times)

librosa.output.times_csv("beat_times.csv", beat)
