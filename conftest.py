import pytest
import os

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
def readWriteUserIndx():
    with open(r"files\username_index.txt",'r') as f:
        st = int(f.read())
    with open(r"files\username_index.txt",'w') as f:
        nst = st + 1
        f.write(str(nst))
    return st

@pytest.fixture
def readUserIndx():
    with open(r"files\username_index.txt",'r') as f:
        st = int(f.read())
    return st