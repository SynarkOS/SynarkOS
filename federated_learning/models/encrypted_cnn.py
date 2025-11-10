# federated_learning/models/encrypted_cnn.py  
import torch  
import tenseal as ts  

class EncryptedCNN:  
    def __init__(self, context):  
        self.context = context  
        self.conv1 = ts.encrypted_conv2d(context, in_channels=1, out_channels=32, kernel_size=3)  
        self.fc1 = ts.encrypted_linear(context, 32 * 26 * 26, 128)  
        self.fc2 = ts.encrypted_linear(context, 128, 10)  

    def forward(self, x):  
        x = ts.encrypted_relu(self.conv1(x))  
        x = ts.encrypted_flatten(x)  
        x = ts.encrypted_relu(self.fc1(x))  
        return self.fc2(x)  