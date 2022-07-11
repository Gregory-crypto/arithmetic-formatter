
def arithmetic_arranger(problems, argument=False):
    line1 = []
    line2 = []
    line3 = []
    line4 = []

    for i in problems:
        problem = i.split()
        a = problem[0]
        len_a = len(a)
        operator = problem[1]
        b = problem[2]
        len_b = len(b)
        counter = max(len_a, len_b) + 2

        if len(problems) > 5:
            return "Error: Too many problems."

        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."
        
        try:
            a = int(a)
            b = int(b)
        except:
            return "Error: Numbers must only contain digits."


        if a > 9999 or b > 9999:
            return "Error: Numbers cannot be more than four digits."

        a = str(a)
        b = str(b)

        line1.append(' ' * (counter - len_a) + a + ' ' * 4)
        line2.append(operator + ' ' * (counter - 1 - len_b) + b + ' ' * 4)
        line3.append('-' * counter + ' ' * 4)
      
        if argument == True:
            if operator == '+':
                answer = str(int(a) + int(b))
                len_ans = len(answer)
                line4.append(' ' * (counter - len_ans) + answer + ' ' * 4)
            else:
                answer = str(int(a) - int(b))
                len_ans = len(answer)
                line4.append(' ' * (counter - len_ans) + answer + ' ' * 4)

  
    if argument == True:
        return (''.join(line1).rstrip() + '\n' + ''.join(line2).rstrip() + '\n' +
            ''.join(line3).rstrip() + '\n' + ''.join(line4).rstrip())
    else:
        return (''.join(line1).rstrip() + '\n' + ''.join(line2).rstrip() + '\n' +
            ''.join(line3).rstrip())