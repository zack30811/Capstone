#Other code
import Dolphin

# Machine learning
import torch
import torch.nn as nn
import torch.optim as optim

# Reinforcement learning
from stable_baselines3 import PPO

# Environment
import gymnasium as gym
from gymnasium import spaces

# Image processing
import cv2
import numpy as np

class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

def main():
    device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
    print(f"Using {device} device")

    model = NeuralNetwork().to(device)
    print(model)

    Dolphin.main()


if __name__ == "__main__":
    main()