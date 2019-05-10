# Copyright 2019, Digi International Inc.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import network
import time
import uftp

# Constants
FTP_HOST = "speedtest.tele2.net"
FTP_USER = "anonymous"
FTP_PASS = "anonymous@"

REMOTE_FILE = "1KB.zip"
LOCAL_FILE = "2b.txt"

PATH_ROOT = "/flash"
PATH_REMOTE_UPLOAD = "upload"


print(" +------------------------------------+")
print(" | XBee MicroPython FTP Client Sample |")
print(" +------------------------------------+\n")

cellular = network.Cellular()

print("- Waiting for the module to be connected to the cellular network... ",
      end="")
while not cellular.isconnected():
    time.sleep(5)
print("[OK]")

# Connect to the FTP server.
print("- Connecting to FTP server... ", end="")
ftp_conn = uftp.FTP(host=FTP_HOST)
ftp_conn.login(user=FTP_USER, passwd=FTP_PASS)
print("[OK]")

# Download a file from the FTP.
print("- Retrieving file '%s' (%d bytes)... " % (REMOTE_FILE,
                                                 ftp_conn.size(REMOTE_FILE)),
      end="")
start = time.time()
with open("%s/%s" % (PATH_ROOT, REMOTE_FILE), "w") as local_file:
    ftp_conn.retr(REMOTE_FILE, callback=local_file.write)
print("[OK]")
print("   * Time taken: %d seconds" % (time.time() - start))

# Upload a file to the 'update' folder of the FTP.
print("- Uploading file '%s'... " % LOCAL_FILE, end="")
ftp_conn.cwd(PATH_REMOTE_UPLOAD)
start = time.time()
ftp_conn.stor("%s/%s" % (PATH_ROOT, LOCAL_FILE), LOCAL_FILE)
print("[OK]")
print("   * Time taken: %d seconds" % (time.time() - start))

# Close connection.
print("- Closing FTP connection... ", end="")
ftp_conn.cwd("..")
ftp_conn.quit()
print("[OK]")

print("- Done")
