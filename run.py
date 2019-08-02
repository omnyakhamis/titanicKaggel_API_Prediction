import sys
import os

sys.path.append('API/model')
from API.app import create_app

server = create_app()

# server.run(host='0.0.0.0', port=os.environ['PORT'])
# server.run(host='0.0.0.0')
port = int(os.environ.get("PORT", 5000))
server.run(debug=True, host='0.0.0.0', port=port)
