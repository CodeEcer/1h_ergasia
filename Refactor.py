import datetime
import json
from datetime import datetime

new_tweets = []
updated_tweets = []

new_tweets_ids = []
deleted_tweets_ids = []
updated_tweets_ids = []
NUMBER_OF_TWEETS = 0
CURRENT_TWEET_ID = 0

menu_phrase = """Welcome to the tweet editor by George Petakas and his bitches

                        To use this editor please enter one of the following choices

                            c :  create a tweet
                            r (space) tweet's id : read a certain tweet
                            u (space) tweet's id : update a certain tweet
                            $ :  read the last tweet
                            - :  read one tweet up from the current tweet
                            + :  read one tweet down from your current tweet
                            = :  Print current tweet ID
                            q :  Quit without save
                            w :  (Over)write file to disk
                            x :  Exit and save
                            """
option_menu = "Enter your option (enter h for help): "


def getting_input_from_user():
    user_input = input(option_menu)

    if len(user_input) == 1:
        instruction = user_input
        print("the user selected the choice:", instruction)
        return (instruction, None)
    else:
        instruction, number = user_input[0], user_input[
                                             1:]  # assign the 1st char as the instruction and the rest into tweet_id
        tweet_id = int(number)  # this parses char to int
        print("the user selected the choice:", instruction, "of the tweet with the id", tweet_id)
        return (instruction, tweet_id)

# Reads the lines of tweets in the json
def initializing_tweet_list():
    global NUMBER_OF_TWEETS
    global CURRENT_TWEET_ID
    with open("tweetdhead300000.json", "r") as json_file_read:
        for i in json_file_read:
            NUMBER_OF_TWEETS += 1
        CURRENT_TWEET_ID = NUMBER_OF_TWEETS - 1

def create_tweet():
    global NUMBER_OF_TWEETS

    users_text = input("Please enter your text: ")
    current_time = datetime.now()

    print("the user typed", users_text, "at", current_time.strftime("%a %b %d %H:%M:%S %Y"))
    new_tweet = {"text": users_text, "created_at": current_time.strftime("%a %b %d %H:%M:%S %Y")}

    new_tweets.append(new_tweet)
    new_tweets_ids.append(NUMBER_OF_TWEETS)

    global CURRENT_TWEET_ID
    CURRENT_TWEET_ID = NUMBER_OF_TWEETS
    NUMBER_OF_TWEETS += 1
    print(" the current tweet is set to the tweet with id:", CURRENT_TWEET_ID)
    print(new_tweets_ids)


def read_tweet(id):
    global CURRENT_TWEET_ID

    if id in new_tweets_ids:
        print(new_tweets[NUMBER_OF_TWEETS - id - 1]["text"], " created at: ", new_tweets[NUMBER_OF_TWEETS - id - 1]["created_at"])
        CURRENT_TWEET_ID = id
    elif id in updated_tweets_ids:
        print(updated_tweets_ids.index(id))
        print(updated_tweets[updated_tweets_ids.index(id)]["text"], " created at: ", updated_tweets[updated_tweets_ids.index(id)]["created_at"])

    elif id in deleted_tweets_ids:
        print("The ID does not correspond to any tweet")
    else:
        with open("tweetdhead300000.json", "r") as json_file_read:
            json_file_read.seek(0)
            tweet = []
            for i in range(id - 1):
                json_file_read.readline()
            tweet = json.loads(json_file_read.readline())
            print(tweet["text"], " created at: ", tweet["created_at"])
        CURRENT_TWEET_ID = id

def update_tweet(id):
    global CURRENT_TWEET_ID

    current_time = datetime.now()
    new_text = input("Set the updated text")

    if id in new_tweets_ids:
        index = NUMBER_OF_TWEETS - id - 1
        new_tweets[index]["text"] = new_text
        new_tweets[index]["created_at"] = current_time.strftime("%a %b %d %H:%M:%S %Y")

        print("you texted :", new_tweets[index]["text"], "at the exact time of : ", new_tweets[index]["created_at"])
        CURRENT_TWEET_ID = id

    elif id in updated_tweets_ids:
        updated_tweets[updated_tweets_ids.index(id)]["text"] = new_text
        updated_tweets[updated_tweets_ids.index(id)]["created_at"] = current_time.strftime("%a %b %d %H:%M:%S %Y")

        print("you texted :", updated_tweets[id]["text"], "at the exact time of : ", updated_tweets[id]["created_at"])
        CURRENT_TWEET_ID = id

    elif id < NUMBER_OF_TWEETS:
        with open("tweetdhead300000.json", "r") as json_file:
            json_file.seek(0)
            for i in range(id):
                json_file.readline()

            tweet = json.loads(json_file.readline())
            tweet["text"] = new_text
            tweet["created_at"] = current_time.strftime("%a %b %d %H:%M:%S %Y")

            updated_tweets.append(tweet)
            updated_tweets_ids.append(id)
        CURRENT_TWEET_ID = id

    else:
        print("The id does not exist")


def delete_tweet(id):
    deleted_tweets_ids.append(id)


def read_previous_tweet():
    global CURRENT_TWEET_ID
    if CURRENT_TWEET_ID == 1:
        print("You have reached the bottom end of the tweets")

    else:
        CURRENT_TWEET_ID = CURRENT_TWEET_ID - 1
        read_tweet(CURRENT_TWEET_ID)


def read_next_tweet():
    global CURRENT_TWEET_ID
    if CURRENT_TWEET_ID is (NUMBER_OF_TWEETS - 1):
        print("You have reached the top end of the tweets")

    else:
        CURRENT_TWEET_ID = CURRENT_TWEET_ID + 1
        read_tweet(CURRENT_TWEET_ID)


def save_changes():

    with open("tweetdhead300000.json", "r+") as json_to_write:
        buffer = []
        for line in json_to_write:
            tweet = json.loads(line)
            buffer.append(tweet)
        json_to_write.seek(0)

        for id_w in range(NUMBER_OF_TWEETS):
            if id_w in deleted_tweets_ids:
                continue
            elif id_w in updated_tweets_ids:
                json.dump(updated_tweets[updated_tweets_ids.index(id_w)], json_to_write)
            elif id_w in new_tweets_ids:
                json.dump(new_tweets[new_tweets_ids.index(id_w)], json_to_write)
            else:
                json.dump(buffer[id_w], json_to_write)







def exit_save_changes():
    save_changes()
    exit()


def main():
    initializing_tweet_list()

    while True:

        instruction, tweet_id = getting_input_from_user()

        if instruction == "c":
            create_tweet()

        elif instruction == "r":
            read_tweet(tweet_id)

        elif instruction == "u":
            update_tweet(tweet_id)

        elif instruction == "d":
            delete_tweet(tweet_id)

        elif instruction == "$":
            read_tweet(NUMBER_OF_TWEETS - 1)  # size is by 1 bigger than the sum of indexes cause it starts with 1. If i make up for the
            # indexes for the user, i won't have to subtract 1 cause the indexes will start from 1 for the user.

        elif instruction == "-":
            read_previous_tweet()

        elif instruction == "+":
            read_next_tweet()

        elif instruction == "=":
            print(" the current tweet is set to the tweet with id:", CURRENT_TWEET_ID)

        elif instruction == "h":
            print(menu_phrase)

        elif instruction == "q":
            exit()

        elif instruction == "w":
            save_changes()

        elif instruction == "x":
            exit_save_changes()
        else:
            print("wrong character")


if __name__ == "__main__":
    main()
