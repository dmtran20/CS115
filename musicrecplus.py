'''
Dylan Tran
I pledge my honor that I have abided by the Stevens Honor System.
'''

def greeting():
    Name = input('What is your name? ')


def menu():
    print('e - Enter preferences')
    print('r - Get recommendations')
    print('p - Show most popular artists')
    print('h - How popular is the most popular')
    print('m - Which user has the most likes')
    print('q - Save and quit')
    choice= input('Enter a letter to choose an option: ')
    if choice=='e':
        print ('1')
    if choice=='r':
        print ('2')
    if choice=='p':
        print ('3')
    if choice=='h':
        print ('4')
    if choice=='m':
        print ('5')
    if choice=='q':
        print ('6')
    else:
       menu()

def loadUsers(fileName):
    ''' Reads in a file of stored users' preferences
        stored in the file 'fileName'. Returns a dictionary containing a mapping
        of user names to a list preferred artists
    '''
    file = open(fileName, 'r')
    userDict = {}
    for line in file:
        # Read and parse a single line
        [Name, bands] = line.strip().split(":")
        bandList = bands.split(",")
        bandList.sort()
        userDict[Name] = bandList
    file.close()
    return userDict

def Enter_preferences():
    preferences=input('Enter an artist that you like ( Enter to finish )' )
    if preferences=='':
        return 1

 
def getPreferences(Name, userMap):
    ''' Returns a list of the uesr's preferred artists.

        If the system already knows about the user,
        it gets the preferences out of the userMap
        dictionary and then asks the user if she has
        additional preferences.  If the user is new,
        it simply asks the user for her preferences. '''
    newPref = ""
    if Name in userMap:
        prefs = userMap[Name]
        print("I see that you have used the system before.")
        print("Your music preferences include:")
        for artist in prefs:
            print(artist)
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newPref = input("to see your recommendations: ")
    else:
        prefs = []
        print("I see that you are a new user.")
        print("Please enter the name of an artist or band")
        newPref = input("that you like: " )
        
    while newPref != "":
        prefs.append(newPref.strip().title())
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newPref = input("to see your recommendations: ")
        
    # Always keep the lists in sorted order for ease of
    # comparison
    prefs.sort()
    return prefs


def Get_recommendations():
    pass

def popular_artists():
    pass

def most_popular():
    pass

def most_likes():
    pass

def save_quit():
    pass

#save_and_quit(dictionary,filename,user,preferences):


'''def main():
    greeting()
    menu()
    

if __name__ == "__main__": main()'''

