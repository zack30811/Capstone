#Other code
import Dolphin

# Reinforcement learning
from stable_baselines3 import PPO

# Environment
import gymnasium as gym
from gymnasium import spaces

# Image processing
import cv2
import numpy as np

def main():
    device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
    print(f"Using {device} device")

    model = NeuralNetwork().to(device)
    print(model)



if __name__ == "__main__":
    main()