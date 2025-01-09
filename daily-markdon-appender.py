from datetime import datetime

with open('___PATH TO FILE___', 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    
    f.write("- This will get added every day \n")
    
    if datetime.today().weekday() == 0:
        #Monday
        f.write("- Added on Monday \n")
        f.write("- Example \n")
    elif datetime.today().weekday() == 1:
        #Tuesday
        f.write("- Added on Tuesday \n")
        f.write("- Example \n")
    elif datetime.today().weekday() == 2:
        #Wednesday
        f.write("- Added on Wednesday \n")
        f.write("- Example \n")
    elif datetime.today().weekday() == 3:
        #Thursday
        f.write("- Added on Thursday \n")
        f.write("- Example \n")
    elif datetime.today().weekday() == 4:
        #Friday
        f.write("- Added on Friday \n")
        f.write("- Example \n")
    elif datetime.today().weekday() == 5:
        #Saturday
        f.write("- Added on Saturday \n")
        f.write("- Example \n")
    elif datetime.today().weekday() == 6:
        #Sunday
        f.write("- Added on Sunday \n")
        f.write("- Example \n")
    
    f.write("- \n")
        
    f.write(content)
