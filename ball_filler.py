import math

ballsmanufacturedstring = input ("How many bowling balls will be manufactured? ")
ballsmanu = int(ballsmanufacturedstring)

diameterstring = input ("What is the diameter of each ball in inches? ")
diame = float(diameterstring)

corevolumestring = input ("What is the core volume in inches cubed? ")
covolu = int(corevolumestring)

volume_ofa_ball = (4/3) * math.pi * ((diame/2)**3)

filler_per_ball = volume_ofa_ball - covolu

amount_of_filler = ballsmanu * filler_per_ball

print( "You will need", amount_of_filler, "inches cubed of filler."
