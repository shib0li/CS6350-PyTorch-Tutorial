# CS6350-PyTorch-Tutorial

This is the repository of the Pytorch tutorial of Fall 2021 CS5350,CS6350 Machine Learning Course.

## Env

We recommend using **conda** to install Pytorch, details how to use conda can be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). Using **conda** to manage enviroments is easy. Basically, in three steps

1.create an enviroment
```
conda create --name=(your_env_name)
```
2.active your enviroment
```
conda activate (your_env_name)
```
3.install the package required
```
conda/pip install (pkg_names)
```

## Install PyTorch

To intall Pytorch with latetest cuda support(Linux only)
```
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
```
With CPU support only for all platforms
```
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```
[Other install options](https://pytorch.org/get-started/locally/)

## Roadmap

1.**Basics**:\
Examples of using autograd, *backward()* and *autograd.grad()* to compute high-order derivatives. Concepts of Pytorch *Dataset* and *Dataloader* and how to customize *Datasets* with your own data

2.**nn.Module**:\
Basic building blocks of models, use Pytorch exsiting moduels to build linear regressors and neural net regressors

3.**torch.optim**:\
More about Pytorch optimization modules such as scheduling and second-order optimizers

4.**Customize nn.Module**:\
How to implement and reuse your own nn moduels as building blocks: examples such as *Polynomial and Logistic regression*

5.**ConvNet for Cifar10**:\
A step-by-step example of using Pytorch to build a convolutional neural network and train it on [CIFAR10](https://www.cs.toronto.edu/~kriz/cifar.html)



