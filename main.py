import json
import random
def chatbot():

    while True:
        with open("dataset.json", "r") as file:
            data = json.load(file)
        questions = data["items"]

        user = input("you : ").lower().strip()
        if user == "quit" or user == "exit" or user == "bye":
            print("bye bye Mr. american pie!!!")
            break

        found = False
        for item in questions:
            item_questions = item["question"] if isinstance(item["question"], list) else [item["question"]]
            if any(user in q.lower() for q in item_questions):
                ans = random.choice(item["answers"]) 
                print("momo :", ans)    
                found = True
                break

        if not found:
            print("momo : sorry I don't know it's answer")
def store_info():
    pass

def read_info():
    pass

if __name__ == "__main__":
    chatbot()