import sys, string

codes   = {}

def frequency (str) :
    freqs = {}
    for ch in str :
        freqs[ch] = freqs.get(ch,0) + 1
    return freqs

def sortFreq (freqs) :
    letters = freqs.keys()
    tuples = []
    for let in letters :
        tuples.append((freqs[let],let))
    tuples.sort()
    return tuples

def buildTree(tuples) :
    while len(tuples) > 1 :
        leastTwo = tuple(tuples[0:2])                  
        theRest  = tuples[2:]                          
        combFreq = leastTwo[0][0] + leastTwo[1][0]     
        tuples   = theRest + [(combFreq,leastTwo)]     
        tuples.sort()                                  
    return tuples[0]        

def trimTree (tree) :
     
    p = tree[1]                                   
    if type(p) == type("") : return p            
    else : return (trimTree(p[0]), trimTree(p[1]))

def assignCodes (node, pat='') :
    global codes
    if type(node) == type("") :
        codes[node] = pat               
    else  :                               
        assignCodes(node[0], pat+"0")    
        assignCodes(node[1], pat+"1")     

def encode (str) :
    global codes
    output = ""
    for ch in str : output += codes[ch]
    return output

def decode (tree, str) :
    output = ""
    p = tree
    for bit in str :
        if bit == '0' : p = p[0]     
        else          : p = p[1]    
        if type(p) == type("") :     
            output += p            
            p = tree                
    return output

def main () :
    debug = None
    str = sys.stdin.read()
    freqs = frequency(str)
    tuples = sortFreq(freqs)

    tree = buildTree(tuples)
    if debug : print "Built tree", tree

    tree = trimTree(tree)
    if debug : print "Trimmed tree", tree

    assignCodes(tree)
    if debug : showCodes()

    small = encode(str)
    original = decode (tree, small)
    print "Original text length", len(str)
    print "Requires %d bits. (%d bytes)" % (len(small), (len(small)+7)/8)
    print "Restored matches original", str == original
    print "Code for space is ", codes[' ']
    print "Code for letter e ", codes['e']
    print "Code for letter y ", codes['y']
    print "Code for letter z ", codes['z']

if __name__ == "__main__" : main()

