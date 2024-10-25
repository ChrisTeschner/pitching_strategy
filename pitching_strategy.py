Pitcher_Using = True
while Pitcher_Using: #This is the loop that will make sure multiple pitchers can use the code once one is done
    print("Hello pitcher, I need to know some information on what\ntype of pitcher you are in order to find out what best\npitch for you to use")
    print("At any point in the game that you want to leave, simply type leave.")
    PitchTypeFastball = input('Do you throw a fastball? Yes or No:').title() #gathers information on whether or not the pitcher throws a fastball
    if PitchTypeFastball == ('Leave'):#this line of code breaks the loop and will be present throughout the code where any input statement is present
        break
    PitchTypeChangeup = input('Do you throw a changeup? Yes or No:').title()#gathers information on whether or not the pitcher throws a changeup
    if PitchTypeChangeup == ('Leave'):
        break
    PitchTypeCurveball = input('Do you throw a curveball? Yes or No:').title()#gathers information on whether or not the pitcher throws a curveball
    if PitchTypeCurveball == ('Leave'):
        break
    allPitches = []#My list of pitches
    if PitchTypeFastball == ('Yes'):
        allPitches.append('Fastball')#This adds the fastball to the list if the pitcher says he throws a fastball
    if PitchTypeChangeup == ('Yes'):
        allPitches.append('Changeup')#This adds the changeup to the list if the pitcher says he throws a changeup
    if PitchTypeCurveball == ('Yes'):
        allPitches.append('Curveball')#This adds the curveball to the list if the pitcher says he throws a curveball
    print(f"You throw {allPitches}")#Prints the list
    print("I will now gather information on the current at bat.")
    CountBalls = input('How many balls have you thrown? 1, 2, or 3:')#Gathers information on the balls thrown in the at bat
    if Countballs == ('Leave'):
        break
    CountStrikes = input('How many strikes have you thrown? 1 or 2:')#Gathers information on the strikes thrown in the at bat
    if CountStrikes == ('Leave'):
        break
    Count = []#My list of the at bat's count
    if CountBalls == ('1'):#This adds one ball to the count
        Count.append('1')
    if CountBalls == ('2'):#This adds two balls to the count
        Count.append('2')
    if CountBalls == ('3'):#This adds three balls to the count
        Count.append('3')
    if CountStrikes == ('1'):#This adds one strike to the count
        Count.append('1')
    if CountStrikes == ('2'):#This adds two strikes to the count
        Count.append('2')
    print(f"Your count is {Count}")#Prints the list
    print("I will now gather information on the type of batter.")
    TypeOfBatter = input('Is your batter a Lefty or a Righty?:').title()#This gathers information on the type of hitter in the at bat
    if TypeOfBatter == ('Leave'):
        break
    Batter = []#My list of what type of batter the batter is
    if TypeOfBatter == ('Lefty'):
        Batter.append('Lefty')#This adds a lefty batter to the list
    if TypeOfBatter == ('Righty'):
        Batter.append('Righty')#This adds a righty batter to the list
    print(f"Your batter is a {Batter}")#Prints the list
    def best_pitch(PitchTypeFastball, PitchTypeChangeup, PitchTypeCurveball, CountBalls, CountStrikes, TypeOfBatter):#This is my function that will decide what the best possible pitch to throw is based on certain conditions like what types of pitches the pitcher throws, and what the count of the at bat is
        if PitchTypeFastball == 'Yes' and CountBalls > CountStrikes:
            print('Your best pitch is a fastball')
        if PitchTypeFastball == 'No' and PitchTypeChangeup == 'Yes' and CountBalls > CountStrikes:
            print('Your best pitch is a changeup')
        if PitchTypeFastball == 'No' and PitchTypeChangeup == 'No' and PitchTypeCurveball == 'Yes' and CountBalls > CountStrikes:
            print('Your best pitch is a curveball')
        if PitchTypeFastball == 'No' and PitchTypeChangeup == 'No' and PitchTypeCurveball == 'No':
            print('Go learn how to pitch')
        if PitchTypeFastball == 'Yes' and PitchTypeChangeup == 'No' and PitchTypeCurveball == 'No' and CountBalls < CountStrikes:
            print('Your best pitch is a fastball')
        if PitchTypeFastball == 'No' and PitchTypeChangeup == 'Yes' and PitchTypeCurveball == 'No' and CountBalls < CountStrikes:
            print('Your best pitch is a changeup')
        if PitchTypeFastball == 'No' and PitchTypeChangeup == 'No' and PitchTypeCurveball == 'Yes' and CountBalls < CountStrikes:
            print('Your best pitch is a curveball')
        if PitchTypeCurveball == 'Yes' and CountBalls < CountStrikes:
            print('Your best pitch is a curveball')
        if PitchTypeChangeup == 'Yes' and CountBalls == CountStrikes:
            print('Your best pitch is a changeup')
        if PitchTypeFastball == 'Yes' and PitchTypeChangeup == 'No' and CountBalls == CountStrikes:
            print('Your best pitch is a fastball')
        if PitchTypeFastball == 'No' and PitchTypeChangeup == 'No' and PitchTypeCurveball == 'Yes' and CountBalls == CountStrikes:
            print('Your best pitch is a curveball')
    best_pitch(PitchTypeFastball, PitchTypeChangeup, PitchTypeCurveball, CountBalls, CountStrikes, TypeOfBatter)