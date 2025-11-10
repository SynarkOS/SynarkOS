import numpy as np
from scipy.stats import laplace

class AdaptiveDP:
    def __init__(self, epsilon=1.0, delta=1e-5, sensitivity=1.0):
        self.epsilon = epsilon
        self.delta = delta
        self.sensitivity = sensitivity
        
    def apply_gaussian(self, gradients):
        sigma = np.sqrt(2 * np.log(1.25/self.delta)) * self.sensitivity / self.epsilon
        return [g + np.random.normal(0, sigma) for g in gradients]
    
    def apply_laplacian(self, gradients):
        scale = self.sensitivity / self.epsilon
        return [g + laplace.rvs(scale=scale) for g in gradients]
    
    def adaptive_clip(self, gradients, percentile=90):
        clip_value = np.percentile([np.linalg.norm(g) for g in gradients], percentile)
        return [np.clip(g, -clip_value, clip_value) for g in gradients]