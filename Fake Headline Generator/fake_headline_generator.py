import random

def generate_fake_headline():
    subjects = [
        "Scientists", "Politicians", "Celebrities", "Tech Giants", "Researchers",
        "Athletes", "Artists", "Entrepreneurs", "Activists", "Educators"
    ]
    
    actions = [
        "discover", "announce", "criticize", "support", "challenge",
        "revolutionize", "investigate", "launch", "debate", "transform"
    ]
    
    objects = [
        "new technology", "climate change solutions", "health breakthroughs",
        "economic reforms", "social movements", "artistic trends",
        "sports innovations", "educational methods", "political strategies",
        "cultural phenomena"
    ]
    
    subject = random.choice(subjects)
    action = random.choice(actions)
    object_ = random.choice(objects)
    
    headline = f"{subject} {action} {object_}"
    return headline

if __name__ == "__main__":
    while True:
        print(generate_fake_headline())
        user_input = input("Generate another headline? (y/n): ").lower()
        if user_input != 'y':
            break