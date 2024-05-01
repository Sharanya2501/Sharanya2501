#Write a Python function named feedback_analysis() to calculate and display the following information:
#Total feedbacks stored in the file.
#Count of positive feedbacks.
#Count of negative feedbacks.

def feedback_analysis():
    positive = 0
    negative = 0
    with open('/PracticePrograms/feedback.txt', 'r') as fil:
        file = fil.readlines()
        print(file)
        print(len(file))
        for line in file:
            if line.startswith('Positive'):
                positive +=1
            elif line.startswith('Negative'):
                negative +=1

        print(positive)
        print(negative)

feedback_analysis()