import torch
import torch.nn as nn


class DetectEdge(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super(DetectEdge, self).__init__()
        self.linear1 = nn.Linear(512*512, 128)
        self.conv1 = nn.Conv2d(1, 64, 3, 1, 1)
        self.conv2 = nn.Conv2d(64, 128, 3, 1, 1)
        self.conv3 = nn.Conv2d(128, 256, 3, 1, 1)
        self.conv4 = nn.Conv2d(256, 512, 3, 1, 1)
        self.linear2 = nn.Linear(512, 24)

    def forward(self, x):
        # Apply the first linear layer and ReLU activation
        x = nn.ReLU(self.linear1(x.view(x.size(0), -1)))
        
        # Reshape the data for the convolutional layers
        x = x.view(-1, 1, 512, 512)
        
        # Apply the convolutional layers and ReLU activation
        x = nn.ReLU(self.conv1(x))
        x = nn.ReLU(self.conv2(x))
        x = nn.ReLU(self.conv3(x))
        x = nn.ReLU(self.conv4(x))
        
        # Flatten the output for the final linear layer
        x = x.view(x.size(0), -1)
        
        # Apply the final linear layer
        x = self.linear2(x)
        
        # Reshape the output to the desired shape (12, 2)
        x = x.view(-1, 12, 2)
        
        return x
        