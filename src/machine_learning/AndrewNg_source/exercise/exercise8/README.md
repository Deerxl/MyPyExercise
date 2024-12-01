# Coursera - Machine Learning by Andrew Ng
https://www.coursera.org/learn/machine-learning

# Exercise 8: Anomaly Detection and Recommender Systems
In this exercise, you will implement the anomaly detection algorithm and
apply it to detect failing servers on a network. In the second part, you will
use collaborative filtering to build a recommender system for movies. Before
starting on the programming exercise, we strongly recommend watching the
video lectures and completing the review questions for the associated topics.
<br />
To get started with the exercise, you will need to download the starter
code and unzip its contents to the directory where you wish to complete the
exercise. If needed, use the cd command in Octave/MATLAB to change to
this directory before starting this exercise.
<br />
You can also find instructions for installing Octave/MATLAB in the 
Environment Setup Instructions" of the course website.
<br />
# Files included in this exercise
ex8.m - Octave/MATLAB script for first part of exercise<br />
ex8 cofi.m - Octave/MATLAB script for second part of exercise<br />
ex8data1.mat - First example Dataset for anomaly detection<br />
ex8data2.mat - Second example Dataset for anomaly detection<br />
ex8 movies.mat - Movie Review Dataset<br />
ex8 movieParams.mat - Parameters provided for debugging<br />
multivariateGaussian.m - Computes the probability density function
for a Gaussian distribution<br />
visualizeFit.m - 2D plot of a Gaussian distribution and a dataset<br />
checkCostFunction.m - Gradient checking for collaborative filtering<br />
computeNumericalGradient.m - Numerically compute gradients<br />
fmincg.m - Function minimization routine (similar to fminunc)<br />
loadMovieList.m - Loads the list of movies into a cell-array<br />
movie ids.txt - List of movies<br />
normalizeRatings.m - Mean normalization for collaborative filtering<br />
submit.m - Submission script that sends your solutions to our servers<br />
[?] estimateGaussian.m - Estimate the parameters of a Gaussian 
distribution with a diagonal covariance matrix<br />
[?] selectThreshold.m - Find a threshold for anomaly detection<br />
[?] cofiCostFunc.m - Implement the cost function for collaborative filtering<br />
? indicates files you will need to complete<br />
