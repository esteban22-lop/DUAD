#csv_1

import csv


def create_video_game_csv():
    #First of all, create the field names 
    fieldnames = ['nombre', 'genero', 'desarrollador', 'clasificacion']
    filename = 'videogames.csv'
    
    # I used newline = '' to prevent extra blank lines
    
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            
            writer.writeheader()
            print(f"File '{filename}' created with header.")
            
            while True:
                print("\nEnter video game info: ")
                name = input("Name: ")
                genre = input("Genre: ")
                developer = input("Developer: ")
                rating = input("ESRB rating: ")
                
                writer.writerow({
                    'nombre': name,
                    'genero': genre,
                    'desarrollador': developer,
                    'clasificacion': rating, 
                    })
                print(f"Added name: {name} ")
                choice = input("Do you want to add more info? (y/n)").lower()
                if choice == "n":
                    break
    except Exception as e:
        print(f"Error: {e}")
        


if __name__ == "__main__":
    create_video_game_csv()