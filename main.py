import random
from euler import *
from deikstra import dijkstra


def task1(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return "Граф орієнтований" + '\n'
    return "Граф неорієнтований" + '\n'


def get_graph_list(matrix):
    res = []
    for i in range(len(matrix)):
        res.append([])
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                res[i].append(j)
    return res

def get_graph_for_dijkstra(graph):
    res = []
    for i in range(len(graph)):
        res.append([])
        for j in range(len(graph)):
            if graph[i][j] == 1:
                res[i].append(random.randint(1, 10))
            else:
                res[i].append(1000000000)
    return res


graph = [[1, 1, 0, 0, 0],
         [0, 1, 0, 1, 1],
         [1, 0, 1, 0, 0],
         [0, 1, 1, 1, 0],
         [1, 1, 1, 1, 1]]

PRIORITY = {1: ['-'], 2: ['*', '/']}


def priority(value: str) -> int:
    for k, v in PRIORITY.items():
        if value in v:
            return k
    return -1


def infix_to_postfix(expression):
    OPERATORS = set(['-', '*', '/', '(', ')', '^'])
    PRIORITY = {'-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = ''
    for ch in expression:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(ch)

    while stack:
        output += stack.pop()

    return output


OPERATORS = set(['*', '-', '%', '/', '^'])


def evaluate_postfix(expression):
    stack = []
    res = []
    for i in expression:
        if i not in OPERATORS:
            stack.append(i)
        else:

            a = stack.pop()
            b = stack.pop()
            if i == '+':
                res = int(b) + int(a)
            elif i == '-':
                res = int(b) - int(a)
            elif i == '*':
                res = int(b) * int(a)
            elif i == '%':
                res = int(b) % int(a)
            elif i == '/':
                res = int(b) / int(a)
            elif i == '^':
                res = int(b) ** int(a)
            print(b, i, a, '=', res)
            stack.append(res)
    return (''.join(map(str, stack)))

def postfix_to_prefix(expression):
    ops = ['*', '-', '%', '/', '^']
    res = ''
    tmp = ''
    for i in range(len(expression)-1, -1, -1):
        res += expression[i]

    res1 = ''
    for i in range(len(res)):
        if res[i] in ops:
            res1 += (''.join(list(reversed(tmp))))
            tmp = ''
            res1+= res[i]
        else:
            tmp += res[i]
    res1 += (''.join(list(reversed(tmp))))
    return res1


print(task1(graph))

eulerCycle(get_graph_list(graph))

print('Найкоротший шлях з початкової вершини у кінцеву: ', dijkstra(5, 0, get_graph_for_dijkstra(graph))[-1], '\n')

expression = '(8^2-4)/(2*8-6)'
print('Арифметичний вираз: ', expression)
print('Зворотній польскький запис: ', infix_to_postfix(expression))
print('Прямий польський запис: ', postfix_to_prefix(infix_to_postfix(expression)))
print(evaluate_postfix(infix_to_postfix(expression)), '\n')

