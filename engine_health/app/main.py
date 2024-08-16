from fastapi import FastAPI, Depends, Security, HTTPException
# import pickle
import mlflow

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.base import TransformerMixin, BaseEstimator

app = FastAPI()


@app.on_event("startup")
def load_model():

    global loaded_model

    # with open("../../model/model.pickle", "rb") as openfile:
    #     model1 = pickle.load(openfile)
    model_uri = ''
    loaded_model = mlflow.pyfunc.load_model(model_uri)


@app.get("/health")
async def root():
    return {"message": "Hello World"}


@app.get("/predict")
async def root():
    X_test, y_test = get_test_data()
    predictions = loaded_model.predict(X_test)
    
    return {
        "actual_class": y_test[:4],
        "predicted_class": predictions[:4]
        }
    
    
def get_test_data():
    engine_df = pd.read_csv("./../data/interim/engine_data_w_efficiency_downsampled.csv")
    
    X = engine_df.drop("Engine Condition", axis=1)
    y = engine_df["Engine Condition"]
    
    prep_pipe = Pipeline([
        ("attr_adder", AttributesAdder()),
        ("std_scaler", StandardScaler())
    ])
    
    data_prepared = prep_pipe.fit_transform(X.values)
    X_train, X_test, y_train, y_test = train_test_split(
        data_prepared, y, 
        test_size=0.2, 
        random_state=SEED,
        stratify=y
    )
    return X_test, y_test
    
    


class AttributesAdder(BaseEstimator, TransformerMixin):
    rpm_idx, oil_pressure_idx, coolant_pressure_idx, oil_temp_idx, coolant_temp_idx = 0, 1, 3, 4, 5
    
    # Constructor of the Class
    def __init__(self, add_oil_system=True, add_coolant_system=True):
        self.add_oil_system = add_oil_system
        self.add_coolant_system = add_coolant_system
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        if self.add_oil_system:
            oil_efficiency = 1 / (X[:, rpm_idx] * X[:, oil_temp_idx])
            X = np.c_[X, oil_efficiency]
            
        if self.add_coolant_system:
            cool_efficiency = (1 / X[:, rpm_idx]) * X[:, coolant_temp_idx]
            X = np.c_[X, cool_efficiency]
            
        return X  