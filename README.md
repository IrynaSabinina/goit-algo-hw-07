# Рішення завдань для Дерев Пошуку та Системи Коментарів

Цей репозиторій містить рішення для чотирьох завдань, пов'язаних з Деревами Пошуку (BST), Деревами AVL та системою коментарів з ієрархічними відповідями.

## Огляд Завдань

### Завдання 1: Знайти найбільше значення у двійковому дереві пошуку або в AVL-дереві

Знайти найбільше значення у двійковому дереві пошуку (BST) або в AVL-дереві.

#### Фрагмент коду:


class TreeNode:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

def find_max(root):
    while root and root.right: 
        root = root.right
    return root.key if root else None


### Завдання 2: Знайти найменше значення у двійковому дереві пошуку або в AVL-дереві
Знайти найменше значення у двійковому дереві пошуку (BST) або в AVL-дереві.

#### Фрагмент коду:

class TreeNode:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

def find_min(root):
    while root and root.left:
        root = root.left
    return root.key if root else None

### Завдання 3: Обчислити суму всіх значень у двійковому дереві пошуку або в AVL-дереві
Обчислити суму всіх значень у двійковому дереві пошуку (BST) або в AVL-дереві.

#### Фрагмент коду:

def sum_tree(root):
    if root is None: return 0
    return root.key + sum_tree(root.left) + sum_tree(root.right)
Завдання 4: Реалізація системи коментарів з ієрархічними відповідями
Реалізуйте систему коментарів, де коментарі можуть мати відповіді, а ці відповіді можуть мати свої відповіді, формуючи ієрархічну структуру.

#### Фрагмент коду:
class Comment:
    def __init__(self, text, author):
        self.text, self.author, self.replies, self.is_deleted = text, author, [], False
    def add_reply(self, reply): self.replies.append(reply)
    def remove_reply(self): self.text, self.is_deleted = "Цей коментар було видалено.", True
    def display(self, indent=0):
        print(f"{'    '*indent}{self.author}: {self.text}" if not self.is_deleted else f"{'    '*indent}{self.text}")
        for reply in self.replies: reply.display(indent+1)
