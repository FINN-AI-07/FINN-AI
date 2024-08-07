import torch
import torch.nn as nn

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()  # Define ReLU activation function
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)  # Apply ReLU activation
        out = self.l2(out)
        out = self.relu(out)  # Apply ReLU activation again
        out = self.l3(out)

        # Note: Typically, for multi-class classification, you would apply softmax here
        # However, if using nn.CrossEntropyLoss, softmax is included in the loss function
        return out
