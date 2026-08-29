from flask import Flask, render_template, jsonify

app = Flask(__name__)

script_steps = [
    {"stage": "Pembukaan", "dialogue": "Sayang, udah posisi paling nyaman di kasur belum? Merem ya..."},
    {"stage": "Pemanasan", "dialogue": "Bayangin aku lagi meluk kamu, tangan aku mulai nyentuh paha kamu..."},
    {"stage": "Eskalasi", "dialogue": "Aku lagi megang punya aku sekarang, keras banget ngebayangin bodi kamu..."},
    {"stage": "Klimaks / Stop", "dialogue": "Ahh... aku udah mau keluar, tahan sebentar... crot di dalam..."},
    {"stage": "Penutup", "dialogue": "Fyuuh... lemas banget. Makasih ya sayang, sekarang waktunya tidur nyenyak."}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_steps')
def get_steps():
    return jsonify(script_steps)
