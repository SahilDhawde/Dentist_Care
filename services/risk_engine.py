def calculate_score(data):
 score=100
 if data.get('smoker'): score-=15
 if data.get('diabetes'): score-=10
 if data.get('bleeding'): score-=15
 if data.get('caries'): score-=10
 return max(score,0)
