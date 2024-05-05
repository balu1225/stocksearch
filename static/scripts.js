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
    handleCompanyOutlookClick(event);
}

// Function to handle click on "Company Outlook" link
function handleCompanyOutlookClick(event) {
    event.preventDefault();
    const ticker = stockInput.value; // Get ticker from input field
    fetch(`/api/tiingo/${ticker}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            document.querySelector('.companydetails').innerHTML = `
                <table>
                    <tr>
                        <th>Company Name</th>
                        <td id="companyName">${data.name || 'N/A'}</td>
                    </tr>
                    <tr>
                        <th>Stock Ticker Symbol</th>
                        <td id="tickerSymbol">${data.ticker || 'N/A'}</td>
                    </tr>
                    <tr>
                        <th>Stock Exchange Code</th>
                        <td id="exchangeCode">${data.exchangeCode || 'N/A'}</td>
                    </tr>
                    <tr>
                        <th>Company Start Date</th>
                        <td id="startDate">${data.startDate || 'N/A'}</td>
                    </tr>
                    <tr>
                        <th>Description</th>
                        <td id="description">${data.description || 'N/A'}</td>
                    </tr>
                </table>
            `;
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
}

// Function to handle click on "Stock Summary" link
function handleStockSummaryClick(event) {
    event.preventDefault();
    const ticker = stockInput.value; // Assuming you want to use the ticker entered by the user

    fetch(`/api/iex/${ticker}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Ensure data is not empty and we have at least one object in the array
            if (data && data.length > 0) {
                const stock = data[0];
                document.querySelector('.companydetails').innerHTML = `
                    <table>
                        <tr>
                            <th>Stock Ticker Symbol</th>
                            <td id="tickerSymbol">${stock.ticker || 'N/A'}</td>
                        </tr>
                        <tr>
                            <th>Trading Day</th>
                            <td id="tradingDay">${new Date(stock.timestamp).toLocaleDateString() || 'N/A'}</td>
                        </tr>
                        <tr>
                            <th>Previous Closing Price</th>
                            <td id="prevClose">${stock.prevClose || 'N/A'}</td>
                        </tr>
                        <tr>
                            <th>Opening Price</th>
                            <td id="open">${stock.open || 'N/A'}</td>
                        </tr>
                        <tr>
                            <th>High Price</th>
                            <td id="high">${stock.high || 'N/A'}</td>
                        </tr>
                        <tr>
                            <th>Low Price</th>
                            <td id="low">${stock.low || 'N/A'}</td>
                        </tr>
                        <tr>
                            <th>Last Price</th>
                            <td id="last">${stock.last || 'N/A'}</td>
                        </tr>
                        <tr>
                            <th>Volume</th>
                            <td id="volume">${stock.volume || 'N/A'}</td>
                        </tr>
                    </table>
                `;
            } else {
                document.querySelector('.companydetails').innerHTML = '<p>No data available for this ticker.</p>';
            }
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
            document.querySelector('.companydetails').innerHTML = `<p>Error loading stock data. Please try again later.</p>`;
        });
}


// Event listener for "Stock Summary" link

function handleChartsClick(event) {
    event.preventDefault();
    
    document.querySelector('.companydetails').innerHTML = `
        <h1>display charts</h1>
    `;
}

function handleNewsClick(event) {
    event.preventDefault();
    document.querySelector('.companydetails').innerHTML = `
        <h1>display news</h1>
        
    `;
}


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
    document.addEventListener('click', function(event) {
        if (event.target.id === 'charts') {
            handleChartsClick(event);
        }
    });
    document.addEventListener('click', function(event) {
        if (event.target.id === 'latestNews') {
            handleNewsClick(event);
        }
    });
});
