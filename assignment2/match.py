import numpy as np
from typing import List, Tuple
import random

def changeArr(input1):
 
    # Copy input array into newArray
    newArray = input1.copy()
     
    # Sort newArray[] in ascending order
    newArray.sort()
     
    # Dictionary to store the rank of
    # the array element
    ranks = {}
     
    rank = 1
     
    for index in range(len(newArray)):
        element = newArray[index];
     
        # Update rank of element
        if element not in ranks:
            ranks[element] = rank
            rank += 1
         
    # Assign ranks to elements
    for index in range(len(input1)):
        element = input1[index]
        input1[index] = ranks[input1[index]]

def run_matching(scores: List[List], gender_id: List, gender_pref: List) -> List[Tuple]:
    # Edit Ranking
    for i in range(len(scores)):
        changeArr(scores[i])
    # print(gender_pref)
    print(scores)
    
    # Set Gender Preferences for Incompatible Ranking
    for i in range(len(scores)):        
        for j in range(len(scores[i])):
            if scores[i][j] == 0:
                continue
            if gender_pref[i] == "Men" and genders[j] == "Female":
                scores[i][j] = 0
                scores[j][i] = 0
                print(gender_pref[i], genders[j])
            if gender_pref[i] =="Women" and genders[j] == "Male":
                scores[i][j] = 0
                scores[j][i] = 0
            # if Bisexual, can be matched with anyone

    proposed = [[], [], [], [], [], [], [], [], [], [], []]
    # intialize everyone to be free
    unmatched = []
    for i in range(len(scores)):
        unmatched.append(i)
    print(unmatched)
    matched = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    proposers = random.sample(range(0, 10), 5)
    receivers = []
    for i in range(len(scores)):
        if i not in proposers:
            receivers.append(i)
    print("proposers", proposers, "receivers", receivers)
  
    
    while any(item in proposers for item in unmatched):
        proposee = proposers.pop()
        receiver = 0
        for j in range(len(scores[proposee])):
            if scores[proposee][j] != 0 and j not in proposed[proposee]: 
                receiver = j
                break
        
        # if w if free, match m and w
        if receiver not in matched:
            matched[proposee] = receiver
            matched[receiver] = proposee
            unmatched.remove(receiver)
            continue
        # if w prefers m to her current match m' then free up m'
        elif scores[receiver][matched[receiver]] > scores[receiver][proposee]:
            matched[receiver] = proposee
            matched[proposee] = receiver
            # free up current match
            matched[matched[receiver]] = 0
            unmatched.append(matched[receiver])
            unmatched.remove(proposee)
        else:
            # w rejects m
            proposed[proposee].append(receiver)
            proposers.append(proposee)
    
    print(matched)
    for i in range(len(matched)):
        if matched[i] == 10:
            continue
        else:
            print(i, matched[i], genders[i], gender_pref[i], genders[matched[i]], gender_pref[matched[i]])
    
    print(gender[ ])

    
    
                
        



    """
    TODO: Implement Gale-Shapley stable matching!
    :param scores: raw N x N matrix of compatibility scores. Use this to derive a preference rankings.
    :param gender_id: list of N gender identities (Male, Female, Non-binary) corresponding to each user
    :param gender_pref: list of N gender preferences (Men, Women, Bisexual) corresponding to each user
    :return: `matches`, a List of (Proposer, Acceptor) Tuples representing monogamous matches

    Some Guiding Questions/Hints:
        - This is not the standard Men proposing & Women receiving scheme Gale-Shapley is introduced as
        - Instead, to account for various gender identity/preference combinations, it would be better to choose a random half of users to act as "Men" (proposers) and the other half as "Women" (receivers)
            - From there, you can construct your two preferences lists (as seen in the canonical Gale-Shapley algorithm; one for each half of users
        - Before doing so, it is worth addressing incompatible gender identity/preference combinations (e.g. gay men should not be matched with straight men).
            - One easy way of doing this is setting the scores of such combinations to be 0
            - Think carefully of all the various (Proposer-Preference:Receiver-Gender) combinations and whether they make sense as a match
        - How will you keep track of the Proposers who get "freed" up from matches?
        - We know that Receivers never become unmatched in the algorithm.
            - What data structure can you use to take advantage of this fact when forming your matches?
        - This is by no means an exhaustive list, feel free to reach out to us for more help!
    """
    # gay men should not be matched with straight men, set the scores of such combinations to be 0
    # choose a random half of users to act as proposers
    # proposers = random half
    # other half of users
    # receivers = 
    matches = [()]
    return matches

if __name__ == "__main__":
    raw_scores = np.loadtxt('raw_scores.txt').tolist()
    genders = []
    with open('genders.txt', 'r') as file:
        for line in file:
            curr = line[:-1]
            genders.append(curr)

    gender_preferences = []
    with open('gender_preferences.txt', 'r') as file:
        for line in file:
            curr = line[:-1]
            gender_preferences.append(curr)

    gs_matches = run_matching(raw_scores, genders, gender_preferences)
