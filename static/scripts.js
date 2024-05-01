// Initialization
const form = document.getElementById('stockForm');
const stockInput = document.getElementById('stockname');
const clearButton = document.querySelector('.clear');

// Function to handle form submission
function handleFormSubmit(event) {
    event.preventDefault();
    // Insert HTML into .shownavbar
    document.querySelector('.shownavbar').innerHTML = `
    <div class="divider-line"></div> 
        <div class="subnavbar">
            <a href="#" id="companyOutlook">Company Outlook</a>
            <a href="#" id="stockSummaryLink">Stock Summary</a>
            <a href="#" id="charts">Charts</a>
            <a href="#" id="latestNews">Latest News</a>
        </div>
        
        <div class="companydetails" id="companyDetails"></div>
        <div class="stocksummary" id="stockSummary"></div>
        <div class="chartcontainer" id="chartContainer"></div>
    `;
    // You can fetch data or perform other actions here if needed
}

// Function to handle click on "Company Outlook" link
function handleCompanyOutlookClick(event) {
    event.preventDefault();
    document.querySelector('.companydetails').innerHTML = `
        <table>
            <tr>
                <th>Company Name</th>
                <td id="companyName">Loading...</td>
            </tr>
            <tr>
                <th>Stock Ticker Symbol</th>
                <td id="tickerSymbol">Loading...</td>
            </tr>
            <tr>
                <th>Stock Exchange Code</th>
                <td id="exchangeCode">Loading...</td>
            </tr>
            <tr>
                <th>Company Start Date</th>
                <td id="startDate">Loading...</td>
            </tr>
            <tr>
                <th>Description</th>
                <td id="description">Loading...</td>
            </tr>
        </table>
    `;
}

// Function to handle click on "Stock Summary" link
function handleStockSummaryClick(event) {
    event.preventDefault();
    document.querySelector('.companydetails').innerHTML = `
        <table>
            <tr>
                <th>Stock Ticker Symbol</th>
                <td id="tickerSymbol">Loading...</td>
            </tr>
            <tr>
                <th>Trading Day</th>
                <td id="tradingDay">Loading...</td>
            </tr>
            <tr>
                <th>Previous Closing Price</th>
                <td id="prevClose">Loading...</td>
            </tr>
            <tr>
                <th>Opening Price</th>
                <td id="open">Loading...</td>
            </tr>
            <tr>
                <th>High Price</th>
                <td id="high">Loading...</td>
            </tr>
            <tr>
                <th>Low Price</th>
                <td id="low">Loading...</td>
            </tr>
            <tr>
                <th>Last Price</th>
                <td id="last">Loading...</td>
            </tr>
            <tr>
                <th>Change</th>
                <td id="change">Loading...</td>
            </tr>
            <tr>
                <th>Change Percent</th>
                <td id="changePercent">Loading...</td>
            </tr>
            <tr>
                <th>Number of Shares Traded</th>
                <td id="volume">Loading...</td>
            </tr>
        </table>
    `;
}

// Event listener for "Stock Summary" link



// Function to clear the input field
function clearInputField(event) {
    stockInput.value = '';
    document.querySelector('.shownavbar').innerHTML = '';
}

// Event Listeners
document.addEventListener('DOMContentLoaded', function() {
    form.addEventListener('submit', handleFormSubmit);
    clearButton.addEventListener('click', clearInputField);
    
    // Event delegation for companyOutlook link
    document.addEventListener('click', function(event) {
        if (event.target.id === 'companyOutlook') {
            handleCompanyOutlookClick(event);
        }
    });
    document.addEventListener('click', function(event) {
        if (event.target.id === 'stockSummaryLink') {
            handleStockSummaryClick(event);
        }
    });
   
});
