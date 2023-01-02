import numpy as np
from numpy.linalg import eigvals

def run_experiment(n=100):
	k = 100
	results = []
	for _ in range(n):
		mat = np.random.rand(k,k)
		max_eig = np.abs(eigvals(mat)).max()
		results.append(max_eig)
	return results
some_results = run_experiment()
print('Largest {}'.format(np.max(some_results)))
	 
