import random as r
count = 0
a = r.randint(1,10)
print("---ಪಜಲ್ ಗೇಮ್ ಗೆ ಸ್ವಾಗತ---")
print(" ")
for i in range(3):
    n = int(input("ಒಂದು ಸಂಖ್ಯೆಯನ್ನು ಹಾಕಿ: "))
    if a == n:
        print("ನೀವು ಸರಿಯಾದ ಉತ್ತರ ನೀಡಿದ್ದೀರಿ.. ಧನ್ಯವಾದಗಳು...")
        break
    else:
        print("ನಿಮ್ಮ ಉತ್ತರ ತಪ್ಪು... ")
        count =  count+1 
    if count == 3:
        print("ನೀವು ನಿಮ್ಮ ಗರಿಷ್ಟ ಮಿತಿಯನ್ನು ಮೀರಿದ್ದೀರಿ... ಪುನಃ ಪ್ರಯತ್ನಿಸಿ ..")
        print ("ಸರಿಯಾದ ಉತ್ತರ : ",a)