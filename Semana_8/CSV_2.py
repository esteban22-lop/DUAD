#CSV_2

import csv

#Tsv = tab separated values
def create_video_game_tsv():
    fieldnames = ['Nombre', 'Genero', 'Desarrollador', 'Clasificacion']
    filename = 'videogames.tsv'
    
    with open (filename, mode='w', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t')
            
            writer.writeheader()
            print(f"File '{filename}' created with header")
            
            #Ask the user how many games will be added
            n = int(input("How many video games you want to add?" ))
            
            #This for will add n video games
            for i in range(n):
                print(f"\nAdding game {i + 1}")
                
                name = input("Name: ")
                genre = input("Genre: ")
                developer = input("Developer: ")
                rating = input("ESRB rating: ")
                
                writer.writerow({
                    'Nombre': name,
                    'Genero': genre,
                    'Desarrollador': developer,
                    'Clasificacion': rating,
                    
                })
    print("All video games were saved successfully. ")
    

if __name__ == "__main__":
    create_video_game_tsv()