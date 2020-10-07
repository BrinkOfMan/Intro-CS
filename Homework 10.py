#Ethan Brinkman
#Homework 10: 3, 4, 6, 8
#Due 3/13/19


#Number 3
print('Number 3\n')


def alphaAndE(t):
    alpha = 'abcdefghijklmnopqrstuvwkyxABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ctrA = 0
    ctrE = 0
    for i in range(len(t)):
        
        if t[i] == 'e' or t[i] == 'E':
            ctrE += 1
        elif t[i] in alpha:
            ctrA += 1
            
    print('This passage contains '+str(ctrA)+' alphabetic characters, of which '+str(ctrE)+' ('+str(round((ctrE/ctrA * 100),2))+'%)'+" are the letter 'e'.")

favParagraph = """To whom it may concern,

I am writing this complaint letter regarding the employment of Kim Bauer and how her social skills are childish at best. From the information I have been given, she has “multiple jobs she must complete”(Kim Bauer). From what I have seen, she has three. Her first and most important job is to patrol the high school parking lot, making sure that there is no suspicious cars. Her second job is to make sure that no student or pedestrian are tampering with the cars that are on the property. Finally, her final job is to make sure that all students have paid the fee for a parking pass. From the information that I have gathered, she is not needed or liked by the student body.

Every morning I drive into school, and Kim Bauers red Chrysler Sebring is facing away from the entrance. Logically speaking, she can’t even see who is in the vehicles if she is facing away from the cars. Some of the times she isn’t even in the parking lot. If her first and most important job is to spot suspicious cars that could contain a threat, how is she supposed to find them if is not even facing towards the cars, or in the lot for that matter. Now, during the school day she does take laps and look at the cars, I also think she lacks the knowledge of being able to spot a potential threat that is hidden in a car. She may not be a certified bomb detection specialist, but I am unsettled by the fact that she has not presented or shown any type of formal training.

After she “inspects cars” for potential threats she makes sure that our vehicles are secure and safe on the premises. When I had to go purchase a parking pass, I found Kim Bauer sitting in her office playing on her phone. Giving her the benefit of the doubt I assumed she was looking at cameras and was taking a quick break to rest her mind. That is 100% understandable, what I do not understand is when she went back to her computer, she didn’t even have the camera tab open, none the less active. I sat and watched her sift through her emails, many of the personal emails. I began to question the security of my vehicle and whether or not she really is taking the time to protect my property. It is extremely unprofessional to be on your phone and responding to your personal emails, when you should be doing your job, and should be making sure that people's property is safe.

Her third and final job is to collect the fees for parking passes, and enforce the rule that you must have a pass to park in the lot. This however, is not true. Multiple friends and acquaintances park in the lot without a pass for extensive periods of time without paying. I however, paid for the $150 parking pass. So I conducted a experiment. I removed my pass and began to park without it. So far, I have not been caught for three weeks. When I ended my experiment, there were five days where she was standing in the area I have parked, look at my car that does not have a pass, and simply walked away. When she does enforce the rule, she does it in a very rude manner if she manages to talk to you face to face. With a condescending tone, she makes you feel like you are a peanut and she is the hammer that cracks you. People will respond better and kinder if they are treated like humans. 

With these points in mind, please consider why this woman is employed, She is suppose to be protecting the school from harm and danger, but I do not feel any safer. All i feel is that I have been mistreated and talked to like I am some kind of infidel. I am not asking for her to be fired, but some formal training and having her take her job seriously would be a perfect solution.

With love,

Luke Meyers"""

print('My favorite passage ever was a letter to the school written by my high school friend Luke Meyers, concerning his feelings about the uselessness of the parking lot patrol.\n\n'+favParagraph+'\n')
alphaAndE(favParagraph)


#Number 4
print('\nNumber 4\n')

maxL = len(str(12 * 12)) + 1                            #The +1 is for the extra space needed at max length product

for row in range(1,13):                                 #Range of 1 through 12
    for col in range(1,13):                             #Range of 1 through 12
        prod = str(row * col)                           
        spaces = maxL - len(prod)                       #However many spaces needed to keep the consistent MaxLength throughout each iteration
        print(prod,end =' ' * spaces)                   #Print the times table for the current row through 12
    print()                                             #Line break


#Number 6
print('\nNumber 6\n')

def reverse(s):
    newString = ''
    for char in s:
        newString = char + newString        #Add the character in reverse order
        
    return newString

string = input('Please enter a string, and I will reverse it.\n')
print(reverse(string))


#Number 8
print('\nNumber 8\n')

def removeE(s):
    newString = ''
    for char in s:
        if char == 'e' or char == 'E':
            pass                            #Don't do anything
        else:
            newString += char               #Add that character to the new string
            
    return newString

print("I will now remove every instance of the letter e from Luke's letter.\nBehold.\n")
print(removeE(favParagraph))

input()
