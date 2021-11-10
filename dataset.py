import os, sys
import numpy as np
from torch.utils.data import Dataset, DataLoader

class SimpleDataset(Dataset):
    def __init__(self, X, y):
        super(SimpleDataset, self).__init__()
        self.X = X
        self.y = y
        
    def __getitem__(self, index):
        return self.X[index,:], self.y[index,:]

    def __len__(self,):
        return self.X.shape[0]
    
    
class BankNote(Dataset):
    def __init__(self, data_path, mode):
        
        super(BankNote, self).__init__()
        
        raw_tr = np.loadtxt(os.path.join(data_path, 'train.csv'), delimiter=',')
        raw_te = np.loadtxt(os.path.join(data_path, 'test.csv'), delimiter=',')
        
        Xtr, ytr, Xte, yte = \
            raw_tr[:,:-1], raw_tr[:,-1].reshape([-1,1]), raw_te[:,:-1], raw_te[:,-1].reshape([-1,1])
        
        if mode == 'train':
            self.X, self.y = Xtr, ytr
        elif mode == 'test':
            self.X, self.y = Xte, yte
        else:
            raise Exception("Error: Invalid mode option!")
        
    def __getitem__(self, index):
        
        return self.X[index,:], self.y[index,:]
    
    def __len__(self,):
        # Return total number of samples.
        return self.X.shape[0]