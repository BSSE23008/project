import logging
from flask import Flask, jsonify

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>DevOps Mission Control</title>
   <style>
      :root { --primary: #00ff88; --bg: #0f172a; --card: #1e293b; --text: #e2e8f0; }
      body { background: var(--bg); color: var(--text); font-family: 'Segoe UI', system-ui, sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
      .container { text-align: center; max-width: 600px; padding: 20px; }
      .card { background: var(--card); padding: 40px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 1px solid #334155; }
      h1 { font-size: 2.5rem; margin-bottom: 10px; color: #fff; }
      .status-badge { display: inline-block; background: rgba(0, 255, 136, 0.1); color: var(--primary); padding: 8px 16px; border-radius: 50px; font-weight: bold; border: 1px solid var(--primary); margin-bottom: 20px; }
      .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 30px; }
      .stat { background: #0f172a; padding: 15px; border-radius: 12px; }
      .stat h3 { margin: 0; color: #94a3b8; font-size: 0.9rem; }
      .stat p { margin: 5px 0 0; font-size: 1.2rem; font-weight: bold; }
      .pulse { width: 10px; height: 10px; background: var(--primary); border-radius: 50%; display: inline-block; margin-right: 8px; animation: pulse 2s infinite; }
      @keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(0, 255, 136, 0.7); } 70% { box-shadow: 0 0 0 10px rgba(0, 255, 136, 0); } 100% { box-shadow: 0 0 0 0 rgba(0, 255, 136, 0); } }
   </style>
</head>
<body>
   <div class="container">
      <div class="card">
         <div class="status-badge"><span class="pulse"></span>SYSTEM OPERATIONAL</div>
         <h1>DevOps Exam Target</h1>
         <p>Phase 4 Deployment Successful. The pipeline is fully functional.</p>
         
         <div class="grid">
               <div class="stat">
                  <h3>Environment</h3>
                  <p>Kubernetes Pod</p>
               </div>
               <div class="stat">
                  <h3>Pipeline</h3>
                  <p>Jenkins CI/CD</p>
               </div>
               <div class="stat">
                  <h3>Container</h3>
                  <p>Dockerized</p>
               </div>
               <div class="stat">
                  <h3>Status</h3>
                  <p style="color: var(--primary);">Healthy</p>
               </div>
         </div>
      </div>
   </div>
</body>
</html>
"""


@app.route('/')
def dashboard():
   """Render the DevOps mission control dashboard."""
   logger.info("Dashboard accessed")
   return HTML_TEMPLATE


@app.route('/health', methods=['GET'])
def health_check():
   """Health check endpoint for Kubernetes liveness probes."""
   logger.info("Health check performed")
   return jsonify({
      'status': 'healthy',
      'service': 'devops-exam'
   }), 200


@app.errorhandler(404)
def not_found(error):
   """Handle 404 errors."""
   logger.warning(f"404 error: {error}")
   return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_error(error):
   """Handle 500 errors."""
   logger.error(f"500 error: {error}")
   return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
   logger.info("Starting DevOps Exam application")
   app.run(host='0.0.0.0', port=5000, debug=False)