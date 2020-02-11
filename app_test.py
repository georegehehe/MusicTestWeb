# coding=utf-8
import json
import os

from flask import Flask, render_template, request, make_response
from flask_cors import CORS, cross_origin
import audio_to_midi_melodia_test
from audio_to_midi_melodia_test import fill_ui_beats, ui_beats_to_notes, notes_to_ui, audio_to_midi_notes, detach_down_beats

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SECRET_KEY'] = 'secret!'


@app.route('/', methods=['GET', 'POST'])
def index_html():
    rst = make_response(render_template('index.html', name='stronger'))
    rst.headers['cache-control'] = 'no-cache, no-store, must-revalidate'
    rst.headers['pragma'] = 'no-cache'

    return rst


@app.route('/humming', methods=['GET', 'POST'])
@cross_origin()
def humming():
    if request.method == 'POST':
        f = request.files['audioData']
        f.save(os.path.join('static3', 'humming.wav'))
        notes = audio_to_midi_notes(infile=os.getcwd() + "/static3/humming.wav",
                                    smooth=0.001, minduration=0.11, speed=100)
        return json.dumps({"notes": notes_to_ui(notes)})


@app.route('/mix', methods=['GET', 'POST'])
@cross_origin()
def mix():
    if request.method == 'POST':
        data = request.get_data()
        data2 = json.loads(data, encoding='raw_unicode_escape')
        print "data 2 is " + str(data2["notes"])
        detached_ui = detach_down_beats(data2["notes"])
        filled_ui_beats = fill_ui_beats(detached_ui)
        data = ui_beats_to_notes(filled_ui_beats)

        data_raw = []
        for i in data:
            data_raw.append([i[0], i[1], i[2].encode('raw_unicode_escape')])

        print data_raw

        pyPlayCd = os.getcwd()
        py2PlayMusicshell = "%s/venv/bin/python %s/audio_to_midi_melodia_test.py" % (pyPlayCd, pyPlayCd)

        os.chdir(pyPlayCd)

        print "Calling shell: %s" % (py2PlayMusicshell + " \"" + str(data_raw) + "\"" + " \"" + str(audio_to_midi_melodia_test.downbeatbar) + "\"")
        val = os.system(py2PlayMusicshell + " \"" + str(data_raw) + "\"" + " \"" + str(audio_to_midi_melodia_test.downbeatbar) + "\"")
        val = os.system("rm -rf ./musicpiece*")
        print val

        ui_notes = notes_to_ui(data);

        print ui_notes

        return json.dumps({"notes": notes_to_ui(data), "duration": 41})


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
