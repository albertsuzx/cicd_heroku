from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to EC-fastapi-pipeline"}


def test_unit_test():
    to_predict_dict = {'id': 'se0001',
                       'UC_NoInqMain': 1,
                       'OverCycle_amt_Min6mth': -3500,
                       'MostRecentApp_No_Grp': '10 Plus',
                       'UC_LandVal_Grp': 'Missing',
                       'RemainingLoanPct_Grp': '65 to 93',
                       'Rem2Month_flag_MonthsSince_Grp': '3 to 5'}

    response = client.post("/predict", json=to_predict_dict)
    assert response.status_code == 200
    assert response.json() == {'prediction': {'prob': 0.4076874630362837}}
