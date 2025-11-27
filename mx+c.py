import numpy as np
import matplotlib.pyplot as plt
import torch
from torch import nn


np.random.seed(42)

true_slope = 3.5
true_intercept = 1.2

l = 100
x = np.random.randn(l)
y = true_slope * x + true_intercept + np.random.randn(l)

a = np.random.randn()
b = np.random.randn()
learning_rate = 0.1
n_iterations = 200
loss_history = []

for i in range(n_iterations):
    y_pred = a * x + b
    error = y_pred - y
    loss = np.mean(error ** 2)
    loss_history.append(loss)
    grad_a = 2 * np.mean(error * x)
    grad_b = 2 * np.mean(error)
    a = a - learning_rate * grad_a
    b = b - learning_rate * grad_b
    if i % 10 == 0:
        print(f"NumPy Iteration {i}: loss = {loss:.4f}, slope = {a:.4f}, intercept = {b:.4f}")


plt.figure(figsize=(12,5))

plt.subplot(1, 2, 1)
plt.scatter(x, y, color='blue', label='Data')
plt.plot(x, y_pred, color='red', label='Fitted Line')
plt.title("NumPy Linear Regression Line")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(loss_history, color='green', label='Loss')
plt.title("NumPy Loss Curve")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.legend()

plt.tight_layout()
plt.show()

torch.manual_seed(42)


X_train = torch.tensor(x[:80].reshape(-1,1), dtype=torch.float32)
Y_train = torch.tensor(y[:80].reshape(-1,1), dtype=torch.float32)
X_test = torch.tensor(x[80:].reshape(-1,1), dtype=torch.float32)
Y_test = torch.tensor(y[80:].reshape(-1,1), dtype=torch.float32)


class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(1))
        self.bias = nn.Parameter(torch.randn(1))
    def forward(self, x):
        return self.weight * x + self.bias

model = LinearRegressionModel()
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

epochs = 200
epoch_count = []
loss_values = []
test_loss_values = []

for epoch in range(epochs):
    model.train()
    y_preds = model(X_train)
    loss = loss_fn(y_preds, Y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

  
    model.eval()
    with torch.no_grad():
        test_preds = model(X_test)
        test_loss = loss_fn(test_preds, Y_test)

  
    if epoch % 10 == 0:
        epoch_count.append(epoch)
        loss_values.append(loss.item())
        test_loss_values.append(test_loss.item())
        print(f"PyTorch Epoch {epoch}: Train Loss = {loss.item():.4f}, Test Loss = {test_loss.item():.4f}")


plt.figure(figsize=(12,5))


plt.subplot(1,2,1)
plt.plot(epoch_count, loss_values, label='Train Loss')
plt.plot(epoch_count, test_loss_values, label='Test Loss')
plt.title("PyTorch Training/Test Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()


plt.subplot(1,2,2)
with torch.no_grad():
    X_all = torch.tensor(x.reshape(-1,1), dtype=torch.float32)
    Y_pred_all = model(X_all)
plt.scatter(x, y, color='blue', label='Data')
plt.plot(X_all.numpy(), Y_pred_all.numpy(), color='red', label='Fitted Line')
plt.title("PyTorch Linear Regression Fit")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()

plt.tight_layout()
plt.show()

print(f"PyTorch Learned weight: {model.weight.item():.4f}")
print(f"PyTorch Learned bias: {model.bias.item():.4f}")
