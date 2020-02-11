# coding=utf-8
import json
import os

from flask import Flask, render_template, request, make_response, send_from_directory
from flask_cors import CORS, cross_origin

import audio_to_midi_melodia_test
from audio_to_midi_melodia import fill_ui_beats, ui_beats_to_notes, notes_to_ui, audio_to_midi_notes
from audio_to_midi_melodia_test import detach_down_beats

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SECRET_KEY'] = 'secret!'


@app.route('/', methods=['GET', 'POST'])
def index_html():
    rst = make_response(render_template('index.html', name='stronger'))
    rst.headers['cache-control'] = 'no-cache, no-store, must-revalidate'
    rst.headers['pragma'] = 'no-cache'

    return rst


# 传统模式
@app.route('/humming', methods=['GET', 'POST'])
@cross_origin()
def humming():
    if request.method == 'POST':
        f = request.files['audioData']
        f.save(os.path.join('static', 'humming.wav'))
        notes = audio_to_midi_notes(infile=os.getcwd() + "/static/humming.wav",
                                    smooth=0.001, minduration=0.11, speed=100)
        return json.dumps({"notes": notes_to_ui(notes)})


# 传统模式
@app.route('/mix', methods=['GET', 'POST'])
@cross_origin()
def mix():
    if request.method == 'POST':
        data = request.get_data()
        data2 = json.loads(data, encoding='raw_unicode_escape')
        print "data2 is " + str(data2)
        filled_ui_beats = fill_ui_beats(data2["notes"])

        data = ui_beats_to_notes(filled_ui_beats)

        data_raw = []
        for i in data:
            data_raw.append([i[0], i[1], i[2].encode('raw_unicode_escape')])

        print data_raw

        pyPlayCd = os.getcwd()
        py2PlayMusicshell = "%s/venv/bin/python %s/audio_to_midi_melodia.py" % (pyPlayCd, pyPlayCd)

        os.chdir(pyPlayCd)

        print "Calling shell: %s" % (py2PlayMusicshell + " \"%s\"" % data_raw)
        val = os.system(py2PlayMusicshell + " \"%s\"" % data_raw)
        val = os.system("rm -rf ./musicpiece*")
        print val

        ui_notes = notes_to_ui(data);

        print ui_notes

        return json.dumps({"notes": notes_to_ui(data), "duration": 41})

# 高级模式
@app.route('/mixAd', methods=['GET', 'POST'])
@cross_origin()
def mix_advanced():
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

        print "Calling shell: %s" % (py2PlayMusicshell + " \"" + str(data_raw) + "\"" + " \"" + str(
            audio_to_midi_melodia_test.downbeatbar) + "\"")
        val = os.system(py2PlayMusicshell + " \"" + str(data_raw) + "\"" + " \"" + str(
            audio_to_midi_melodia_test.downbeatbar) + "\"")
        val = os.system("rm -rf ./musicpiece*")
        print val

        ui_notes = notes_to_ui(data);

        print ui_notes

        return json.dumps({"notes": notes_to_ui(data), "duration": 41})

@app.route("/download")
def download():
    pyCd = os.getcwd()

    file_name = "finalversion.wav"
    file_path_name = "%s/static" % pyCd

    return send_from_directory(file_path_name, filename=file_name, as_attachment=True)


@app.route("/downloadAd")
def downloadAd():

    pyCd = os.getcwd()

    file_name = "finalversionAd.wav"

    file_path_name = "%s/static" % pyCd

    return send_from_directory(file_path_name, filename=file_name, as_attachment=True)


# 高级模式
@app.route('/hummingAd', methods=['GET', 'POST'])
@cross_origin()
def humming_advanced():
    if request.method == 'POST':
        f = request.files['audioData']
        f.save(os.path.join('static', 'hummingAd.wav'))
        notes = audio_to_midi_notes(infile=os.getcwd() + "/static/hummingAd.wav",
                                    smooth=0.001, minduration=0.11, speed=100)
        return json.dumps({"notes": notes_to_ui(notes)})





if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
