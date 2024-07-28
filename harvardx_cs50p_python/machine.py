emoticon = '🫣'

def main():
    global emoticon
    say('Is anyone there?')
    emoticon = '👋'
    say('Oh, hi!')
def say(phrase):
    print(phrase + " " + emoticon)

main()
