
import warnings
warnings.filterwarnings('ignore')

#Verisetinin alınması
import pandas as pd
data = pd.read_csv("../input/krediVeriseti.csv", delimiter = ";")

#Veriseti üzerinde düzenlemeler
data.evDurumu[data.evDurumu == 'evsahibi'] = 1
data.evDurumu[data.evDurumu == 'kiraci'] = 0

data.telefonDurumu[data.telefonDurumu == 'var'] = 1
data.telefonDurumu[data.telefonDurumu == 'yok'] = 0

data.KrediDurumu[data.KrediDurumu == 'krediver'] = True
data.KrediDurumu[data.KrediDurumu == 'verme'] = False

data= data.astype(float) 
# Veri setimizi okuyoruz
X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values
# Veri setini test ve eğitim olarak 2'ye ayırıyoruz.
from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

# eğitim setine Naive Bayes uyguluyoruz 
from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(x_train, y_train)
# Test veri setini kullanarak sonuçları tahmin ediyoruz
y_pred = nb.predict(x_test)

# Confusion matrisimizi oluşturuyoruz.
from sklearn.metrics import confusion_matrix,classification_report
cm = confusion_matrix(y_test, y_pred)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

nb.fit(X_train, y_train)

y_pred = nb.predict(X_test)

#Modelin kaydedilmesi
import pickle
pickle.dump(nb, open('Model.pkl','wb'))

