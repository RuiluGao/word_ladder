#!/bin/python3
from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny',
    'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots',
    'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    if(start_word == end_word):
        return [start_word]
    if len(start_word) != len(end_word):
        return None

    with open(dictionary_file) as f:
        words = f.readlines()
    clean_dic = []
    for word in words:
        clean_dic.append(word.strip('\n'))

    stack = []
    stack.append(start_word)
    q = deque()
    q.append(stack)

    while q != deque():
        current_stack = q.popleft()
        for word in clean_dic:
            if _adjacent(word, current_stack[-1]):
                if word == end_word:
                    current_stack.append(word)
                    return current_stack
                new_copy = copy.deepcopy(current_stack)
                new_copy.append(word)
                q.append(new_copy)
                clean_dic.remove(word)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''

    if ladder is None:
        return False
    if len(ladder) == 0:
        return False
    if len(ladder) == 1:
        return True

    for i in range(len(ladder) - 1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    diff = 0
    if len(word1) != len(word2):
        return False
    else:
        for i in range(len(word1)):
            if not word1[i] == word2[i]:
                diff += 1
        return diff == 1
