class Quiz:
    def __init__(self):
        self.questions = [
            "Largest planet?\nA.EARTH B.MARS C.JUPITER",
            "Capital of India?\nA.DELHI B.MUMBAI C.CHENNAI",
            "7+7=?\nA.10 B.14 C.16"
        ]
        self.answers = ["C", "A", "B"]
        self.score = 0

    def start_quiz(self):
        for i in range(len(self.questions)):
            print(self.questions[i])
            user_ans = input("Enter choice: ").upper()
            if user_ans == self.answers[i]:
                self.score += 1

    def display_score(self):
        print("Final Score:", self.score)


q = Quiz()
q.start_quiz()
q.display_score()
