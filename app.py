from flask import Flask, Response, render_template
#from waitress import serve
import os, sys
from camera import VideoCamera1


app = Flask(__name__)
app.config['SECRET_KEY'] = 'some super secret key'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/video')
def stream_page():
    return render_template('camera_stream.html')

def generator_loading(camera):
    while True:
       
        frame = camera.get_frame()
        
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_stream')
def cam_video_stream():
    return Response(generator_loading(VideoCamera1()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
    #serve(app, host="0.0.0.0", port=3000)