
# Neighborhood Blending

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/p)




Generally, the embedding used for any task is already pre-trained and generalized. However, for a specific task, Neighborhood Blending/mixing can be used. Here, we try to use the fact that a specific query/instance is primarily affected by its nearest neighbors only. Neighborhood Blending is a general technique and can be used in text data with pre-trained embedding or on images data.
After the queries get encoded using any sentence transformer model and using [*Facebook AI Similarity Search (FAISS)*](https://github.com/facebookresearch/faiss) to search for the similar embedding of multimedia documents, we obtained the top k nearest neighbors (in terms of similarity) of each given query.

Neighborhood Blending is used to make similar queries more distinct and closer to their neighbors. It makes the clusters more coherent. 


Official repository: 
https://github.com/sonisanskar/Neighborhood-Blending

# Features
- Cross-platform: Windows, Mac, and Linux are officially supported.
- Works with Python  2.7,3.5,3.6,3.7
# Requires
- numpy, pandas , faiss-cpu or faiss-gpu
## Acknowledgements

 - [FAISS](https://github.com/facebookresearch/faiss)
 
## Authors

- [@sonisanskar](https://github.com/sonisanskar)


## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sanskar-soni-6337a1196/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/sanskar75030473)


## Support

For support, email soni.sanskar@gmail.com 

