# A quantum variational approach to data classification:<br>current Quantum Computers maturity and the potential for Quantum Advantage 

### Team Name: 

Q-Reply

### Project Description: 

In the latest years more and more attention has been drawn to the application of Quantum Computing to Machine Learning. Classical computers are often able to provide high quality solutions, thus enabling businesses to benefit from data-driven and automated approaches. However, if even better results were at hand the profits would be higher and in some situations classical Machine Learning may not be able to provide sufficiently good results at all. For these reasons, the search for higher quality solutions is endless. 

In this framework, Quantum Computing sets itself as a major potential game-changer, opening up a number of possibilities to obtain improved performances when compared to existing classical techniques. This new field, called Quantum Machine Learning, is still in its infancy: Quantum Computers are currently undergoing major engineering improvements and it is not yet clear how and when Machine Learning could benefit from Quantum Computing. 

In this work we extensively explore the well-known (in the Quantum Computing Community!) variational approach for data classification. We analyse the dataset of interest and investigate the impact of different strategies, namely the ansatz and the depth of the Quantum Circuit, with a two-fold goal: 

* Test empirically if the Quantum Computing strategy is able to perform better than classical techniques – Quantum Advantage 
* Investigate whether the fidelity of gates operations and coherence times are sufficiently high for current Quantum Computers to be employed in real or near-real applications 

To do so, we derive most of the results on a simulator, select a strategy and finally run it on Rigetti’s Quantum Processing Unit (QPU). 

### Presentation: 

https://github.com/ivang/QHack-Q-Reply-2021/submission.ipynb

### Source code: 

https://github.com/ivang/QHack-Q-Reply-2021

### Details

* Datasets *

How: look for open dataset with classical benchmarks (this one)
https://archive.ics.uci.edu/ml/datasets/Rice+%28Cammeo+and+Osmancik%29


* Lessons learned *

The scaling of features count. For example, with a BasicEntanglerLayers the classifier shows two cycles in the range (-6,6), but scaling the features to double the value reduces the number of cycles to 1. This can lead to better accuracy.

Make GIF or pictures to show this?

* Effects on the performance *

* Operations in the circuit (e.g. only X rotations don't introduce much entanglement)
* Postprocessing and loss function (e.g. linear transformation + squareloss; sigmoid + logloss)
* Feature scaling (this affect the periodicity of the decision boundaries)
