import itertools
import matplotlib.pyplot as plt
import pandas as pd
import random

def get_coin_outcomes(n: int) -> int:
    return list(itertools.product(['H', 'T'], repeat=n))

assert len(get_coin_outcomes(6)) == 64

def fac(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
     
assert fac(6) == 720

def get_probability_table(n: int, method: str='fac') -> pd.DataFrame:
    
    assert method in ['count', 'fac'], 'method must be "count" or "fac"'
    
    count_heads = [int(i) for i in range(n+1)]
    
    if method=='count':
        outcomes = get_coin_outcomes(n)
        total_outcomes = len(outcomes)

        probabilities = []
        for count in count_heads:
            successes = 0
            for outcome in outcomes:
                if outcome.count('H') == count:
                    successes += 1
            probabilities.append(successes/total_outcomes)
    
    elif method=='fac':
        # p(h) = n!/h!(n-h)! * 2^-n
        
        modifier = pow(2, -n)
        fac_n = fac(n)
        
        probabilities = [(fac_n/(fac(count)*fac(n-count))*modifier)
                        for count in count_heads]
            
    return pd.DataFrame(
            {f'coutn_heads (n={n})' : count_heads,
             'probability' : probabilities}
        )

def get_binary_probability(n: int, h: int) -> float:
    '''p(h) = n!/h!(n-h)! * 2^-n'''
        
    return fac(n) / (fac(h)*fac(n-h)) * pow(2, -n)

assert round(get_binary_probability(50, 25), 2) == 0.11
        
    
    

