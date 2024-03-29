import math

# can be configured by command options
USE_FIRST_CONSONANT = False
COMPARE_LEADING_PHONEMES = True
WORD_WEIGHTS = []


CONSONANT_IMPORTANCE = 1
VOWEL_IMPORTANCE = 2

#                   (voiced, lips, n_like, stop, alveolar_depth, slide_level, hiss_level)
CONSONANT_WEIGHTS = [   1.0,   .3,    1.2,   .9,           .6/8,        .5/3,       .5/4]

#                   (voiced, mouth_openness, mouth_depth, r_sound)
VOWEL_WEIGHTS     = [   1.0,         1.0/16,      1.0/16,     1.0]


#                          [last_consonant, last_vowel, 2_to_last_consonant, 2_to_last_vowel, ...    ]
WORD_WEIGHTS_RHYME       = [           1.0,        1.0,                  .8,              .8, .4, .4, .2, .2]
WORD_WEIGHTS_RHYME_HARD  = [            .9,        1.0,                  .9,             1.0]
WORD_WEIGHTS_RHYME_SOFT  = [            .7,        1.0,                  .8,              .8, .7, .6, .5, .4, .3, .2, .1]
WORD_WEIGHTS_FLAT        = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
WORD_WEIGHTS_LINEAR      = [1.0, .9, .9, .8, .8, .7, .7, .6, .6, .5, .5, .4, .4, .3, .3, .2, .2, .1, .1]
WORD_WEIGHTS_LIN_SHORT   = [1.0, .9, .8, .7, .6, .5, .4, .3, .2, .1]
                                                                           


# returns (starting_phoneme, rest_of_word)
def standard_to_weston_phoneme(ph):

    # emphasis
    if ph.startswith('ˈ'):
        return ('',ph[1:])
    elif ph.startswith('ˌ'):
        return ('',ph[1:])

    # simple consonants
    elif ph.startswith('b'):
        return ('b',ph[1:])    
    elif ph.startswith('k'):
        return ('k',ph[1:])    
    elif ph.startswith('d'):
        return ('d',ph[1:])    
    elif ph.startswith('f'):
        return ('f',ph[1:])    
    elif ph.startswith('g'):
        return ('g',ph[1:])    
    elif ph.startswith('h'):
        return ('h',ph[1:])    
    elif ph.startswith('l'):
        return ('l',ph[1:])    
    elif ph.startswith('m'):
        return ('m',ph[1:])    
    elif ph.startswith('n'):
        return ('n',ph[1:])
    elif ph.startswith('p'):
        return ('p',ph[1:])    
    elif ph.startswith('r'):
        return ('R',ph[1:])    
    elif ph.startswith('s'):
        return ('s',ph[1:])    
    elif ph.startswith('t'):
        return ('t',ph[1:])    
    elif ph.startswith('v'):
        return ('v',ph[1:])    
    elif ph.startswith('w'):
        return ('w',ph[1:])    
    elif ph.startswith('j'):
        return ('y',ph[1:])    
    elif ph.startswith('z'):
        return ('z',ph[1:])    

    # complex consonants
    elif ph.startswith('θ'):
        return ('th',ph[1:])    
    elif ph.startswith('ð'):
        return ('dh',ph[1:])    
    elif ph.startswith('ʃ'):
        return ('sh',ph[1:])
    elif ph.startswith('ʒ'):
        return ('zh',ph[1:])    
    elif ph.startswith('ʧ'):
        return ('ch',ph[1:])    
    elif ph.startswith('ʤ'):
        return ('j',ph[1:])
    elif ph.startswith('ŋ'):
        return ('ng',ph[1:])    
    
    # r vowels
    elif ph.startswith('aɪər'):
        return ('Ir', ph[4:])
    elif ph.startswith('aɪr'):
        return ('Ir', ph[3:])    
    elif ph.startswith('ɪr'):
        return ('Er', ph[2:])
    elif ph.startswith('ir'):
        return ('Er', ph[2:])
    elif ph.startswith('ɛr'):
        return ('Ar', ph[2:])
    elif ph.startswith('ɑr'):
        return ('or', ph[2:])
    elif ph.startswith('ɔr'):
        return ('Or', ph[2:])
    elif ph.startswith('ʊr'):
        return ('Ur', ph[2:])
    elif ph.startswith('ər'):
        return ('-r', ph[2:])
    elif ph.startswith('ɜr'):
        return ('-r', ph[2:])

    # complex vowels
    elif ph.startswith('aʊ'):
        return ('ow', ph[2:])
    elif ph.startswith('ɔɪ'):
        return ('oy', ph[2:])

    # simple vowels
    elif ph.startswith('æ'):
        return ('a', ph[1:])
    elif ph.startswith('eɪ'):
        return ('A', ph[2:])
    elif ph.startswith('ɛ'):
        return ('e', ph[1:])
    elif ph.startswith('i'):
        return ('E', ph[1:])
    elif ph.startswith('ɪ'):
        return ('i', ph[1:])
    elif ph.startswith('aɪ'):
        return ('I', ph[2:])
    elif ph.startswith('ɑ'):
        return ('o', ph[1:])
    elif ph.startswith('ɔ'):
        return ('o', ph[1:])
    elif ph.startswith('oʊ'):
        return ('O', ph[2:])
    elif ph.startswith('ʌ'):
        return ('u', ph[1:])
    elif ph.startswith('ə'):
        return ('u', ph[1:])
    elif ph.startswith('u'):
        return ('U', ph[1:])
    elif ph.startswith('ʊ'):
        return ('-', ph[1:])

    # non yet impl
    else:
        #print("could not read "+ph)
        return('?', ph[1:])


    
