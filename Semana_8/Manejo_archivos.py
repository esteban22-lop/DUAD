#Manejo_archivos

#Read song names from the file I created

with open(r"C:\Users\bitan\Desktop\Python_Ejercicios\Manejo_archivos\songs.txt", "r") as input_file:
    songs = [line.strip() for line in input_file]
    

#sort the songs
songs.sort(key=str.lower)

#write the sorted songs to the output file
with open("sorted_songs", "w") as output_file:
    for song in songs:
        output_file.write(song + "\n")
        
print("Song names have been sorted succesfully.")

