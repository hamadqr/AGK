"""
This module imports sound data from encrypted zip file and then loads sounds directly into memory. It can be useful for packing other stuff as well that needs to be inaccessible by users. You can use this to prevent users from modifying sounds and game maps, or cheeting your game save data.
If you make modifications, please share it with me.
"""

import libaudioverse
from Crypto.Cipher import AES
import hashlib
from io import BytesIO
import zipfile
import os
import random
import struct
import wave


class packer(object):
	def encrypt_file(self,key, in_filename, out_filename=None, chunksize=64*1024):
		key=hashlib.sha256(key).digest()
		if not out_filename:
			out_filename = in_filename + '.enc'
		iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
		encryptor = AES.new(key, AES.MODE_CBC, iv)
		filesize = os.path.getsize(in_filename)
		with open(in_filename, 'rb') as infile:
			with open(out_filename, 'wb') as outfile:
				outfile.write(struct.pack('<Q', filesize))
				outfile.write(iv)
				while True:
					chunk = infile.read(chunksize)
					if len(chunk) == 0:
						break
					elif len(chunk) % 16 != 0:
						chunk += ' ' * (16 - len(chunk) % 16)
					outfile.write(encryptor.encrypt(chunk))
		return key

	def decrypt_file(self,key, in_filename, out_filename=None, chunksize=24*1024):
		if not out_filename:
			out_filename = os.path.splitext(in_filename)[0]
		with open(in_filename, 'rb') as infile:
			origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
			iv = infile.read(16)
			decryptor = AES.new(key, AES.MODE_CBC, iv)
			with BytesIO() as outfile:
				while True:
					chunk = infile.read(chunksize)
					if len(chunk) == 0:
						break
					outfile.write(decryptor.decrypt(chunk))
				outfile.truncate(origsize)
				zip = zipfile.ZipFile(outfile)
				return {name: zip.read(name) for name in zip.namelist()}

	def load_sound_data(self,filename):
		buffer = libaudioverse.Buffer(server)
		buffer.decode_from_array(data[filename])
		return buffer

	def add_file(self,zipname,name):
		z=zipfile.ZipFile(zipname,"a")
		z.write(name)
		z.close()