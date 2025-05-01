from flask import Flask, request, jsonify
from flask_cors import CORS
from page_replacement import PageReplacementSimulator
from visualization import generate_chart
import base64
import traceback

app = Flask(__name__)
CORS(app)

@app.route('/simulate', methods=['POST'])
def simulate():
    try:
        data = request.json
        if not data.get('reference_string') or not data.get('frames'):
            return jsonify({"error": "Missing required parameters"}), 400
        
        ref_str = data['reference_string']
        if isinstance(ref_str, str):
            ref_str = list(map(int, ref_str.split()))
        else:
            ref_str = list(map(int, ref_str))
            
        frames = int(data['frames'])
        if frames <= 0:
            return jsonify({"error": "Number of frames must be positive"}), 400

        simulator = PageReplacementSimulator(frames, ref_str)
        fifo_faults = simulator.fifo()
        lru_faults = simulator.lru()
        opt_faults = simulator.optimal()
        
        results = {
            "FIFO": fifo_faults,
            "LRU": lru_faults,
            "OPT": opt_faults
        }

        chart_img = generate_chart(results)
        chart_b64 = base64.b64encode(chart_img.getvalue()).decode('utf-8')

        return jsonify({
            "fifo_faults": fifo_faults,
            "lru_faults": lru_faults,
            "opt_faults": opt_faults,
            "chart": chart_b64
        })
        
    except Exception as e:
        print(f"Server Error: {str(e)}")
        print(traceback.format_exc())  
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)