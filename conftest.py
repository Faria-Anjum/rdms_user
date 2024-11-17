import pytest
from datetime import datetime

#all test functions in a test file run on the same browser context
@pytest.fixture(scope="module")
def page(browser):
    page = browser.new_page()
    return page

#customizing html report
def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Description</th>")
    #cells.insert(1, '<th class="sortable time" data-column-type="time">Time</th>')

def pytest_html_results_table_row(report, cells):
    cells.insert(2, f"<td>{report.description}</td>")
    #cells.insert(1, f'<td class="col-time">{datetime.now()}</td>')

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)

#setting viewport
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

@pytest.fixture
def readUserIndx():
    with open(r"files\username_index.txt",'r') as f:
        st = int(f.read())
    return st

@pytest.fixture
def readBulkUserID():
    with open(r"files\bulkuser_id.txt",'r') as f:
        st = int(f.read())
    return str(st)

@pytest.fixture
def readProductID():
    with open(r"files\product_id.txt",'r') as f:
        st = int(f.read())
    return str(st)

@pytest.fixture
def readProductTypeCode():
    with open(r"files\product_type.txt",'r') as f:
        st = int(f.read())
    return str(st)

@pytest.fixture
def readCategoryCode():
    with open(r"files\product_category.txt",'r') as f:
        st = int(f.read())
    return str(st)

@pytest.fixture
def readSubTypeCode():
    with open(r"files\product_subtype.txt",'r') as f:
        st = int(f.read())
    return str(st)

@pytest.fixture(scope="session")
def today():
    today = datetime.now()

    year = today.year
    month = today.month
    day = today.day

    if len(str(today.day))==1:
        day = "0"+str(day)
    if len(str(today.month))==1:
        month = "0"+str(month)

    day = f'{year}-{month}-{day}'
    return day

@pytest.fixture(scope="session")
def tomorrow():
    today = datetime.now()

    if today.day in [28,29,30,31]:
        if today.month == 12:
            month = 1
            year = today.year + 1
        else:
            month = today.month + 1
            year = today.year
        day = 1
    else:
        year = today.year
        month = today.month
        day = today.day + 1

    if len(str(today.day))==1:
        day = "0"+str(day)
    if len(str(today.month))==1:
        month = "0"+str(month)

    day = f'{year}-{month}-{day}'
    return day