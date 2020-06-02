#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:22:04 2020

just some trying out... 

Cards: 
    2 - 10 as normal
    11 = Jack
    12 = Queen
    13 = King
    14 = As
        
Straights are not right, needs work
Very unhappy with the output... 

@author: Max
"""
import random as rd



def generate_hand(deck):
    hand = []
    pocket = False
    for n in range(2):
        index = rd.randint(0,len(deck)-1)
        card = deck.pop(index)
        hand.append(card)
    if hand[0][1] == hand[1][1]:
        pocket = True 
    return hand, deck, pocket

def generate_deck():
    deck = []
    number = []
    n_kind =[]
    kinds = ["Hearts", "Diamonds", "clubs", "Spades"]
    for k in kinds:
        for n in range(2,15):
            deck.append([k,n])
            number.append(n)
            n_kind.append(k)
    return deck

#attempt to calculate probabilities, wrong calculations!

def fact(n):
    fact = 1
    for n in range(1,n+1):
        fact = fact*n
    return fact

# nCr = (n!)/(r!(n-r)!)
def nCr(n,r):
    x = n - r
    return fact(n)/(fact(r)*fact(x))

def flush_straight(hand):
    if hand[1][0] == hand[1][0] and abs(hand[0][1] - hand[1][1]) < 5:
        prob_1 = prob_1 = (1/50)*(1/49)*(1/48)
        ncr = nCr(5,3)
    else:
        prob_1 = prob_1 = (1/50)*(1/49)*(1/48)*(1/47)
        ncr = nCr(5,4)
    total_prob = prob_1 * ncr
    return total_prob

def four_of_kind(hand, pocket): 
    if pocket == True:
        prob_1 = (2/50)*(1/49) 
        ncr = nCr(5,2)
    else:
        prob_1 = (3/50) * (2/49) * (1/48)
        ncr = nCr(5,3)
    total_prob = prob_1 * ncr
    return total_prob    

def full_house(hand, pocket):
    if pocket == True:
        prob_1 = (2/50)*(48/49)*(3/48)
        ncr = nCr(5,3)
    else:
        prob_1 = (3/50) * (2/49) * (3/48)
        ncr = nCr(5,3)
    total_prob = prob_1 * ncr
    return total_prob  

def flush(hand):
    if hand[0][0] == hand[1][0]:
        prob_1 = (12/50)*(11/49)*(10/48)
        ncr = nCr(5,3)
    else:
        prob_1 = (12/50)*(11/49)*(10/48)*(9/47)
        ncr = nCr(5,4)
    total_prob = prob_1 * ncr
    return total_prob       

def straight(hand):
    if abs(hand[0][1] - hand[1][1]) < 5 and abs(hand[0][1] - hand[1][1]) > 0:
        prob_1 = (3/50)*(3/49)*(3/48)
        ncr = nCr(5,3)
    else:
        prob_1 = (3/50)*(3/49)*(2/48)*(1/47)
        ncr = nCr(5,4)
    total_prob = prob_1 * ncr
    return total_prob

def three_of_kind(hand, pocket): 
    if pocket == True:
        prob_1 = (2/50)
        ncr = nCr(5,1)
    else:
        prob_1 = (3/50)*(2/50)
        ncr = nCr(5,2)
    total_prob = prob_1 * ncr
    return total_prob      

def two_pair(hand, pocket): 
    if pocket == True:
        prob_1 = (48/50)*(3/49)
        ncr = nCr(5,2)
    else:
        prob_1a = (3/50)*(3/49)
        ncr_1a = nCr(5,2)
        prob_1b = (3/50)*(45/49)*(44/48)
        ncr_1b = nCr(5,3)
        prob_1c = (44/50)*(3/49)*(40/48)*(3/47)
        ncr_1c = nCr(5,4)
        prob_1 = (prob_1a*ncr_1a)+(prob_1b*ncr_1b)+(prob_1c*ncr_1c)
        ncr = 1
    total_prob = prob_1 * ncr
    return total_prob

def one_pair(hand, pocket):
     if pocket == True:
        prob_1 = 1
        ncr =  1
     else:
        prob_1a = (6/50)
        ncr_1a = nCr(5,1)
        prob_1b = (44/50)*(3/49)
        ncr_1b = nCr(5,2)
        prob_1 = (prob_1a*ncr_1a)+(prob_1b*ncr_1b)
        ncr = 1
     total_prob = prob_1 * ncr
     return total_prob 





def test_2000():
    l = []
    for x in range(2000):
        
        deck = []
        number = []
        n_kind =[]
        kinds = ["Hearts", "Diamonds", "clubs", "Spades"]
        for k in kinds:
            for n in range(2,14):
                deck.append([k,n])
                number.append(n)
                n_kind.append(k)
        
        x,n,m = generate_hand(deck)   
        
        f = four_of_kind(x,m)
        if f > 0.0006:
            l.append(f)
    print(l)
    print(len(l)/2000)
        
def calculate_prob(deck):
    hand, deck, pocket = generate_hand(deck)
    print(hand)
    list_prob = []
    list_prob.append(round(flush_straight(hand),4))
    list_prob.append(round(four_of_kind(hand,pocket),4))
    list_prob.append(round(full_house(hand,pocket),4))
    list_prob.append(round(flush(hand),4))
    list_prob.append(round(straight(hand),4))
    list_prob.append(round(three_of_kind(hand,pocket),4))
    list_prob.append(round(two_pair(hand,pocket),4))
    list_prob.append(round(one_pair(hand,pocket),4))
    print("""Probabilities: \n\n
          Straigh flush: {0} \n
          Four of a kind: {1} \n
          Full house: {2} \n
          Flush: {3} \n
          Straight: {4} \n
          Three of a kind: {5} \n
          Two pair: {6}
          One pair: {7}""".format(list_prob[0],list_prob[1],list_prob[2],list_prob[3],list_prob[4],
          list_prob[5],list_prob[6], list_prob[7]))
