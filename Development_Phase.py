import json
#jekinao me lista apo dictionaries oste kathe index ths listas na einai to id tou tweet.
    ##sto refactor tha prospathisoume na ginei me tuple gia pio grhgora. 


menu_phrase = """Welcome to the tweet editor by George Petakas and his bitches
                        
                        To use this editor please enter one of the following choices
                        
                            c :  create a tweet
                            r (space) tweet's id : read a certain tweet
                            u (space) tweet's id : update a certain tweet
                            $ : read the last tweet
                            - :  read one tweet up from the current tweet
                            + :  read one tweet down from your current tweet
                            = :  Print current tweet ID
                            q :  quit without save
                            w :  Yoloss
                            x :  exit and save
                            """

def main():
    
    ##while True:
        menu_selector = input(menu_phrase)
       
        for c in menu_selector.split():
            try : 
                id = (int(c))
            except ValueError:
                pass
    
print(id)
            
        


       

       








if __name__ == "__main__":
    main()

