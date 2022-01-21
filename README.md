
# Neighborhood Blending

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/p)
![PyPI - License](https://img.shields.io/pypi/l/NeighborBlend)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/NeighborBlend)



Generally, the embedding used for any task is already pre-trained and generalized. However, for a specific task, Neighborhood Blending/mixing can be used. Here, we try to use the fact that a specific query/instance is primarily affected by its nearest neighbors only. Neighborhood Blending is a general technique and can be used in text data with pre-trained embedding or on images data.
After the queries get encoded using any sentence transformer model and using [*Facebook AI Similarity Search (FAISS)*](https://github.com/facebookresearch/faiss) to search for the similar embedding of multimedia documents, we obtained the top k nearest neighbors (in terms of similarity) of each given query.

Neighborhood Blending is used to make similar queries more distinct and closer to their neighbors. It makes the clusters more coherent. 


Official repository: 
https://github.com/sonisanskar/Neighborhood-Blending

## Features
- Cross-platform: Windows, Mac, and Linux are officially supported.
- Works with Python 3.7, 3.8, 3.9

## Requires
- numpy, pandas , faiss-cpu,and scikit-learn

## Installation
We recommend using Python 3.5 or higher.
\
\
**Install with pip**\
Install the NeighborBlend using **`pip`**

```bash
  pip install NeighborBlend
```
## Getting Started
First we list down all the functions which can be leveraged by the user

**Function1**

```bash
  # Funct1 : neighborhood_search(emb,thresh,k_neighbors)

  '''
  Finds the neighbors of all samples embeddings above a given threshold 
  '''
  # Params
  '''
  emb: 2D matrix of embeddings
  thresh : float value of similarity above which we want neighbors
  k_neighbors: Number of neighbors which need to be considered for thresholding
  '''
  # Return
  '''
  match_index_lst: Dictionary with matching indexes
  similarities_lst: Similarities scores corresponding to above indexes
  '''
```

**Function2**
```bash
  # Funct2 :blend_neighborhood(emb, match_index_lst, similarities_lst)
  '''
  Performs weighted average and normalization of embeddings
  with the simialrity scores of its neighbors
  '''
  # Params
  '''
  emb: 2D matrix of embeddings
  match_index_lst: Dictionary with matching indexes
  similarities_lst: Similarities scores corresponding to above indexes
  '''
  # Return
  '''
  updated_embedding: Embedding obtained after weighted average
  '''
```

**Function3**
```bash
  # Funct3 :iterative_neighborhood_blending(emb, threshes,k_neighbors):
  '''
  Finds the neighbors of all samples embeddings above a given threshold and weighted average of the samles
  '''
  # Params
  '''
  emb: 2D matrix of embeddings
  threshes: a list of thresholds applied iteratively
  k_neighbors: number of neighbors to be considered
  '''
  # Return
  '''
  updated_embedding: Embedding obtained after weighted average
  match_index_lst
  similarities_lst
  '''
```





## Example Usage

````python
from NeighborBlend import*
import NeighborBlend
#Func 1
match_index_lst, similarities_lst = neighborhood_search(emb, thresh,k_neighbors)

Func3 is used for iteratively finding its neighbors and the dropping and updating
````
Func3 is used for the final updation of embeddings

````python
#Func 3
updated_emb,match_lst, simi_lst = iterative_neighborhood_blending(emb, threshes,k_neighbors)

````


## Acknowledgements

 - [FAISS](https://github.com/facebookresearch/faiss)
 
## Authors

- [@sonisanskar](https://github.com/sonisanskar)


## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sanskar-soni-6337a1196/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/sanskar75030473)


## Support

For support, email soni.sanskar@gmail.com 