# returns (starting_phoneme, rest_of_word)
def westons_to_list(wesword):
    ww = wesword
    
    # simple consonants
    if ww.startswith('b'):
        return ('b',ww[1:])    
    elif ww.startswith('k'):
        return ('k',ww[1:])    
    elif ww.startswith('d'):
        return ('d',ww[1:])    
    elif ww.startswith('f'):
        return ('f',ww[1:])    
    elif ww.startswith('g'):
        return ('g',ww[1:])    
    elif ww.startswith('h'):
        return ('h',ww[1:])    
    elif ww.startswith('l'):
        return ('l',ww[1:])    
    elif ww.startswith('m'):
        return ('m',ww[1:])    
    elif ww.startswith('n'):
        return ('n',ww[1:])
    elif ww.startswith('p'):
        return ('p',ww[1:])    
    elif ww.startswith('R'):
        return ('R',ww[1:])    
    elif ww.startswith('s'):
        return ('s',ww[1:])    
    elif ww.startswith('t'):
        return ('t',ww[1:])    
    elif ww.startswith('v'):
        return ('v',ww[1:])    
    elif ww.startswith('w'):
        return ('w',ww[1:])    
    elif ww.startswith('y'):
        return ('y',ww[1:])    
    elif ww.startswith('z'):
        return ('z',ww[1:])    

    # complex consonants
    elif ww.startswith('th'):
        return ('th',ww[2:])    
    elif ww.startswith('dh'):
        return ('dh',ww[2:])    
    elif ww.startswith('sh'):
        return ('sh',ww[2:])
    elif ww.startswith('zh'):
        return ('zh',ww[2:])    
    elif ww.startswith('ch'):
        return ('ch',ww[2:])    
    elif ww.startswith('j'):
        return ('j',ww[1:])
    elif ww.startswith('ng'):
        return ('ng',ww[2:])    
    
    # r vowels
    elif ww.startswith('Ir'):
        return ('Ir', ww[2:])
    elif ww.startswith('Ir'):
        return ('Ir', ww[2:])    
    elif ww.startswith('Er'):
        return ('Er', ww[2:])
    elif ww.startswith('Er'):
        return ('Er', ww[2:])
    elif ww.startswith('Ar'):
        return ('Ar', ww[2:])
    elif ww.startswith('or'):
        return ('or', ww[2:])
    elif ww.startswith('Or'):
        return ('Or', ww[2:])
    elif ww.startswith('Ur'):
        return ('Ur', ww[2:])
    elif ww.startswith('-r'):
        return ('-r', ww[2:])

    # complex vowels
    elif ww.startswith('ow'):
        return ('ow', ww[2:])
    elif ww.startswith('oy'):
        return ('oy', ww[2:])

    # simple vowels
    elif ww.startswith('a'):
        return ('a', ww[1:])
    elif ww.startswith('A'):
        return ('A', ww[1:])
    elif ww.startswith('e'):
        return ('e', ww[1:])
    elif ww.startswith('E'):
        return ('E', ww[1:])
    elif ww.startswith('i'):
        return ('i', ww[1:])
    elif ww.startswith('I'):
        return ('I', ww[2:])
    elif ww.startswith('o'):
        return ('o', ww[1:])
    elif ww.startswith('O'):
        return ('O', ww[1:])
    elif ww.startswith('u'):
        return ('u', ww[1:])
    elif ww.startswith('u'):
        return ('u', ww[1:])
    elif ww.startswith('U'):
        return ('U', ww[1:])
    elif ww.startswith('-'):
        return ('-', ww[1:])

    # non yet impl
    else:
        #print("could not read "+ph)
        return('?', ww[1:])

