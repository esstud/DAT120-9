#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 10:13:49 2021

@author: stoliarovevgeni
"""

class MultipleChoice:
    #Constructor
    def __init__(self, question, alternatives, correct_answer):
        self.question = question
        self.alternatives = alternatives
        self.correct_answer = correct_answer


    def answer_check(self, entered_integer):
        if entered_integer == self.correct_answer:
            return 'You right!'
        else:
            return 'Sorry , that´s not correct...'


    def __str__(self):
       # return f'{self.question} (enter the number you think is correct under the dotted line below)\n' + '\n'.join(f'{indeks} - {element}' 
       #     for indeks, element in enumerate(self.alternatives,1))+ '\n--------------------\n'
       return f"{self.question} n 1: {self.alternatives[0]} / n 2: {self.alternatives[1]}"
   
   

if __name__ == '__main__':
    question1 = MultipleChoice('What´s best?', ['BMW', 'Ford'], 1)
    question2 = MultipleChoice('Capitol of Norway?' , ['Amsterdam', 'Oslo'], 2)
    
    answer1 = int(input(question1))
    print(question1.answer_check(answer1))
    answer2 = int(input(question2))
    print(question2.answer_check(answer2))


