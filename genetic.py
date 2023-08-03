import pandas as pd
import random


def selection(population,Np):
	df  = pd.DataFrame(population,index = ['Rating','Genome'])
	df = df.transpose()
	df.index.name = 'Individual'
	print(df)

	df = df.sort_values(by='Rating',ascending = False)
	print('sorted')
	print(df)
	Np_num = int((Np/100) * len(df))
	top_Np = df.iloc[:Np_num,1]

	print('Individuals selected for next generation')
	print(top_Np)

	no_of_pairs = int(len(top_Np)/2)
	print('No. of pairs:',no_of_pairs)
	mating_pool = []
	for i in range(0,no_of_pairs,2):
		mating_pool.append( [ top_Np[top_Np.index[i]],top_Np[top_Np.index[i+1]] ] )



	return mating_pool
	
def crossover(mating_pool):
	new_generation = []
	for pair in mating_pool:
		print(pair)
		parent1 = pair[0]
		parent2 = pair[1]
		print('parent 1: ',parent1)
		print('parent 2: ',parent2)
		offspring1 = ''
		offspring2 = ''

		for i in range(0,len(parent1),4):
			gene1 = parent1[i:i+4]
			gene2 = parent2[i:i+4]
			print(gene1)
			print(gene2)
			print('-----')

			k  = random.randrange(0,4)
			print('k:',k)
			sub_gene_1_1 = gene1[0:k]
			sub_gene_1_2 = gene1[k:]
			sub_gene_2_1 = gene2[0:k]
			sub_gene_2_2 = gene2[k:]

			new_gene_1 = sub_gene_1_1 + sub_gene_2_2
			new_gene_2 = sub_gene_2_1 + sub_gene_1_2

			print('####')
			print('new gene1: ',new_gene_1)
			print('new gene2: ',new_gene_2)
			print('')

			offspring1 = offspring1 + new_gene_1
			offspring2 = offspring2 + new_gene_2
		print('new offspring1: ',offspring1)
		print('new offspring2: ',offspring2)

		new_generation.append(offspring1)
		new_generation.append(offspring2)
	return new_generation




if __name__ == '__main__':
	parent1 = '1111000001011000'
	parent2 = '1110101001011011'

	mating_pool =[[parent1,parent2]]

	new_generation = crossover(mating_pool)
	print(new_generation)


