import os
import pytest
import json
from datetime import datetime

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    print("Setting Reports Pattern...")
    # Add Timestamp to the Report File
    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"

@pytest.fixture(scope="session",autouse=True)
def setup_teardown():
    print("\nSetting Up Resources...")
    yield
    print("\nTearing Down Resources...")

@pytest.fixture
def load_user_data():
    print("Loading Data for use...")
    try:       
        json_file_path = os.path.join(os.path.dirname(__file__),"data","test_data.json")
        with open(json_file_path) as json_file:
            user_data = json.load(json_file)

        print("\nInput Data :: ",user_data,type(user_data))

    except Exception as Error:
        print("Error in Loading the Users Data")
        user_data = {}

    return user_data
