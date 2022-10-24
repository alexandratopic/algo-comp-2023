#!usr/bin/env python3
import json
import sys
import os

INPUT_FILE = 'testdata.json' # Constant variables are usually in ALL CAPS

class User:
    def __init__(self, name, gender, preferences, grad_year, responses):
        self.name = name
        self.gender = gender
        self.preferences = preferences
        self.grad_year = grad_year
        self.responses = responses

# find how rare similar response is
def rarity(question, response):
    if not os.path.exists(INPUT_FILE):
            print('Input file not found')
            sys.exit(0)

    score_count = [0, 0, 0, 0, 0, 0]
    total = 0
    with open(INPUT_FILE) as json_file:
        data = json.load(json_file)
        for user_obj in data['users']:
            # print(question)
            
            # print(user_obj['responses'][17])
            score_count[(user_obj['responses'][question])] += 1  
            total += 1 
    # print(score_count)
    # print(score_count[response] / total)
    rarity = 1 - (score_count[response] / total)
    # print(rarity)
    return rarity
  
            
    
    # score_count = [0, 0, 0, 0, 0]
    # for question 
    #     score_count[]




# Takes in two user objects and outputs a float denoting compatibility
def compute_score(user1, user2):
    # we want the output to be normalized in range [0, 1]
    # zi = (xi – min(x)) / (max(x) – min(x))

    # scores in range 0 - 60 then normalized to range [0,1]
    score = 0


    # Preferences Compatibility, range [0, 20]
    if user1.gender in user2.preferences:
        score += 10
        print(user1.preferences)
    if user2.gender in user1.preferences:
        score += 10
    
    # Grad Year Compatibility, range [0, 20]
    diff = max(user1.grad_year, user2.grad_year) - min(user1.grad_year, user2.grad_year)
    diff = (diff / 4) * 20
    diff = 20 - diff
    score += diff

    # Responses, range [0, 20]
    # if the response is rare and the same weight it more
    # weight the response based on how common it is 
    # more common response = weighted less


    # z = (score - )
    res_questions = 0
    for i in range(len(user1.responses)):
        if user1.responses[i] == user2.responses[i]:
            scale = rarity(i, user1.responses[i])
            print("scale", scale)
            res_questions += scale
    score += res_questions
        # print(i)

        # rarity(i, user1.responses[i])
    # for i in range(len(user1.responses)):
    #     print(i)
    #     # If they have the same response, weight the same response based on rarity 
    #     if user1.responses[i] == user2.responses[i]:
    #         rarity(i, user1.responses[i])
    # YOUR CODE HERE
    score =  score / 60
    return score


if __name__ == '__main__':
    # Make sure input file is valid
    if not os.path.exists(INPUT_FILE):
        print('Input file not found')
        sys.exit(0)

    users = []
    with open(INPUT_FILE) as json_file:
        data = json.load(json_file)
        for user_obj in data['users']:
            new_user = User(user_obj['name'], user_obj['gender'],
                            user_obj['preferences'], user_obj['gradYear'],
                            user_obj['responses'])
            users.append(new_user)

    for i in range(len(users)-1):
        for j in range(i+1, len(users)):
            user1 = users[i]
            user2 = users[j]
            score = compute_score(user1, user2)
            print('Compatibility between {} and {}: {}'.format(user1.name, user2.name, score))
