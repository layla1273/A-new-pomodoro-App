from flask import Flask, request
import time

app = Flask(__name__)

@app.route('/pomodoro', methods=['POST'])
def pomodoro():
    data = request.json
    time_in_minutes = int(data['time'])
    start_time = time.time()
    end_time = start_time + (time_in_minutes * 60)

    while time.time() < end_time:
        pass
    
    return "Time is over!"

if __name__ == '__main__':
    app.run(debug=True)
