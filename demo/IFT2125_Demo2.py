
# coding: utf-8

# 
# # Algo des permutations
# ## IFT2125 - Demo 2 - Stephanie Larocque

# In[1]:


## Utils

################################################################################
# Note that the indices start at 0 while the permutations are from 1 to m
# This is why we add/substract 1 at some places in the utils
# Note also that the permutations are tuple
# If p = (1, 3, 5, 4, 2), it means that p(1)=1, p(2)=3, p(3)=5, p(4)=4, p(5)=2
# In the canonical notation p would be p=(235), and NOT 1-->3-->5-->4-->2
################################################################################

def product(p, q):
    # p, q : 2 permutations (we suppose valid permutations)
    # Product (left to right) of permutations p*q
    return tuple( [q[p[i]-1] for i in range(len(p))])
    
def inverse(p):
    # p : permutation
    # Output : its inverse
    return tuple( [p.index(i)+1 for i in range(1, len(p)+1) ]  )



# In[2]:


def sift(p, T):
    # input : p (permutation to sift) and T (table)
    # output : permutation q if new permutation inserted, otherwise None
    
    m = len(p)
    IDENTITY =tuple(range(1, m+1)) 
    
    while p!= IDENTITY:
        i = min(x for x in range(m) if p[x] != x+1)
        j = p[i]-1
        if T[i][j] == IDENTITY : 
            T[i][j] = p
            return p
        else:
            p = product(p, inverse(T[i][j])) 
    return None


# In[3]:


def appartenance_intelligent_n6(r, permutations):
    """L'algo n6: does r belong to the group generated by the set permutations?"""
    
    #raise Error if invalid permutations
    
    m = len(r)
    IDENTITY = tuple(range(1, m+1))
    T = [[IDENTITY] * m for _ in range(m)] # creates a mXm table T containing IDENTITY

    
    # pour assurer le tamisage des permutations en entrée
    to_sift = [(p) for p in permutations]
    
    # maintains set of table entries as a set
    entries = set()
    
    while len(to_sift) > 0:
        p = to_sift.pop()
        q = sift(p, T)

        if q is not None:
            entries.add(q)  
            # the product q*q is considered since we added q to entries
            to_sift.extend([(product(q,p)) for p in entries])
            to_sift.extend([(product(p,q)) for p in entries])

            
    # Genere r? / Generates r?
    return sift(r, T) is None




# In[4]:


p = tuple([3,2, 4, 5, 1])
permutations = { tuple([2,1,4,3,5]), tuple([2,3,4,5,1])}

print("p", p)
print("p1, p2, .., pk", permutations)
appartenance_intelligent_n6(p, permutations)

