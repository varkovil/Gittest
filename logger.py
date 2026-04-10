# logger.py — Arjun's work
# Log every prediction made by the fraud model
import datetime
def log_prediction(transaction_id, prediction, confidence):
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log = f"[{timestamp}] TXN: {transaction_id} | Result: {prediction} | Confidence: {confidence:.1f}%"
print(log)
return log
# Test
log_prediction("TXN001", "FRAUD", 92.5)
log_prediction("TXN002", "LEGITIMATE", 98.1)