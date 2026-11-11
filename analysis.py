from pathlib import Path
import pandas as pd,sqlite3,matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,roc_auc_score,ConfusionMatrixDisplay
p=Path(__file__).resolve().parent;d=pd.read_csv(p/'data/sample_data.csv');(p/'outputs').mkdir(exist_ok=True)
X=d.drop(columns=['customer_id','churned']);y=d.churned
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,stratify=y,random_state=42)
prep=ColumnTransformer([('num',StandardScaler(),['tenure_months','monthly_charges','support_tickets_90d','autopay']),('cat',OneHotEncoder(handle_unknown='ignore'),['contract_type'])]);models={'logistic_regression':LogisticRegression(max_iter=1000,random_state=42),'random_forest':RandomForestClassifier(n_estimators=150,min_samples_leaf=5,random_state=42)}
metrics=[];best=None;best_auc=-1
for name,model in models.items():
 pipe=Pipeline([('preprocess',prep),('model',model)]);pipe.fit(Xtr,ytr);pred=pipe.predict(Xte);scores=pipe.predict_proba(Xte)[:,1];auc=roc_auc_score(yte,scores)
 metrics.append([name,accuracy_score(yte,pred),precision_score(yte,pred,zero_division=0),recall_score(yte,pred),f1_score(yte,pred),auc]);
 if auc>best_auc:best_auc=auc;best=(name,pipe,pred,scores)
base=int(ytr.mean()>=.5);metrics.append(['majority_baseline',accuracy_score(yte,[base]*len(yte)),precision_score(yte,[base]*len(yte),zero_division=0),recall_score(yte,[base]*len(yte)),f1_score(yte,[base]*len(yte)),.5])
pd.DataFrame(metrics,columns=['model','accuracy','precision','recall','f1','roc_auc']).to_csv(p/'outputs/model_metrics.csv',index=False)
pd.DataFrame({'actual':yte.to_numpy(),'predicted':best[2],'churn_probability':best[3]}).to_csv(p/'outputs/test_predictions.csv',index=False)
ConfusionMatrixDisplay.from_predictions(yte,best[2]);plt.title('Test-set Confusion Matrix: '+best[0]);plt.tight_layout();plt.savefig(p/'figures/confusion_matrix.png');plt.close()
with sqlite3.connect(p/'outputs/churn.db') as con:d.to_sql('customers',con,if_exists='replace',index=False)
print(pd.read_csv(p/'outputs/model_metrics.csv').to_string(index=False))
