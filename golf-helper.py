print('Welcome to the Golf Club Helper!',
      '\n Tell me your situation, and I\'ll recommend a Club\n')
 
ball_on_Green = input("Did you hit it in the green (y/n)? ") == 'y'
distance_ball_hit = int(input('How far is the ball form the hole? '))
 
recommended_club = None
 
if ball_on_Green:
    recommended_club = 'Putter'
elif distance_ball_hit >= 200:
    recommended_club = 'Driver'
elif distance_ball_hit >= 140:
    recommended_club = '5-Iron'
elif distance_ball_hit >= 100:
    recommended_club = '9-Iron'
else:
     recommended_club = 'Pitching Wedge'

print('\n I recommend using your {}'.format(recommended_club))