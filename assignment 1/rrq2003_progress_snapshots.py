progressbar = '-'
fill_in_character = '▓'
bar_length = 50
total_to_complete = 10000
amount_completed = 8000
percentage = '0%'
percentage_complete = '80%'
bar = ('|' + progressbar*bar_length + '|')
formattedbar = format(bar, '>20s')
formattedpercentage = format(percentage, '>20s')
print('Snapshot 1')
print(formattedbar, formattedpercentage)


print('Snapshot 2')
completebar = format('|' + fill_in_character*int((amount_completed/total_to_complete)*(bar_length)) +   #math to determine how much of bar to fill
    progressbar*int(bar_length-(amount_completed/total_to_complete)*(bar_length)) + '|', '>20s')        #int used bc value is a float initially
formattedpercentage_complete = format(percentage_complete, '>20s')
print(completebar, formattedpercentage_complete)
