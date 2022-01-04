from findmusic import find_music
from spotify import create_list

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
date_list = [int(i) for i in date.split("-")]
print(date_list)
if date_list[0] > 2021 and date_list[1] > 12 or date_list[2] > 31:
    print("Invalid Date")
else:
    song_names = find_music(date)
    create_list(song_names, date)


