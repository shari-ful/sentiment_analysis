from setfit import SetFitModel

pred_label = ["Negetive","Positive","Neutral"]
# Download from Hub and run inference
model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")


print("prediction")
# Run inference
preds = model(["the trial should be held on neutral ground"])

prediction = pred_label[preds]

print(prediction)