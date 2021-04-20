from talon import speech_system
from talon.engines.w2l import WebW2lEngine
w2l = WebW2lEngine(debug=False)
speech_system.add_engine(w2l)
