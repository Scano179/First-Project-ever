def cheer():
    print("😊 Hi! Here's a little boost for your day: You're doing great!")

def ask_mood():
    mood = input("How are you feeling today (good/ok/bad)? ").strip().lower()
    if mood in ("good", "great", "awesome"):
        print("That's wonderful — keep it up!")
    elif mood in ("ok", "fine"):
        print("Not bad. Maybe try something small that makes you happy.")
    elif mood in ("bad", "not good", "sad"):
        print("Sorry to hear that. It's okay to take a break and be kind to yourself.")
    else:
        print("Thanks for sharing — every feeling matters.")

def main():
    cheer()
    ask_mood()
    print("Have a nice day! 🎉")

if __name__ == "__main__":
    main()
