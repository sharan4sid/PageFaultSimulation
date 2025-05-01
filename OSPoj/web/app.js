document.addEventListener('DOMContentLoaded', function() {
  const runButton = document.getElementById('runBtn');
  if (runButton) {
    runButton.addEventListener('click', runSimulation);
  } else {
    console.error("Run button not found in the DOM");
  }
});
function updateResults(data) {
  const resultsDiv = document.getElementById('results');
  const chartDiv = document.getElementById('chart');
  if (!resultsDiv || !chartDiv) {
    showError('Results display elements not found');
    return;
  }
  const fifoElement = document.getElementById('fifoResult');
  const lruElement = document.getElementById('lruResult');
  const optElement = document.getElementById('optResult');
  
  if (fifoElement && lruElement && optElement) {
    fifoElement.textContent = data.fifo_faults;
    lruElement.textContent = data.lru_faults;
    optElement.textContent = data.opt_faults;
  }
  if (data.chart) {
    chartDiv.innerHTML = `
      <img src="data:image/png;base64,${data.chart}" 
           class="chart-image" 
           alt="Algorithm Comparison Chart">`;
  } else {
    chartDiv.innerHTML = '<p class="error">Failed to generate comparison chart</p>';
  }

  resultsDiv.style.opacity = '0';
  void resultsDiv.offsetWidth; 
  resultsDiv.style.opacity = '1';
}

async function runSimulation() {
  const loading = document.getElementById('loading');
  const errorDiv = document.getElementById('error');
  const refStr = document.getElementById('referenceString').value;
  const frames = document.getElementById('frames').value;

  if (!refStr || !frames) {
    showError('Please enter both reference string and number of frames');
    return;
  }

  errorDiv.classList.remove('show');
  loading.style.display = 'flex';
  
  try {
    const response = await fetch('http://localhost:5001/simulate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        reference_string: refStr,
        frames: parseInt(frames)
      })
    });

    if (!response.ok) {
      throw new Error(`Server responded with status: ${response.status}`);
    }

    const data = await response.json();
    
    if (data.error) {
      throw new Error(data.error);
    }
    
    updateResults(data);
    
  } catch (error) {
    showError(error.message || 'Failed to connect to server');
  } finally {
    loading.style.display = 'none';
  }
}

function showError(message) {
  const errorDiv = document.getElementById('error');
  errorDiv.textContent = message;
  errorDiv.classList.add('show');
  setTimeout(() => errorDiv.classList.remove('show'), 5000);
}