def to_mine_once(x):
    return standard_to_weston_phoneme(x)

def to_mine(phone):
    a = ''
    b = phone
    w = "["
    while len(b):
        a, b = to_mine_once(b)
        if a == '?':
            return ''
        w += a + ''
    w = w[:]+']'
    return w.strip()



def is_vowel(ph):
    return [ph] in [['Ir'], ['Ir'], ['Er'], ['Ar'], ['or'], ['Or'],
                    ['Ur'], ['-r'], ['ow'], ['oy'], ['a'], ['A'],
                    ['e'], ['E'], ['i'], ['I'], ['o'], ['O'], ['u'],
                    ['u'], ['U'], ['-']]


def get_word_to_phone():    
    words = open("clean-words.txt").read().split('\n')
    phones = open("clean-phones.txt").read().split('\n')
    word_to_phone = {}
    clean_words = []
    for i in range(len(words)):
        w = words[i]
        ph = phones[i]
        if w != ph and len(to_mine(ph)):
            word_to_phone[w] = ph
            clean_words.append(w)
    return clean_words, word_to_phone
WORDS, WORD_TO_PHONE = get_word_to_phone()

def phoneme_and_vec_from_line(line):
    try:
        spl = line.split()
        assert len(spl) == 2
        ph = spl[0]
        vec = [float(n) for n in spl[1][1:-1].split(',')]
    except:
        print("bad phoneme vector definition in 'values' file")
        print(line)
        exit(1)
    return ph, vec
        
def get_phoneme_to_vec():
    value_lines = open("values").readlines()
    phoneme_to_vec = {}
    for line in value_lines:
        line = line.strip()
        if (not len(line)) or line.startswith("//") or line.startswith("#"):
            continue
        ph, vec = phoneme_and_vec_from_line(line)
        phoneme_to_vec[ph] = vec
    return phoneme_to_vec
PHONEME_TO_VEC = get_phoneme_to_vec()
                    
        
        
def phoneme_distance(p1, p2, weights):
    vec1 = PHONEME_TO_VEC[p1]
    vec2 = PHONEME_TO_VEC[p2]
    sum = 0
    for i in range(len(weights)):
        sum += math.pow((vec1[i] - vec2[i])*weights[i], 2)
    return math.sqrt(sum)

def vowel_distance(v1, v2):
    return phoneme_distance(v1, v2, VOWEL_WEIGHTS)

# more complicated because we represent a consonant as a list of consonant
# phonemes since you can have multiple consonant phonemes in a row
def consonant_distance(c1, c2):
    if len(c2) > len(c1):
        temp = c1
        c1 = c2
        c2 = temp
    n = len(c1)
    if len(c2) != len:
        c2 = ['0']*(n-len(c2)) + c2
    sum = 0
    for i in range(n):
        sum += phoneme_distance(c1[i],c2[i], CONSONANT_WEIGHTS)*(i+1)**2
               # somewhere between adding the differences and averaging them
               # (with more weight for the phonemes that come first in the
               # word (last in the consonant list))
    sum /= n**2
    return sum

def cv_list_distance(cv_list1, cv_list2, weights):
    
    # we want cv_list1 to be whichever is bigger
    if len(cv_list2) > len(cv_list1):
        temp = cv_list1
        cv_list1 = cv_list2
        cv_list2 = temp

    # add or subtract elements to make the 2 lists the same length
    if len(cv_list1) != len(cv_list2):
        if COMPARE_LEADING_PHONEMES:
            cv_list2 += ['0', ['0']]*int((len(cv_list1)-len(cv_list2))/2)
        else:
            cv_list1 = cv_list1[:len(cv_list2)]

    # sum differences of phonemes
    sum = 0
    num_ph_to_compare = min(int(len(cv_list1)/2), int(len(weights)/2))
    for i in range(num_ph_to_compare):
        ic = i * 2
        iv = ic + 1
        sum += consonant_distance(cv_list1[ic], cv_list2[ic]) * weights[ic] * CONSONANT_IMPORTANCE
        sum += vowel_distance(cv_list1[iv], cv_list2[iv])     * weights[iv] * VOWEL_IMPORTANCE

    # add the difference of the leading consonants if appropriate
    last = len(cv_list1) - 1
    if USE_FIRST_CONSONANT and last < len(weights):
        sum += consonant_distance(cv_list1[last], cv_list2[last])*weights[last]

    return sum


