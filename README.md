A statistical mechanics approach to de-biasing and uncertainty estimation in LASSO for random measurements
===


![image_of_debiased_estimator](https://takashi-takahashi.github.io/sandbox/debiased_estimator.png)

# overview 
* In high-dimensional statistical inference in which the number of parameters to be estimated is larger than that of the holding data, regularized linear estimation techniques are widely used. These techniques have, however, some drawbacks. 

    1. Estimators are biased in the sense that their absolute values are shrunk toward zero because of the regularization effect. 
    2. Their statistical properties are difficult to characterize as they are given as numerical solutions to certain optimization problems.

* In [our paper]((https://arxiv.org/abs/1803.09927)), we tackle such problems concerning LASSO, which is a widely used method for sparse linear estimation, when the measurement matrix is regarded as a sample from a rotationally invariant ensemble. We develop a new computationally feasible scheme to construct a de-biased estimator with a confidence interval.

* This repository provides a demonstration code for a construction of de-biased estimator.  
    * See [jupyter notebook](https://github.com/takashi-takahashi/debiasing_lasso_demo/blob/master/demonstration.ipynb) for demo. 


# requirements

* Python 3 and following Python modules are required to run demonstration notebook 
    * numpy
    * scipy
    * matplotlib
    * sklearn


# paper 
* T.Takahashi and Y. Kabashima, 
["A statistical mechanics approach to de-biasing and uncertainty estimation in LASSO for random measurements",](https://arxiv.org/abs/1803.09927) 

# people
* [Takashi Takahashi](https://takashi-takahashi.github.io/)
* [Yoshiyuki Kabashima](http://www.sp.dis.titech.ac.jp/~kaba/index_e.html)