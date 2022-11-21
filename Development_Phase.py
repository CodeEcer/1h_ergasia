import datetime
import json
from datetime import datetime

all_tweets = []

current_tweet_id = 0
menu_phrase = """Welcome to the tweet editor by George Petakas and his bitches
                        
                        To use this editor please enter one of the following choices
                        
                            c :  create a tweet
                            r (space) tweet's id : read a certain tweet
                            u (space) tweet's id : update a certain tweet
                            $ :  read t     he last tweet
                            - :  read one tweet up from the current tweet
                            + :  read one tweet down from your current tweet
                            = :  Print current tweet ID
                            q :  Quit without save
                            w :  (Over)write file to disk
                            x :  Exit and save
                            """

def getting_input_from_user():
    user_input = input(menu_phrase)
    
    if len(user_input) == 1:
            instruction = user_input
            print("the user selected the choice:",instruction)
            return(instruction,None)        
    else:
        instruction, number = user_input[0], user_input[1:] #assign the 1st char as the instruction and the rest into tweet_id
        tweet_id = int(number) #this parses char to int
        print("the user selected the choice:",instruction , "of the tweet with the id" ,tweet_id)
        return(instruction, tweet_id)
   

def initializing_tweet_list(): #REFACTOOOOR!!!
    all_tweets.append(None) #In order to start using list from index and not messing with the printed indexes
    with open("_tweet_for_code.json", "r") as json_file_read:
        
        for line in json_file_read:
            tweet = json.loads(line) #kathe tweet einai ena dictionary
            
            #logika tha to kano na krataei mono ta pedia pou me endiaferoun.
            all_tweets.append(tweet) #h all_tweet prosorina einai mia lista apo dictionaries, kai to index tou tweet einai to id tou
         

def create_tweet():
  users_text = input("Please enter your text")
  current_time = datetime.now()
  ##new_tweet = {"text" : users_text , "created_at" : current_time.strftime()  }
  print("the user typed" ,users_text , "at" , current_time.strftime("%a %b %d %H:%M:%S %Y"))
  new_tweet = {"text" : users_text , "created_at" : current_time.strftime("%a %b %d %H:%M:%S %Y") }
  all_tweets.append(new_tweet)
  global current_tweet_id
  current_tweet_id = all_tweets.index(new_tweet)
  print(" the current tweet is set to the tweet with id:" ,current_tweet_id)




def read_tweet(id):
    print(all_tweets[id]["text"] , "created at",all_tweets[id]["created_at"] )
    global current_tweet_id
    current_tweet_id = all_tweets.index(all_tweets[id])
    print(" the current tweet is set to the tweet with id:" ,current_tweet_id)

def update_tweet(id):
    current_time = datetime.now()
    new_text = input("Set the updated text")
    all_tweets[id]["text"] = new_text
    all_tweets[id]["created_at"] = current_time.strftime("%a %b %d %H:%M:%S %Y")
    print("you texted :",all_tweets[id]["text"], "at the exact time of : ", all_tweets[id]["created_at"] )
    global current_tweet_id
    current_tweet_id = all_tweets.index(all_tweets[id])
    print(" the current tweet is set to the tweet with id:" ,current_tweet_id) 
    
def delete_tweet(id):

    all_tweets.pop(id)

    
def read_previous_tweet():
    global current_tweet_id
    if current_tweet_id == 1: 
        print("You have reached the bottom end of the tweets")
        
    else:
        current_tweet_id = current_tweet_id -1
        read_tweet(current_tweet_id)
    


def read_next_tweet():
    global current_tweet_id
    if current_tweet_id == len(all_tweets) -1:
        print("You have reached the top end of the tweets")
       
    else:    
        current_tweet_id = current_tweet_id +1
        read_tweet(current_tweet_id)

def save_changes(): #REFACTOOOOOR!!!!!

    with open("_tweet_for_code.json", "w") as json_to_write:
        json_to_write.seek(0)
        for tweet in all_tweets:
            if tweet != None:
                tweet = json.dump(tweet, json_to_write)
                json_to_write.write('\n')
            else: pass
           



def exit_save_changes():
    save_changes()
    exit()
    



def main():

    
    
    

    initializing_tweet_list()
    
    while  True:
        
        

        instruction , tweet_id = getting_input_from_user()    

   
        match instruction :

            case "c": create_tweet()

            case "r": read_tweet(tweet_id)

            case "u": update_tweet(tweet_id)

            case "d": delete_tweet(tweet_id)

            case "$": read_tweet(len(all_tweets)-1) #size is by 1 bigger than the sum of indexes cause it starts with 1. If i make up for the 
            #indexes for the user, i won't have to subtract 1 cause the indexes will start from 1 for the user.

            case "-": read_previous_tweet()

            case "+": read_next_tweet()

            case "=": print(" the current tweet is set to the tweet with id:" ,current_tweet_id) 

            case "q": exit()

            case "w": save_changes()

            case "x": exit_save_changes()


            case _: print("wrong character")          



if __name__ == "__main__":
    main()         
            


