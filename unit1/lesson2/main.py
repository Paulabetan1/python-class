questions = [
    {
        'question':'What it is the capital of France?',
        'options':['A) Berlin', 'B) Madrid', 'C) Paris', 'D) Roma'],
        'answer':'C'
    },
    {
        "question" : "What it is the capital of Japan?",
        "options" : ['A) Berlin', 'B) Beijing', 'C) Paris' , 'D) Tokyo'],
        "answer" : 'D'
    },
    {
        'question': "What is the capital of Canada?",
        'options': ['A) Ottawa', 'B) Toronto', 'C) Vancouver', 'D) Montreal'],
        'answer': 'A'
    },
    {
        'question': "Which city is the capital of Australia?",
        'options': ['A) Sydney', 'B) Canberra', 'C) Melbourne', 'D) Perth'],
        'answer': 'B'
    }
]

times = 0

for question in questions:
    print(f'❓ \n {question['question']}')
    #print(f'{question['options']}')
    #print(f'{question['answer']}')

    for option in question['options']:
        print(f'⭕ {option}')
    
    answer = input('Your answer (A/B/C/D): ')
    
    if answer.upper() == question['answer']:
        times += 1  
        print(f'✅ Good Job!!!')
    
    else:
        print('You suck!!! 💩')

    print(f'This is your stars {'⭐' * times}')

print('************* FINAL SCORE ****************')
if times == len(questions):
    print('Perfect Score!! 🏆')
elif times >= 2:
    print('Wow! you did alright 😕')
else:
    print('😢')
