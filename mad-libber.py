def main():
    print('Madlib Maker')
    
    
    def printRowRowRowYourBoat(punctuation):
        print('{0}, {0}, {0} your boat, gently down the {1}, {2} '.format(verb, place, punctuation))
    
    place = input('place: ')
    verb = input('verb: ')
    adverb = input('adverb: ')
    verb2 = input('verb2: ')

    
    printRowRowRowYourBoat('.')
    print('{0}, {0}, {0}, {0}.'.format(adverb))
    printRowRowRowYourBoat('!')
    print('life is but a {0}'.format(verb2))

print()
main()

