import time

def main():
    text_to_type = "This is a sample text for the typing test. Try to type it as fast as you can."
    print("Type the following text:")
    print(text_to_type)
    input("Press Enter when you are ready to start...")

    start_time = time.time()
    user_input = input("Start typing: ")

    end_time = time.time()
    typing_time = end_time - start_time

    accuracy = calculate_accuracy(text_to_type, user_input)
    words_per_minute = calculate_words_per_minute(user_input, typing_time)

    print("\nTyping time: {:.2f} seconds".format(typing_time))
    print("Words per minute: {:.2f}".format(words_per_minute))
    print("Accuracy: {:.2f}%".format(accuracy))

def calculate_accuracy(original_text, user_text):
    correct_characters = sum(1 for a, b in zip(original_text, user_text) if a == b)
    accuracy = (correct_characters / len(original_text)) * 100
    return accuracy

def calculate_words_per_minute(user_text, typing_time):
    words = user_text.split()
    num_words = len(words)
    minutes = typing_time / 60
    words_per_minute = num_words / minutes
    return words_per_minute

if __name__ == "__main__":
    main()
