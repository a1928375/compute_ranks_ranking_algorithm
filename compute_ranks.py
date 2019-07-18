graph={'http://udacity.com/cs101x/urank/kathleen.html': [], 'http://udacity.com/cs101x/urank/zinc.html': ['http://udacity.com/cs101x/urank/nickel.html', 'http://udacity.com/cs101x/urank/arsenic.html'], 'http://udacity.com/cs101x/urank/hummus.html': [], 'http://udacity.com/cs101x/urank/arsenic.html': ['http://udacity.com/cs101x/urank/nickel.html'], 'http://udacity.com/cs101x/urank/index.html': ['http://udacity.com/cs101x/urank/hummus.html', 'http://udacity.com/cs101x/urank/arsenic.html', 'http://udacity.com/cs101x/urank/kathleen.html', 'http://udacity.com/cs101x/urank/nickel.html', 'http://udacity.com/cs101x/urank/zinc.html'], 'http://udacity.com/cs101x/urank/nickel.html': ['http://udacity.com/cs101x/urank/kathleen.html']}

def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 1
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank=newrank+d*(ranks[node])/len(graph[node])   
            newranks[page] = newrank
        ranks = newranks
    return ranks

ranks = compute_ranks(graph)
print ranks
