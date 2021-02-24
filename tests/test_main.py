from word_ladder import _adjacent,verify_word_ladder,word_ladder
import random

def test__word_ladder_1():
    assert not _adjacent('stone','money')

def test__word_ladder_1b():
    assert not _adjacent('money','stone')

def test__word_ladder_2():
    assert not _adjacent('stone','stone1')

def test__word_ladder_3():
    assert not _adjacent('stone1','stone')

def test__word_ladder_4():
    assert _adjacent('stone','stony')

def test__word_ladder_4v():
    assert _adjacent('stony','stone')

def test__word_ladder_5():
    assert _adjacent('stone','shone')

def test__word_ladder_5b():
    assert _adjacent('shone','stone')

def test__word_ladder_6():
    assert not _adjacent('shone','shone')

def test__word_ladder_7():
    assert not _adjacent('','shone')

def test__word_ladder_7b():
    assert not _adjacent('shone','')

def test__word_ladder_fuzz():
    with open('words5.dict') as f:
        words = f.readlines()
        words = list(set([ word.strip() for word in words ]))
    for i in range(1000000):
        word1 = random.choice(words)
        word2 = random.choice(words)
        res1 = _adjacent(word1, word2)
        res2 = _adjacent(word2, word1)
        assert res1 == res2 or res1 is res2

def test__verify_word_ladder_1():
    assert not verify_word_ladder([])

def test__verify_word_ladder_2():
    assert verify_word_ladder(['stone'])

def test__verify_word_ladder_3():
    assert verify_word_ladder(['stone'])

def test__verify_word_ladder_4():
    assert verify_word_ladder(['stone', 'shone'])

def test__verify_word_ladder_5():
    assert verify_word_ladder(['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money'])

def test__verify_word_ladder_5b():
    assert verify_word_ladder(list(reversed(['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money'])))

def test__verify_word_ladder_6():
    assert not verify_word_ladder(['stone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money'])

def test__verify_word_ladder_6b():
    assert not verify_word_ladder(list(reversed(['stone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money'])))

def test__verify_word_ladder_7():
    assert not verify_word_ladder(['stone', 'shone', 'phone', 'phony', 'peony', 'benny', 'bonny', 'boney', 'money'])

def test__verify_word_ladder_7b():
    assert not verify_word_ladder(list(reversed(['stone', 'shone', 'phone', 'phony', 'peony', 'benny', 'bonny', 'boney', 'money'])))

def test__verify_word_ladder_8():
    assert not verify_word_ladder(['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'money'])

def test__verify_word_ladder_8b():
    assert not verify_word_ladder(list(reversed(['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'money'])))

# tests for memory management correctness
def test__verify_word_ladder_9():
    assert verify_word_ladder(['chins', 'chine'])

def test__verify_word_ladder_9b():
    assert verify_word_ladder(['chine', 'chins'])

def test__verify_word_ladder_10():
    assert verify_word_ladder(['chins', 'chink'])

def test__verify_word_ladder_10b():
    assert verify_word_ladder(['chink', 'chins'])

def test__verify_word_ladder_11():
    assert verify_word_ladder(['chine', 'chink'])

def test__verify_word_ladder_11b():
    assert verify_word_ladder(['chink', 'chine'])

def test__word_ladder_1():
    ladder = word_ladder('stone','stone')
    assert verify_word_ladder(ladder) and len(ladder)==1

def test__word_ladder_2():
    ladder = word_ladder('aloof','aloof')
    assert verify_word_ladder(ladder) and len(ladder)==1

def test__word_ladder_3():
    ladder = word_ladder('stone','shone')
    assert verify_word_ladder(ladder) and len(ladder)==2

def test__word_ladder_3b():
    ladder = word_ladder('shone','stone')
    assert verify_word_ladder(ladder) and len(ladder)==2

def test__word_ladder_4():
    ladder = word_ladder('dears','fears')
    assert verify_word_ladder(ladder) and len(ladder)==2

def test__word_ladder_4b():
    ladder = word_ladder('fears','dears')
    assert verify_word_ladder(ladder) and len(ladder)==2

def test__word_ladder_5():
    ladder = word_ladder('stone','phone')
    assert verify_word_ladder(ladder) and len(ladder)==3

def test__word_ladder_6():
    ladder = word_ladder('phone','stone')
    assert verify_word_ladder(ladder) and len(ladder)==3

def test__word_ladder_7():
    ladder = word_ladder('babes','child')
    assert verify_word_ladder(ladder) and len(ladder)==9

def test__word_ladder_8():
    ladder = word_ladder('child','babes')
    assert verify_word_ladder(ladder) and len(ladder)==9

def test__word_ladder_9():
    ladder = word_ladder('devil','angel')
    assert verify_word_ladder(ladder) and len(ladder)==9

def test__word_ladder_10():
    ladder = word_ladder('angel','devil')
    assert verify_word_ladder(ladder) and len(ladder)==9

def test__word_ladder_11():
    ladder = word_ladder('money','smart')
    assert verify_word_ladder(ladder) and len(ladder)==11

def test__word_ladder_12():
    ladder = word_ladder('smart','money')
    assert verify_word_ladder(ladder) and len(ladder)==11

def test__word_ladder_13():
    ladder = word_ladder('stone','money')
    assert verify_word_ladder(ladder) and len(ladder)==10

def test__word_ladder_14():
    ladder = word_ladder('money','stone')
    assert verify_word_ladder(ladder) and len(ladder)==10

def test__word_ladder_15():
    assert word_ladder('atlas','zebra') is None

def test__word_ladder_15b():
    assert word_ladder('zebra','atlas') is None

def test__word_ladder_16():
    assert word_ladder('aloof','money') is None

def test__word_ladder_16b():
    assert word_ladder('money','aloof') is None

def test__word_ladder_17():
    assert word_ladder('data','structures') is None

def test__word_ladder_fuzz():
    with open('words5.dict') as f:
        words = f.readlines()
        words = list(set([ word.strip() for word in words ]))
    for i in range(20):
        word1 = random.choice(words)
        word2 = random.choice(words)
        res1 = word_ladder(word1, word2)
        if res1 is not None:
            res2 = word_ladder(word2, word1)
            assert res1 is None and res2 is None or len(res1) == len(res2)
