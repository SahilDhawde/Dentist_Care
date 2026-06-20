def predict(data):
 return {'cariesRisk':40 if data.get('caries') else 10,'gingivitisRisk':60 if data.get('bleeding') else 20}
