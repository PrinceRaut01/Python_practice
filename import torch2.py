import torch
from torch import nn
import matplotlib.pyplot as plt

# --- Random seed ---
torch.manual_seed(42)

# --- Data ---
X_train = torch.arange(0, 8, 0.1).unsqueeze(1)       # Training data
Y_train = 0.7 * X_train + 0.3 + 0.5 * torch.randn_like(X_train)

X_test = torch.arange(8, 10, 0.1).unsqueeze(1)      # Test data
Y_test = 0.7 * X_test + 0.3 + 0.5 * torch.randn_like(X_test)

# --- Model ---
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(1))
        self.bias = nn.Parameter(torch.randn(1))
    
    def forward(self, x):
        return self.weight * x + self.bias

model = LinearRegressionModel()

# --- Loss and optimizer ---
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# --- Training setup ---
epochs = 200
epoch_count = []
loss_values = []
test_loss_values = []

# --- Training Loop ---
for epoch in range(epochs):
    model.train()  # training mode

    # Forward pass (train)
    y_preds = model(X_train)
    loss = loss_fn(y_preds, Y_train)

    # Backpropagation
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Test (evaluation)
    model.eval()
    with torch.no_grad():
        test_preds = model(X_test)
        test_loss = loss_fn(test_preds, Y_test)

    # Track losses every 10 epochs
    if epoch % 10 == 0:
        epoch_count.append(epoch)
        loss_values.append(loss.item())
        test_loss_values.append(test_loss.item())
        print(f"Epoch {epoch}: Train Loss = {loss.item():.4f}, Test Loss = {test_loss.item():.4f}")

# --- Plot Training and Test Loss ---
plt.plot(epoch_count, loss_values, label="Train Loss")
plt.plot(epoch_count, test_loss_values, label="Test Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Training and Test Loss over Epochs")
plt.legend()
plt.show()

# --- Print learned parameters ---
print(f"Learned weight: {model.weight.item():.4f}")
print(f"Learned bias: {model.bias.item():.4f}")

# --- Plot predictions vs data ---
plt.scatter(X_train, Y_train, color='blue', label='Train Data')
plt.scatter(X_test, Y_test, color='orange', label='Test Data')
with torch.no_grad():
    X_all = torch.cat([X_train, X_test], dim=0)
    Y_all_pred = model(X_all)
plt.plot(X_all, Y_all_pred, color='red', label='Fitted Line')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression Fit")
plt.legend()
plt.show()
