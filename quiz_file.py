class Quizbrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number}: {current_question.qn} ? (True/False): ")
        self.check_answer(response, current_question.ans)



    def check_answer(self,user_ans,correct_ans):
        if user_ans == correct_ans.lower():
            self.score +=1
            print("Correct Answer!!")
        else:
            print("Wrong Answer!")
