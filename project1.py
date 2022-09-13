#word puzzle game
def puzzle_game():
    score=0
    round=5
    list1=['TREACHE','OAERELANP','RENEG','CYROTNU','KABRE','RAEHTF']
    list2=['TEACHER','AEROPLANE','GREEN','COUNTRY','BREAK','FATHER']
    #ans = input("your answer")
    while(round):
        print("\nArrange the letters to form a valid word ")
        print(list1[round])
        ans = input("")
        if(ans==list2[round]):
            print("\ncorrect")
            score=score+1
        else:
            print("\nwrong") 
            score=score-1   

        
        round=round-1
    print("\nNet Score is",score)    

puzzle_game()        