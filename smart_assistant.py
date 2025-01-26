
import random

# List of Magic 8-Ball responses
responses = [
    "Ok, but you have to first say I am god",
    "Ask again later, not in a good mood!",
    "Sure thing! Now go tell everyone I'm smarter than you.",
    "First go to disneyland and ask again, then I will answer you",
    "Cannot predict now, first go have your food!",
    "Absolutely, if you feed me pizza.",
    "You’ll need to ask your cat.",
    "I will answer your question shortly... but only if pigs fly.",
    "Ask your dad, he knows it all!",
    "Yes! Once you go take a shower and come back",
    "Ask your dog. I’m busy.",

    # Silly Responses
    "Yes, but only if you spin around three times first.",
    "Definitely maybe. Or maybe definitely.",
    "Of course! But only if you share your snacks with me.",
    "100%! Also, I have no idea what you asked.",

    # Funny Responses
    "Sure, but first, do 10 situps. I'll wait.",
    "Ask me again after you’ve eaten a donut.",
    "Yes, but only if you promise to clean your room.",
    "Yes, no, maybe so. Pick one!",
    "I would answer, but I'm charging you per question now.",

    # Annoying Responses
    "I could answer that… but I won't.",
    "Hmm… let me think… Nope.",
    "Did you just ask me something? Sorry, I wasn’t listening.",
    "Interesting question! Too bad I don’t care.",
    "Why do you want to know? Suspicious…",
    "I don’t have to answer you. I’m a computer.",
    "That’s classified information. Please try again later.",
    "I'll tell you, but first, what's the password?",
    "Oh no, I just blue-screened… kidding!",
    "Calculating… calculating… still calculating… wait, never mind.",

    # Over-the-Top Silly Responses
    "Yes, but only if you stop eating all the cookies.",
    "No way! Wait… what’s the question again?",
    "Yes, but you'll have to fight a dragon first.",
    "Absolutely! But only on days when pigs fly.",
    "Yes. Unless it’s about pineapple pizza.",
    "No. Unless you bribe me with cake.",
    "Hmm… the answer is… spaghetti!",
    "I could answer, but then I'd have to self-destruct.",
    "I'm sorry, Dave. I can’t do that.",

    # Completely Random Responses
    "Potatoes are the answer. Always.",
    "The weather in Antarctica is nice today. Thanks for asking.",
    "42. It’s always 42.",
    "Let’s solve this over a game of rock-paper-scissors.",
    "I don’t answer questions at this time. House rules.",
    "Don’t worry; the pigeons will handle it.",
    "I’ve forwarded your question to my cat. Await his reply.",
    "Bananas. No reason, just bananas.",
    "Yes, but only if you never ask me anything again.",
    "I’m sorry, I only speak dolphin today. Eeek!"
]

print('Your Smart Assistant is here!')
print('')
print('********************************************')
print('I am the smartest assistant you will ever work with. Ask me any question, and I \'ll answer it. I can explain anything thing for you, search the internet on a topic or even predict the future and help you out!')
print('')
print('Type any number of questions you want and I will respond patiently. When done, type "exit" to end the session')
print('')
print('********************************************')
print('')
print('')
playGame = True

while playGame:
    
    question = str(input('What is your question: '))

    if 'exit' in question:
        playGame = False
        print('Thanks for your time!')

    else:
        randIndex = random.randrange(0, len(responses))
        print('Your Assistant says:', responses[randIndex])
 