def word_distance(word1, word2):
    cv1 = to_cv_list(word1)
    cv2 = to_cv_list(word2)
    return cv_list_distance(cv1, cv2, WORD_WEIGHTS)

def wesword_distance(wesword, word2):
    cv1 = wesword_to_cv_list(wesword)
    cv2 = to_cv_list(word2)
    return cv_list_distance(cv1, cv2, WORD_WEIGHTS)




def to_ph_list(word):
    ph_list = []
    phone = WORD_TO_PHONE[word]
    ph = ''
    while len(phone):
        ph, phone = to_mine_once(phone)
        if len(ph):
            ph_list.append(ph)
    return ph_list
    

def wesword_to_ph_list(wesword):
    ph_list = []
    while len(wesword):
        ph, wesword = westons_to_list(wesword)
        ph_list.append(ph)
    return ph_list


def ph_list_to_cv_list(ph_list):
    cv_list = []
    on_consonant = True
    for i in range(len(ph_list) - 1, -1, -1):
        ph = ph_list[i]
        if is_vowel(ph):
            if on_consonant:
                cv_list.append(['0'])
                cv_list.append(ph)
            else:
                cv_list.append(ph)
                on_consonant = True
        else:
            if on_consonant:
                cv_list.append([ph])
                on_consonant = False
            else:
                cv_list[len(cv_list)-1].append(ph)
    if on_consonant:
        cv_list.append(['0'])
    return cv_list

def wesword_to_cv_list(wesword):
    ph_list = wesword_to_ph_list(wesword)
    return ph_list_to_cv_list(ph_list)

# convert word into an alternating list of consonants and vowels, inserting
# 0s (no sound) where necessary
# List will be backwards (last consonant first)
def to_cv_list(word):
    ph_list = to_ph_list(word)
    return ph_list_to_cv_list(ph_list)

                
    
        



    
def parse_args(args):
    mode = "pronounce"
    options = {
        "use-first-consonant": False,
        "compare-leading-phonemes": False,
        "number": 20
    }
    direct_args = []
    i = 0
    while i < len(args):
        arg = args[i]
        if arg.startswith("-"):
            if arg == "--rhyme":
                mode = "rhyme"
            elif arg == "--distance":
                mode = "distance"
            elif arg == "--use-first-consonant":
                options["use-first-consonant"] = True
            elif arg == "--compare-leading-phonemes":
                options["compare-leading-phonemes"] = True
            elif arg == "--number":
                assert len(args) > i+1
                options["number"] = int(args[i+1])
                i += 1
            else:
                print("unrecognized option")
                exit(1)
        else:
            direct_args.append(arg)
        i += 1
    return mode, options, direct_args

def is_wesword(word):
    return word.startswith('[') and word.endswith(']')

    
# ---- main ----
import sys

def main():
    global USE_FIRST_CONSONANT, COMPARE_LEADING_PHONEMES, WORD_WEIGHTS
    mode, options, args = parse_args(sys.argv[1:])
    USE_FIRST_CONSONANT = options["use-first-consonant"]
    COMPARE_LEADING_PHONEMES = True #options["compare-leading-phonemes"]
    WORD_WEIGHTS = WORD_WEIGHTS_RHYME_SOFT
    
    if mode == "pronounce":
        assert len(args) == 1
        inword = args[0]
        if not inword in WORD_TO_PHONE:
            print("didnt find "+inword)
            exit()
        phone = WORD_TO_PHONE[inword]
        print(phone + " " + to_mine(phone))

    elif mode == "distance":
        assert len(args) == 2
        w1 = args[0]
        w2 = args[1]
        print(word_distance(w1, w2))

    elif mode == "rhyme":
        assert len(args) == 1
        inword = args[0]
        if is_wesword(inword):
            inword = inword[1:-1]
            distances = [[w, wesword_distance(inword, w)] for w in WORDS]
        else:
            distances = [[w, word_distance(inword, w)] for w in WORDS]
        distances.sort(key=lambda x: x[1])
        for i in range(options["number"]):
            print(distances[i][0])
        
main()

# TODO: account for emphasis

"""
a = to_cv_list(inword)
b = to_cv_list("maple")
print(a)
print(b)
print(cv_list_distance(a,b, WORD_WEIGHTS_RHYME))

print(to_ph_list(inword))
print(to_cv_list(inword))      
for ph in to_ph_list(inword):
    print(PHONEME_TO_VEC[ph])

for q in to_cv_list(inword):
    if isinstance(q, list):
        dist = consonant_distance(q, ['m'])
        print(str(q) + "  " + str(dist))
        

"""
