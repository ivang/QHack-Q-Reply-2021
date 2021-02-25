# Using NISQ devices right now: lights and shadows of variational approach for data classification

### Team Name: 

Q-Reply

### Project Description: 

Goal of the project - develop variational classifier to answer the following:
* Do we find a quantum advantage (higher accuracy)?
* Are we happy already today with the fidelity of gates or do we need to wait years also for variational approaches? (i.e. does the run on quantum hardware resembles the run on simulator? or does noise lead to completely different (worse?) solutions?)

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
