import random, time
from random import randint
from time import sleep

progName = "Brawl Tera"
progVersion = "1.0"
progAuthor = "Flurcios prod."

brawlerTrophies = 0
brawlerRank = 1

while True:
    sleep(0.1)
    Luck = randint(0, 3) #0-lose 5-win
    print(f"Rank: {brawlerRank}, Trophies: {brawlerTrophies}")
    
    if Luck >= 1 and Luck <= 3:
        if brawlerTrophies >= 0 and brawlerTrophies <= 799:
            brawlerTrophies += 8
    
        if brawlerTrophies >= 800 and brawlerTrophies <= 899:
            brawlerTrophies += 7
        
        if brawlerTrophies >= 900 and brawlerTrophies <= 999:
            brawlerTrophies += 6
        
        if brawlerTrophies >= 1000 and brawlerTrophies <= 1099:
            brawlerTrophies += 5
            
        if brawlerTrophies >= 1100 and brawlerTrophies <= 1199:
            brawlerTrophies += 4
            
        if brawlerTrophies >= 1200:
            brawlerTrophies += 3
            
    if Luck == 0:
        if brawlerTrophies >= 0 and brawlerTrophies <= 49:
            brawlerTrophies -= 0
        
        if brawlerTrophies >= 50 and brawlerTrophies <= 99:
            brawlerTrophies -= 1
            
        if brawlerTrophies >= 100 and brawlerTrophies <= 199:
            brawlerTrophies -= 2
            
        if brawlerTrophies >= 200 and brawlerTrophies <= 299:
            brawlerTrophies -= 3
            
        if brawlerTrophies >= 300 and brawlerTrophies <= 399:
            brawlerTrophies -= 4
            
        if brawlerTrophies >= 400 and brawlerTrophies <= 499:
            brawlerTrophies -= 5
            
        if brawlerTrophies >= 500 and brawlerTrophies <= 599:
            brawlerTrophies -= 6
            
        if brawlerTrophies >= 600 and brawlerTrophies <= 699:
            brawlerTrophies -= 7
            
        if brawlerTrophies >= 700 and brawlerTrophies <= 799:
            brawlerTrophies -= 8
            
        if brawlerTrophies >= 800 and brawlerTrophies <= 899:
            brawlerTrophies -= 9

        if brawlerTrophies >= 900 and brawlerTrophies <= 999:
            brawlerTrophies -= 10
            
        if brawlerTrophies >= 1000 and brawlerTrophies <= 1099:
            brawlerTrophies -= 11
            
        if brawlerTrophies >= 1100:
            brawlerTrophies -= 12
        
    if brawlerTrophies >= 0:
        brawlerRank = 1
        if brawlerTrophies >= 10:
            brawlerRank = 2
            if brawlerTrophies >= 20:
                brawlerRank = 3
                if brawlerTrophies >= 30:
                    brawlerRank = 4
                    if brawlerTrophies >= 40:
                        brawlerRank = 5
                        if brawlerTrophies >= 60:
                            brawlerRank = 6
                            if brawlerTrophies >= 80:
                                brawlerRank = 7
                                if brawlerTrophies >= 100:
                                    brawlerRank = 8
                                    if brawlerTrophies >= 120:
                                        brawlerRank = 9
                                        if brawlerTrophies >= 140:
                                            brawlerRank = 10
                                            if brawlerTrophies >= 160:
                                                brawlerRank = 11
                                                if brawlerTrophies >= 180:
                                                    brawlerRank = 12
                                                    if brawlerTrophies >= 220:
                                                        brawlerRank = 13
                                                        if brawlerTrophies >= 260:
                                                            brawlerRank = 14
                                                            if brawlerTrophies >= 300:
                                                                brawlerRank = 15
                                                                if brawlerTrophies >= 340:
                                                                    brawlerRank = 16
                                                                    if brawlerTrophies >= 380:
                                                                        brawlerRank = 17
                                                                        if brawlerTrophies >= 420:
                                                                            brawlerRank = 18
                                                                            if brawlerTrophies >= 460:
                                                                                brawlerRank = 19
                                                                                if brawlerTrophies >= 500:
                                                                                    brawlerRank = 20
                                                                                    if brawlerTrophies >= 550:
                                                                                        brawlerRank = 21
                                                                                        if brawlerTrophies >= 600:
                                                                                            brawlerRank = 22
                                                                                            if brawlerTrophies >= 650:
                                                                                                brawlerRank = 23
                                                                                                if brawlerTrophies >=700:
                                                                                                    brawlerRank = 24
                                                                                                    if brawlerTrophies >= 750:
                                                                                                        brawlerRank = 25
                                                                                                        if brawlerTrophies >= 800:
                                                                                                            brawlerRank = 26
                                                                                                            if brawlerTrophies >= 850:
                                                                                                                brawlerRank = 27
                                                                                                                if brawlerTrophies >= 900:
                                                                                                                    brawlerRank = 28
                                                                                                                    if brawlerTrophies >= 950:
                                                                                                                        brawlerRank = 29
                                                                                                                        if brawlerTrophies >= 1000:
                                                                                                                            brawlerRank = 30
                                                                                                                            if brawlerTrophies >= 1050:
                                                                                                                                brawlerRank = 31
                                                                                                                                if brawlerTrophies >= 1100:
                                                                                                                                    brawlerRank = 32
                                                                                                                                    if brawlerTrophies >=1150:
                                                                                                                                        brawlerRank = 33
                                                                                                                                        if brawlerTrophies >= 1200:
                                                                                                                                            brawlerRank = 34
                                                                                                                                            if brawlerTrophies >= 1250:
                                                                                                                                                brawlerRank = 35
                                                                                                                                                
